import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# Load the CSV data into a DataFrame
df = pd.read_csv('data/prophet_forecast.csv')

# Ensure the 'ds' column is a datetime type
df['ds'] = pd.to_datetime(df['ds'])

# Plotting
plt.figure(figsize=(10, 6))

# Plot the 'yhat' as a line
plt.plot(df['ds'], df['yhat'], label='Predicted', color='royalblue')

# Fill between 'yhat_lower' and 'yhat_upper' for the confidence interval
plt.fill_between(df['ds'], df['yhat_lower'], df['yhat_upper'], color='grey', alpha=0.4, label='Confidence Interval')

# Styling the plot
plt.title('Stock predictions', fontsize=20, fontweight='bold', color='navy')
plt.xlabel('Date', fontsize=15, fontweight='bold', color='darkred')
plt.ylabel('Forecast Value', fontsize=15, fontweight='bold', color='darkred')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.tight_layout()

# Format the date on the x-axis
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gcf().autofmt_xdate()  # Improve formatting of the date labels

# Save the plot to a file
plt.savefig('data/forecast_plot.png', dpi=300)  # Save the plot as a PNG file

# Optionally, to display the plot if running the script interactively:
# plt.show()
