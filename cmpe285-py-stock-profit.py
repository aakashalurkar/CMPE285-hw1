#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

def get_company_name(ticker):
    url = "http://d.yimg.com/autoc.finance.yahoo.com/autoc?query={}&region=1&lang=en".format(ticker)
    res = requests.get(url).json()
    for i in res['ResultSet']['Result']:
        if i['symbol'] == ticker:
            return i['name']

stock_symbol = input("Enter a stock symbol ")
stock_symbol = stock_symbol.upper()
company_name = get_company_name(stock_symbol)

allotment = input("Enter allotment ")
allotment = float(allotment)

initial_share_price = input("Enter initial share price ")
initial_share_price = float(initial_share_price)

buy_commission = input("Enter buy commission ")
buy_commission = float(buy_commission)

final_share_price = input("Enter final share price ")
final_share_price = float(final_share_price) 

sell_commission = input("Enter sell commission ")
sell_commission = float(sell_commission)

capital_gains_tax = input("Enter Capital Gains Tax ")
capital_gains_tax = float(capital_gains_tax)

print("\n\n")
print("Company Details: ", "(",stock_symbol,")" ,company_name,"\n")
print("Allotment is ",allotment,"\n")
print("Final Share Price is ","$",final_share_price,"\n")
print("Sell Commission is ",sell_commission,"\n")
print("Initial Share Price ",initial_share_price,"\n")
print("Buy Commission ",buy_commission,"\n")
print("Capital Gain Tax Rate ",capital_gains_tax,"%","\n")

print("--------------------------------------------")
print()

proceeds = final_share_price*allotment
proceeds = float("%.2f" % proceeds)

total_purchase_price = allotment*initial_share_price
total_purchase_price = float("%.2f" % total_purchase_price)

cost_for_profit = (total_purchase_price + buy_commission + sell_commission)
cost_for_profit = float("%.2f" % cost_for_profit)

net_profit = proceeds - cost_for_profit
net_profit = float("%.2f" % net_profit)

tax_on_capital_gain = (capital_gains_tax / 100) * net_profit
tax_on_capital_gain = float("%.2f" % tax_on_capital_gain)

final_cost = cost_for_profit + tax_on_capital_gain
final_cost = float("%.2f" % final_cost)

final_net_profit = net_profit - tax_on_capital_gain
final_net_profit = float("%.2f" % final_net_profit)

return_on_investment = (final_net_profit*100)/final_cost
return_on_investment = float(return_on_investment)

break_even = ((buy_commission + sell_commission) / allotment) + initial_share_price

print("PROFIT REPORT: ","\n")
print("Proceeds: ","$","%.2f" % proceeds,"\n")
print("Cost: ","$","%.2f" % final_cost,"\n")
print("Total Purchase Price: ", "%.2f" % total_purchase_price,"\n")

if final_net_profit > 0:
  print("Tax on Capital Gain: ", "%.2f" % tax_on_capital_gain,"\n")
  print("Net Profit: ","$","%.2f" % final_net_profit,"\n")
  print("Return on Investment: ","%.2f" % return_on_investment, "%","\n")
else:
  final_net_profit = -1*final_net_profit
  print("Net Loss: ","$","%.2f" % final_net_profit,"\n")
  return_on_investment = -1*return_on_investment
  print("Loss on Investment: ","%.2f" % return_on_investment, "%","\n")

print("To break even you should have a final share price of: ","$",break_even,"\n")


# In[ ]:





# In[ ]:




