import urllib.request as urllib2
import requests
from requests import ReadTimeout, ConnectTimeout, HTTPError, Timeout, ConnectionError
import sys
import datetime
from datetime import datetime
import pytz 
from pytz import reference, timezone


def all():
  
  # get_company_name
  
    def get_company_name(ticker):
      url ="http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(ticker)
      res = requests.get(url).json()
      for i in res['ResultSet']['Result']:
        if i['symbol'] == ticker:
          return i['name']

    stock_symbol = input("Enter a stock symbol ")
    print()
    stock_symbol = stock_symbol.upper()
    company_name = get_company_name(stock_symbol)
    to_put_in_url = stock_symbol.lower()
  
  # get_current_date
  
    utc = datetime.now(timezone('UTC'))
    pacific = utc.astimezone(timezone('US/Pacific'))
    date = pacific.strftime("%a, %d-%b-%Y %I:%M:%S, " + "%Z%z")

    headers = {
        'Content-Type': 'application/json'
    }
    
    url = "https://api.tiingo.com/iex/?tickers="+to_put_in_url+"&token=6acb967bbf31715249a8ac874ca4c20cd78bc508"
        
  # handle_network_error
  
    def connected(host='https://trinket.io/python3/71395563d6?outputOnly=true&runOption=run'):
      try:
          urllib.urlopen(host)
          return True
      except:
          return False
  
    try:
      response = requests.get(url, headers=headers, timeout=1)
    except requests.ConnectionError:
      print("No internet connection available")
    
  
  # calculate_values
  
    res = response.json()
    if res==[]:
        print("invalid symbol")
        return
    r = res[0]
    latest_price = r['last']
    prev_close = r['prevClose']
    
    value_change = latest_price - prev_close
    percent_change = (value_change*100)/(prev_close)
    value = round(value_change,2)
    percent = round(percent_change,2)
    
    if value > 0:
      v_change = value
      v_change = "+" + str(v_change)
    else:
      v_change = str(value)
    
    if percent > 0:
      p_change = percent
      p_change = "+" + str(p_change)
    else:
      p_change = str(percent)
        
  # show_results
  
    print()
    print(date)
    print()
    print("Company Details: ","(",stock_symbol,")" ,company_name)
    lp = str(latest_price)
    print()
    vc = str(v_change)
    pc = str(p_change)
    print(lp + " "+ vc + " " + "("+ pc + " %)")
    print()

st = "\n cmpe285 - aakash alurkar \n welcome to python finance info - homework 2 \n press 1 to start \n press 2 to exit \n"
while True:
    flag = input(st)
    if flag =="1":
        all()
    elif flag =="2":
        print("thank you!")
        break
    else:
        print("wrong input")
    st = "do you want to start over ? \n 1: yes 2: no \n"