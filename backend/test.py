import requests
import json
from datetime import date, timedelta
import numpy as np



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


def getEMA(ticker):
  today = date.today()
  yesterday = date.today() - timedelta(days=1)
  ti = ticker
  end = "&apikey=A1VFP8M71VTXQIVO"
  url = 'https://www.alphavantage.co/query?function=EMA&symbol=' + ti + '&interval=daily&time_period=2&series_type=open' + end
  response = requests.get(url)
  parsed = json.loads(response.text)
  i = 0
  todaysEMA = parsed["Technical Analysis: EMA"][str(today)]['EMA']
  return todaysEMA

def currentPrice(ticker):
  today = date.today()
  base = "https://www.alphavantage.co/query?function=TIME_SERIES_DAILY_ADJUSTED&symbol="
  ti = ticker
  end = "&apikey=A1VFP8M71VTXQIVO"
  url = base + ti + end
  response = requests.get(url)
  parsed = json.loads(response.text)

  todaysPrice = parsed['Time Series (Daily)'][str(today)]['4. close']
  return todaysPrice

def emaIndication(ticker):
  ema = getEMA(ticker)
  price = currentPrice(ticker)
  buy = False
  
  if price > ema:
    buy = True
    print('Buy signal')
    return buy
  else:
    print('Dont buy')
    return buy

emaIndication('MSFT')


