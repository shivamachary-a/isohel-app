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


cunt = getAdjClose('MSFT')

print(stockVolatility(cunt))


