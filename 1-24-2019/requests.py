#!/usr/bin/env python 
import sys
sys.path.append('Users/User_1/Documents/myproj/1-24-2019/iex_data')
import iex_data as IEX
iex = IEX.API()
iex.get_latest_quote_and_trade(['AAPL', 'IBM'])