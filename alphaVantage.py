# -*- coding: utf-8 -*-
"""
Created on Fri Mar 12 18:56:22 2021

@author: Kianoosh Keshavarzian
"""

import alpha_vantage
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.foreignexchange import ForeignExchange

import pandas as pd

ts = TimeSeries(key='your key here', output_format='pandas')
fx = ForeignExchange(key='your key here', output_format='pandas')

data_GOLD, meta_data = ts.get_daily_adjusted (symbol='GDDCF', outputsize='full')

data_EUR_USD, meta_data = fx.get_currency_exchange_daily (from_symbol='EUR', to_symbol='USD', outputsize='full')

#help(ForeignExchange)
data, metadata = ts.get_symbol_search(keywords='gold')

data_AudUsd.to_csv('data_AudUsd.csv')
data_AudUsd = pd.read_csv('data_AudUsd.csv')

import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='root', password='your password here',
                              host='0.0.0.0',
                              database='stock_market')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = cnx.cursor()
  
  # creating column list for insertion
  cols = "`,`".join([str(i) for i in data_AudUsd.columns.tolist()])
  
  # Insert DataFrame recrds one by one
  for i,row in data_AudUsd.iterrows():
    sql = "INSERT INTO AUD_USD (`" +cols + "`) VALUES (" + "%s,"*(len(row)-1) + "%s)"
    cursor.execute(sql, tuple(row))

  # the connection is not autocommitted by default, so we must commit to save our changes
  cnx.commit()
  cursor.close()
  cnx.close()
