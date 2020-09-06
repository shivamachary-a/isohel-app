import numpy as np
import scipy
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
vol = []
emaSignal = []

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

def getEMA(ticker):
  today = date.today()
  prior = date.today() - timedelta(days=1)
  prior2 = date.today() - timedelta(days=2)
  prior3 = date.today() - timedelta(days=3)
  ti = ticker
  end = "&apikey=A1VFP8M71VTXQIVO"
  url = 'https://www.alphavantage.co/query?function=EMA&symbol=' + ti + '&interval=daily&time_period=2&series_type=open' + end
  response = requests.get(url)
  parsed = json.loads(response.text)
  success = False
  print(url)
  
  try:
    todaysEMA = parsed["Technical Analysis: EMA"][str(today)]['EMA']
  except KeyError:
    try:
      todaysEMA = parsed["Technical Analysis: EMA"][str(prior)]['EMA']
    except KeyError:
      try:
        todaysEMA = parsed["Technical Analysis: EMA"][str(prior2)]['EMA']
      except KeyError:
          todaysEMA = parsed["Technical Analysis: EMA"][str(prior3)]['EMA']      
  return todaysEMA

def currentPrice(ticker):
  today = date.today()
  prior = date.today() - timedelta(days=1)
  prior2 = date.today() - timedelta(days=2)
  prior3 = date.today() - timedelta(days=3)
  base = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="
  ti = ticker
  end = "&apikey=A1VFP8M71VTXQIVO"
  url = base + ti + end
  response = requests.get(url)
  parsed = json.loads(response.text)
  print(url)
  try:
    todaysPrice = parsed['Time Series (Daily)'][str(today)]['4. close']
  except KeyError:
    try:
      todaysPrice = parsed['Time Series (Daily)'][str(prior)]['4. close']
    except KeyError:
      try:
        todaysPrice = parsed['Time Series (Daily)'][str(prior2)]['4. close'] 
      except KeyError:
        todaysPrice = parsed['Time Series (Daily)'][str(prior3)]['4. close']
  return todaysPrice

def emaIndication(ticker):
  ema = getEMA(ticker)
  price = float(currentPrice(ticker))
  buy = False
  
  if price > float(ema):
    buy = True
    print('Buy signal')
    return buy
  else:
    print('Dont buy')
    return buy

def stockVolatility (values):
  returns = []
  for i in range (1, len(values)-1):
    returns.append(np.log(values[i]/values[i-1]))
  deviation = np.std(returns)
  return (deviation * np.sqrt(252))*100

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
def bAndS():
  response_object = {'status': 'success'} #creating the object to send back to the frontend
  if request.method == 'POST': #determining its a POST request, so we are receiving data
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
    #assigning returns of the functions to variables
    call = float(euro_vanilla_call(stocks['Price'], stocks['Strike'], stocks['Time'], stocks['Interest'], stocks['Volatility']))
    put = float(euro_vanilla_put(stocks['Price'], stocks['Strike'], stocks['Time'], stocks['Interest'], stocks['Volatility']))
    
    options.append({
      'Ticker': stocks['Ticker'],
      'Call': call,
      'Put' : put,
    })
    #creating a response object holding the function return
    response_object['options'] = options
    print(options)
  else: #the only request types are POST and GET, hence if its not a POST, its get and we just have to return the response object.
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
    vol.insert(0, {
      'Result': result
    })
    print(vol)
  else:
    response_object['yonk'] = vol
  return jsonify(response_object)

@app.route('/analysis', methods=['GET','POST'])
def analysis():
  response_object = {'status': 'success'}
  if request.method == 'POST':
    post_data = request.get_json()
    print(post_data)
    stock = post_data.get('ticker')
    print(stock)
    result = emaIndication(stock)
    print(result)
    emaSignal.insert(0,{
      'Result': result,
      'Price': currentPrice(stock)
    })
    print(emaSignal)
  else:
    response_object['yonk'] = emaSignal
    print(response_object)
  return jsonify(response_object)



    