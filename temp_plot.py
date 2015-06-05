import datetime
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.cbook as cbook
import csv
from pylab import plotfile, show, gca,savefig 

years    = mdates.YearLocator()   # every year
months   = mdates.MonthLocator()  # every month
yearsFmt = mdates.DateFormatter('%Y-%m-%d')

letter = '%s, %s, %s' %('sdq','ege','vfdger')
print letter
#datafile = cbook.get_sample_data('/home/rohan/Documents/repos/data.csv')


csvfile= cbook.get_sample_data('/home/rohan/Documents/repos/data.csv', asfileobj=False)

#plotfile(csvfile, ('date', 'tempurature'))
plotfile(csvfile,('date', 'tempurature', 'pressure', 'humidity', 'wind_speed'))
savefig('graph.png')
show()

'''
datareader = csv.reader(csvfile)

for row in datareader:
    content = list(row[0])
    print content


fig, ax = plt.subplots()
ax.plot(datareader['year'], datareader['temp'])

csvfile.close()

# format the ticks
ax.xaxis.set_major_locator(years)
ax.xaxis.set_major_formatter(yearsFmt)
ax.xaxis.set_minor_locator(months)

datemin = datetime.date(r.date.min().year, 1, 1)
datemax = datetime.date(r.date.max().year+1, 1, 1)
ax.set_xlim(datemin, datemax)

# format the coords message box
def price(x): return '$%1.2f'%x

ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
ax.format_ydata = price
ax.grid(True)

# rotates and right aligns the x labels, and moves the bottom of the
# axes up to make room for them
fig.autofmt_xdate()

plt.show()
'''
