# Predicting Website Churn Through Seasonal Time Series Decomposition of Traffic Patterns

## Overview

This project analyzes website traffic data to identify seasonal trends associated with user churn. By decomposing the time series data into its constituent components (trend, seasonality, and residual), we aim to proactively identify periods of increased churn risk and inform targeted retention strategies.  The analysis utilizes time series decomposition techniques to pinpoint seasonal patterns in website traffic decline, allowing for more effective prediction and intervention.

## Technologies Used

* Python 3
* Pandas
* NumPy
* Statsmodels
* Matplotlib
* Seaborn

## How to Run

1. **Install Dependencies:**  Navigate to the project directory in your terminal and install the required Python libraries using pip:

   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Analysis:** Execute the main script using:

   ```bash
   python main.py
   ```

   Ensure that your data file (specified within `main.py`) is in the same directory.  The script expects a CSV file with at least a 'date' and a 'traffic' column.


## Example Output

The script will print a summary of the time series decomposition analysis to the console, including key statistics related to trend, seasonality, and residuals.  Additionally, the script will generate several visualizations:

* **Seasonal Decomposition Plot:** A plot visualizing the decomposed time series, showing the trend, seasonal, and residual components.  This will be saved as `seasonal_decomposition.png`.
* **Churn Prediction Plot:** A plot showing the predicted churn probability based on the seasonal patterns. This will be saved as `churn_prediction.png`.  (If applicable based on the analysis performed)

These plots provide a visual representation of the identified seasonal patterns and their relationship to potential website churn.  The specific output may vary depending on the input data.