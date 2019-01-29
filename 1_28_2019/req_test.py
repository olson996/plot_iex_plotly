import plotly.plotly as py 
from plotly.graph_objs import *
py.sign_in('olson996', 'cVbzRp6ynrE6pYndwJIZ')
import requests
import json
import pandas as pd
r = requests.get('https://api.iextrading.com/1.0/stock/aapl/chart/5y')
j_data = json.loads(r.text)
df = pd.DataFrame(j_data)
trace1 = {
  "x": ["2018-10-29", "2018-10-30", "2018-10-31", "2018-11-01", "2018-11-02", "2018-11-05", "2018-11-06", "2018-11-07", "2018-11-08", "2018-11-09", "2018-11-12", "2018-11-13", "2018-11-14", "2018-11-15", "2018-11-16", "2018-11-19", "2018-11-20", "2018-11-21", "2018-11-23", "2018-11-26", "2018-11-27", "2018-11-28", "2018-11-29", "2018-11-30", "2018-12-03", "2018-12-04", "2018-12-06", "2018-12-07", "2018-12-10", "2018-12-11", "2018-12-12", "2018-12-13", "2018-12-14", "2018-12-17", "2018-12-18", "2018-12-19", "2018-12-20", "2018-12-21", "2018-12-24", "2018-12-26"], 
  "close": [212.240005, 213.300003, 218.860001, 222.220001, 207.479996, 201.589996, 203.770004, 209.949997, 208.490005, 204.470001, 194.169998, 192.229996, 186.800003, 191.410004, 193.529999, 185.860001, 176.979996, 176.779999, 172.289993, 174.619995, 174.240005, 180.940002, 179.550003, 178.580002, 184.820007, 176.690002, 174.720001, 168.490005, 169.600006, 168.630005, 169.100006, 170.949997, 165.479996, 163.940002, 166.070007, 160.889999, 156.830002, 150.729996, 146.830002, 157.169998], 
  "closesrc": "spreddy:2:4b5afa", 
  "high": [219.690002, 215.179993, 220.449997, 222.360001, 213.649994, 204.389999, 204.720001, 210.059998, 210.119995, 206.009995, 199.850006, 197.179993, 194.479996, 191.970001, 194.970001, 190.699997, 181.470001, 180.270004, 176.600006, 174.949997, 174.770004, 181.289993, 182.800003, 180.330002, 184.940002, 182.389999, 174.779999, 174.490005, 170.089996, 171.789993, 171.919998, 172.570007, 169.080002, 168.350006, 167.529999, 167.449997, 162.110001, 158.160004, 151.550003, 157.229996], 
  "highsrc": "spreddy:2:07df62", 
  "line": {"color": "rgba(31,119,180,1)"}, 
  "low": [206.089996, 209.270004, 216.619995, 216.809998, 205.429993, 198.169998, 201.690002, 204.130005, 206.75, 202.25, 193.789993, 191.449997, 185.929993, 186.899994, 189.460007, 184.990005, 175.509995, 176.550003, 172.100006, 170.259995, 170.880005, 174.929993, 177.699997, 177.029999, 181.210007, 176.270004, 170.419998, 168.300003, 163.330002, 167, 169.020004, 169.550003, 165.279999, 162.729996, 164.389999, 159.089996, 155.300003, 149.630005, 146.589996, 146.720001], 
  "lowsrc": "spreddy:2:66396e", 
  "open": [219.190002, 211.149994, 216.880005, 219.050003, 209.550003, 204.300003, 201.919998, 205.970001, 209.979996, 205.550003, 199, 191.630005, 193.899994, 188.389999, 190.5, 190, 178.369995, 179.729996, 174.940002, 174.240005, 171.509995, 176.729996, 182.660004, 180.289993, 184.460007, 180.949997, 171.759995, 173.490005, 165, 171.660004, 170.399994, 170.490005, 169, 165.449997, 165.380005, 166, 160.399994, 156.860001, 148.149994, 148.300003], 
  "opensrc": "spreddy:2:8d663b", 
  "text": [None, None, None, None, None, None, None, None, None, None, None, None, True, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None], 
  "textsrc": "spreddy:2:093ceb", 
  "type": "candlestick", 
  "xaxis": "x", 
  "xsrc": "spreddy:2:f1560b", 
  "yaxis": "y"
}
data = Data([trace1])
layout = {
  "hovermode": "closest", 
  "margin": {
    "r": 10, 
    "t": 25, 
    "b": 40, 
    "l": 60
  }, 
  "showlegend": False, 
  "title": "CandleStick Chart", 
  "xaxis": {
    "automargin": True, 
    "domain": [0, 1], 
    "title": "Date"
  }, 
  "yaxis": {
    "automargin": True, 
    "domain": [0, 1]
  }
}
fig = Figure(data=data, layout=layout)
plot_url = py.plot(fig)

	