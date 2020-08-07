import numpy as np
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf
from sympy import init_printing
init_printing()
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from datetime import date, timedelta
import requests
import json




app = Flask(__name__) #initiates flask app

stocks = {}
options = []
volol = []

CORS(app, resources={r'/*': {'origins': '*'}})

def getAdjClose(ticker):
  today = date.today()
  base = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="
  ti = ticker
  end = "&apikey=A1VFP8M71VTXQIVO"
  url = base + ti + end
  response = requests.get(url)
  parsed = json.loads(response.text)

  values = []

  i = 0
  while i < 200:
    try:
      d = date.today() - timedelta(days=i)
      values.append(float(parsed['Time Series (Daily)'][str(d)]['4. close']))
      i = i + 1
    except KeyError:
      i = i + 1
      
  return values

def stockVolatility (values):
  return np.std(values) * np.sqrt(len(values))

def euro_vanilla_call(S, K, T, r, sigma):
    
    #S: spot price
    #K: strike price
    #T: time to maturity
    #r: interest rate
    #sigma: volatility of underlying asset
    
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    call = (S * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    
    return call

def euro_vanilla_put(S, K, T, r, sigma):


  #S: spot price
  #K: strike price
  #T: time to maturity
  #r: interest rate
  #sigma: volatility of underlying asset
  
  d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
  d2 = (np.log(S / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
  
  put = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0) - S * si.norm.cdf(-d1, 0.0, 1.0))
  
  return put




@app.route('/', methods=['GET', 'POST']) #creating the base route for the application
def yeet():
  response_object = {'status': 'success'} #creating the object to send back to the frontend
  if request.method == 'POST':
    post_data = request.get_json() #getting the data sent from the frontend
    #creating object holding data from post request
    stocks = {
      'Ticker': post_data.get('Ticker'),
      'Price': float(post_data.get('Price')),
      'Strike': float(post_data.get('Strike')),
      'Time': float(post_data.get('Time')),
      'Interest': float(post_data.get('Interest')),
      'Volatility': float(post_data.get('Volatility')),
    }
    call = float(euro_vanilla_call(stocks['Price'], stocks['Strike'], stocks['Time'], stocks['Interest'], stocks['Volatility']))
    put = float(euro_vanilla_put(stocks['Price'], stocks['Strike'], stocks['Time'], stocks['Interest'], stocks['Volatility']))
    
    options.append({
      'Ticker': stocks['Ticker'],
      'Call': call,
      'Put' : put,
    })
    response_object['options'] = options
    print(options)
  else:
    response_object['stocks'] = options
  return jsonify(response_object)

@app.route('/volatility', methods=['GET','POST'])
def volatility():

  response_object = {'status': 'success'}
  if request.method == 'POST':
    post_data = request.get_json()
    print(post_data)
    #response should just have a ticker name
    stock = post_data.get('ticker')
    close =  getAdjClose(stock)
    result = stockVolatility(close)
    print(result)
    volol.insert(0, {
      'Result': result
    })
    print(volol)
  else:
    response_object['yonk'] = volol
  return jsonify(response_object)
  



    