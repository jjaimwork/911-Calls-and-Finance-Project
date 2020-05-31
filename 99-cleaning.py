# -*- coding: utf-8 -*-
"""
Created on Sat May 30 12:53:58 2020

@author: Gilgamesh
"""

import pandas as pd
import numpy as np

df = pd.read_csv('911.csv')
df.columns

# create a separate columns for types and its desc
df['type'] = df['title'].apply(lambda x: x.split(': ')[0])
df['reason'] = df['title'].apply(lambda x: x.split(': ')[-1].replace('-',''))

# create separate values for data column
df['timeStamp']=pd.to_datetime(df['timeStamp'])
df['Year'] = df['timeStamp'].apply(lambda time: time.year)
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].map(dmap)
df.to_csv('911_cleaned.csv',index=False)
