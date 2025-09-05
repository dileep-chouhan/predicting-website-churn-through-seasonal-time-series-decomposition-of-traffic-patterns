import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
# --- 1. Synthetic Data Generation ---
# Generate synthetic website traffic data with seasonality and trend
np.random.seed(42)  # for reproducibility
dates = pd.date_range(start='2022-01-01', periods=365)
trend = np.linspace(1000, 1200, 365) # Upward trend in traffic
seasonality = 100 * np.sin(2 * np.pi * np.arange(365) / 365) # Yearly seasonality
noise = np.random.normal(0, 50, 365) # Random noise
traffic = trend + seasonality + noise
# Create DataFrame
df = pd.DataFrame({'Date': dates, 'Traffic': traffic})
df = df.set_index('Date')
# --- 2. Time Series Decomposition ---
# Decompose the time series into trend, seasonality, and residual components
decomposition = seasonal_decompose(df['Traffic'], model='additive', period=30) #period set to 30 for demonstration, adjust as needed for your data
# Extract components
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid
# --- 3. Visualization ---
# Plot the decomposed time series
plt.figure(figsize=(12, 8))
plt.subplot(411)
plt.plot(df['Traffic'], label='Original')
plt.legend(loc='upper left')
plt.subplot(412)
plt.plot(trend, label='Trend')
plt.legend(loc='upper left')
plt.subplot(413)
plt.plot(seasonal, label='Seasonality')
plt.legend(loc='upper left')
plt.subplot(414)
plt.plot(residual, label='Residuals')
plt.legend(loc='upper left')
plt.tight_layout()
output_filename = 'time_series_decomposition.png'
plt.savefig(output_filename)
print(f"Plot saved to {output_filename}")
# --- 4. Analysis (Example: Identify periods of significant decline)---
#  This section needs further development based on specific churn definition and analysis goals.
#  For example, you could identify months with traffic below a certain threshold or calculate rolling averages 
#  to detect significant drops.  This is a placeholder for more advanced analysis.
# Example: Find months with below-average traffic (simple example)
monthly_traffic = df['Traffic'].resample('M').mean()
average_traffic = monthly_traffic.mean()
months_below_average = monthly_traffic[monthly_traffic < average_traffic]
print("\nMonths with below-average traffic:")
print(months_below_average)
#Further analysis would involve correlating these periods with user segment data to identify at-risk groups.