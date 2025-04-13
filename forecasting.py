# models/forecasting.py

from prophet import Prophet
import pandas as pd

# Load the solar energy data
df = pd.read_csv('data/processed/solarenergy.csv', dtype={'wind-direction': 'str'})

# Rename necessary columns for Prophet
df.rename(columns={'Datetime': 'ds', 'solar_mw': 'y'}, inplace=True)

# Convert 'ds' to datetime
df['ds'] = pd.to_datetime(df['ds'], format='%d/%m/%Y %H:%M')

# Initialize and fit the model
model = Prophet()
model.fit(df)

# ✅ FIX: Do NOT pass df here — only specify periods and freq
future = model.make_future_dataframe(periods=60, freq='M')

# Predict future values
forecast = model.predict(future)

# Save forecast
forecast[['ds', 'yhat']].to_csv('data/processed/solarenergy_forecast.csv', index=False)
