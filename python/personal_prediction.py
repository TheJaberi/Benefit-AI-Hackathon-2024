# -*- coding: utf-8 -*-
"""stocks_prophet.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1P65RkRODR-OmIMSkUX4SnFEe4HzmVeyr
"""

# pip install prophet pandas plotly kaleido

from prophet import Prophet
import datetime as dt
import plotly.offline as py_offline
import pandas as pd

data = pd.read_csv("data/anz_data.csv")

data = data[['date', 'balance']]

"""above we selected the date and close column from the csv file"""

# data

"""we print the data above"""

# Iterate over the 'Date' column and extract just the date part from each string
# data['Date'] = [date.split(' ')[0] for date in data['Date']]

# Renaming the columns to 'ds' and 'y' for compatibility with Prophet
data.columns = ['ds', 'y']
# data

"""rename the columns and display change"""

prophet = Prophet(daily_seasonality=True)
prophet.fit(data)

"""made the model take the dataset and fit it"""

future_dates = prophet.make_future_dataframe(periods=30)
predictions = prophet.predict(future_dates)

"""make the predictions with how many days to look ahead"""

from prophet.plot import plot_plotly
fig = plot_plotly(prophet, predictions)
# If you want to display the plot in the browser
# py_offline.plot(fig)


import plotly.io as pio
# Assuming 'fig' is your Plotly figure object
pio.write_image(fig, 'figure.png')


# Access the forecasted values
forecasted_values = predictions[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]

# If you want to save these predictions to a CSV file
forecasted_values.to_csv('data/personal_prediction.csv', index=False)

# To access specific prediction for a specific date
# specific_date = '2025-02-01'
# specific_prediction = predictions[predictions['ds'] == specific_date]

# Print or use the specific prediction
# print(specific_prediction[['ds', 'yhat', 'yhat_lower', 'yhat_upper']])



