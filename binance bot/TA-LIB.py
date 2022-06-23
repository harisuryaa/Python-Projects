import talib
import numpy

from numpy import genfromtxt

my_data = genfromtxt('1_day.csv', delimiter=' ')

d = my_data[:,4]
print(d)

rsi_ana = talib.RSI(d)
sma_ana = talib.SMA(d)

print(rsi_ana)
print(sma_ana)

rsi_sma = talib.RSI(sma_ana)
print(rsi_sma)