import yfinance as yf
import datetime as dt

# Current date
current = dt.datetime.now()

# Start date (one year ago from the current date)
start = dt.datetime(current.year - 1, current.month, current.day)

# End date (today, could be omitted as it's the default behavior to get data up to the current date)
end = dt.datetime(current.year, current.month, current.day)

# Define the ticker symbol
tickerSymbol = 'AAPL'

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
# Formatting the start and end dates as strings in the format 'YYYY-MM-DD'
tickerDf = tickerData.history(start=start.strftime('%Y-%m-%d'), end=end.strftime('%Y-%m-%d'))

# Save the data to CSV
tickerDf.to_csv('AAPL.csv')
