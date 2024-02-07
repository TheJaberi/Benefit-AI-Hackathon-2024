import yfinance as yf
import datetime as dt
import sys  # Import the sys module

# Check if a command line argument was provided
if len(sys.argv) > 1:
    tickerSymbol = sys.argv[1]  # Use the first command line argument as the ticker symbol
else:
    print("Usage: python script_name.py STOCK_TICKER")
    sys.exit(1)  # Exit the script if no ticker symbol is provided

# Current date
current = dt.datetime.now()

# Start date (five years ago from the current date)
start = dt.datetime(current.year - 5, current.month, current.day)

# End date (today, could be omitted as it's the default behavior to get data up to the current date)
end = dt.datetime(current.year, current.month, current.day)

# Get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get the historical prices for this ticker
# Formatting the start and end dates as strings in the format 'YYYY-MM-DD'
tickerDf = tickerData.history(start=start.strftime('%Y-%m-%d'), end=end.strftime('%Y-%m-%d'))

# Save the data to CSV, naming the file 'stock_data.csv'
csv_filename = 'data/stock_data.csv'
tickerDf.to_csv(csv_filename)

print(f"Data saved to {csv_filename}")