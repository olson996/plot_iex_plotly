#!/usr/bin/env python
import numpy as np
import pandas as pd
def header(msg):
    print('-' * 50)
    print('[' + msg + ']')

header("load data into dataframe")
filename = 'sample.csv'
df = pd.read_csv(filename)


header('df.head(5) prints first 5')
print(df.head(5))
header('df.tail(5) prints last 5')
print(df.tail(5))
header('df.index total rows')
print(df.index)
header('df.columns')
print(df.columns)
header('df.values')
print(df.values)
header('df.dtypes prints data types')
print(df.dtypes)
#header('df.describe()')
#print(df.describe)
header('df.sort_values("eq_site_deductible", ascending=False)')
print(df.sort_values('eq_site_deductible', ascending=True))
