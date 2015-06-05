from pylab import *
import matplotlib.pyplot as plt
from datetime import datetime
import time
from matplotlib.dates import  DateFormatter, WeekdayLocator, HourLocator, \
     DayLocator, MONDAY
from matplotlib.finance import candlestick,\
     plot_day_summary, candlestick2
from yahoo_finance import Share


#-----------------------------------
stock = Share('YHOO')
print stock.get_open()
info = stock.get_info()

print info['symbol']
print info['start']
print info['end']
print info['CompanyName']
#print info

#startDate = info['start']
#endDate = info['end']

startDate = '2015-2-1'
endDate = '2015-5-1'

hist = stock.get_historical(startDate, endDate)
#------------------------------------

mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays    = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%d %m %Y')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

#starting from dates expressed as strings...
Date1 = '01/01/2010'
Date2 = '02/01/2010'
#...you convert them in float numbers....
Date1 = date2num(datetime.strptime(Date1, "%d/%m/%Y"))
Date2 = date2num(datetime.strptime(Date2, "%d/%m/%Y"))
#so redefining the Prices list of tuples...
#u'Volume': u'28720000', u'Symbol': u'YHOO', u'Adj_Close': u'35.83', u'High': u'35.89'
#, u'Low': u'34.12', u'Date': u'2014-04-29', u'Close': u'35.83', u'Open': u'34.37'}
#date, open close, high, low
#Prices = [(Date1, 1.123, 1.212, 1.463, 1.056), (Date2,1.121, 1.216, 1.498, 1.002)]

Prices = list()

for row in hist:
	Date1 = date2num(datetime.strptime(row['Date'], "%Y-%m-%d"))
	Prices.append((Date1, float(row['Open']), float(row['Close']), 
	float(row['High']), float(row['Low'])))
#and then following the official example. 
fig, ax = plt.subplots(figsize=(16, 10))
fig.subplots_adjust(bottom=0.2)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
candlestick(ax, Prices, width=0.6)

ax.xaxis_date()
ax.autoscale_view()
plt.setp( plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()
