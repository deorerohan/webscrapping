#!/usr/bin/env python
import matplotlib.pyplot as plt
from matplotlib.dates import DateFormatter, WeekdayLocator,\
     DayLocator, MONDAY
import matplotlib.finance as f


# (Year, month, day) tuples suffice as args for quotes_historical_yahoo
date1 = (2015, 4, 8)
date2 = (2015, 5, 8)


mondays = WeekdayLocator(MONDAY)        # major ticks on the mondays
alldays = DayLocator()              # minor ticks on the days
weekFormatter = DateFormatter('%b %d')  # e.g., Jan 12
dayFormatter = DateFormatter('%d')      # e.g., 12

quotes = f.quotes_historical_yahoo('YHOO', date1, date2)
#print quotes # open close high low volume

if len(quotes) == 0:
    raise SystemExit

fig, ax = plt.subplots(figsize=(16, 10))
fig.subplots_adjust(bottom=0.15)
#fig.set_size_inches(18.5,10.5)
fig.set_size_inches(25,15)
ax.xaxis.set_major_locator(mondays)
ax.xaxis.set_minor_locator(alldays)
ax.xaxis.set_major_formatter(weekFormatter)
#ax.xaxis.set_minor_formatter(dayFormatter)

#plot_day_summary(ax, quotes, ticksize=3)
f.candlestick(ax, quotes, width=0.4)

ax.xaxis_date()
ax.autoscale_view()
plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')

plt.show()
