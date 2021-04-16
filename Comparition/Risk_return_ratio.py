#This is a visualization of the expected returns and volatilitys of several choosen shares.
#@author Marius Haueis
#@version 16.04.2021

import pandas_datareader.data as web
from matplotlib import pyplot as plt
import numpy as np

#import of data
api_key = None #insert your Tiingo api key here.

intel = web.get_data_tiingo("INTC", api_key=api_key)
adobe = web.get_data_tiingo("ADBE", api_key=api_key)
morgan_stanley = web.get_data_tiingo("MS", api_key=api_key)
boeing = web.get_data_tiingo("BCO", api_key=api_key)
ea = web.get_data_tiingo("EA", api_key=api_key)
exxon = web.get_data_tiingo("XOM", api_key=api_key)
home_depot = web.get_data_tiingo("HD", api_key=api_key)
stocks = [intel, adobe, morgan_stanley, boeing, ea, exxon, home_depot]
stocks_name = ["Intel", "Adobe", "Morgan Stanley", "Boeing", "EA", "Exxon", "Home Depot"] 

#returns and risk calculation
def stage(df):
    closing_price = df["close"].pct_change()
    ic = closing_price[1:]
    avg_ret = ic.mean()
    variance = 0.00
    for i in ic:
        variance += np.square(np.abs(i-avg_ret))      
    svariance = variance/(len(closing_price)-1)   
    standard_deviation= np.sqrt(svariance)
    return avg_ret*100, (standard_deviation*100)*(np.sqrt(252))

#plotting
ax = plt.subplot()
for i in stocks:
    ret, vola = stage(i) 
    ax.scatter(ret*250, vola)

plt.legend(stocks_name, loc=2)

#labeling
plt.title("Comparation")
plt.xlabel("Expected return")
plt.ylabel("Expected Volatility ")
plt.show()