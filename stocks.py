from yahoo_finance import Share

#YHOO , BSE-100.BO
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

startDate = '2015-4-8'
endDate = '2015-5-8'

hist = stock.get_historical(startDate, endDate)
#print hist

file=open('stocksdata.csv','w')
file.write('Date, Volume, Adj_Close, High, Low, Open, Close\n')


for row in hist:
    print row['Date']
    #print row['Volume']
    #print row['Adj_Close']
    #print row['High']
    #print row['Low']
    #print row['Open']
    #print row['Close']
    
    file.write('%s, %s, %s, %s, %s, %s, %s\n' 
    %(row['Date'], row['Volume'], row['Adj_Close'], row['High'],
    row['Low'], row['Open'], row['Close']))

file.close()
'''{'Volume': '28736000', 'Symbol': 'YHOO', 
'Adj_Close': '35.83', 'High': '35.89', 
'Low': '34.12', 'Date': '2014-04-29', 
'Close': '35.83', 'Open': '34.37'}
'''
