import numpy as np
import scipy.stats as si
import sympy as sy
from sympy.stats import Normal, cdf
from sympy import init_printing
init_printing()
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS




app = Flask(__name__) #initiates flask app

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/

stocks = {}
options = []

CORS(app, resources={r'/*': {'origins': '*'}})

def euro_vanilla_call(S, K, T, r, sigma):

    # This function uses the Black and Scholes formula to determine the value of a call option.
    
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

  # This function uses the Black and Scholes formula to determine the value of a put option.

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

@app.route('/volatility', methods=['GET', 'POST'])
def volatility():
  response_object = {'status': 'success'}
  if request.method == 'POST':
    post_data = request.get_json()
    #response should just have a ticker name


    