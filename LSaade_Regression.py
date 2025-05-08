# Import packages
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Data import and cleanup
weatherdata = pd.read_csv(r"C:\Users\Lina\OneDrive\Documents\AIT 580\regressionweatherdata.csv")
weatherdata['Date'] = pd.to_datetime(weatherdata['Date'], format = '%Y%m', errors = 'coerce')
weatherdata['Year'] = pd.DatetimeIndex(weatherdata['Date']).year

# Display a few records
print(weatherdata.head(5))

# Fit a linear regression line
x = weatherdata['Year']
y = weatherdata['Anomaly']
slope, intercept = np.polyfit(x, y, 1)
regression_eq = f"y = {slope}x + {intercept}"

# Create plot and labels
plt.figure(figsize=(10, 6))
sns.scatterplot(data = weatherdata, x = 'Year', y = 'Anomaly')
sns.regplot(data= weatherdata, x = 'Year', y = 'Anomaly', scatter = False, color = 'red', label = 'Regression Line')
plt.text(x.min(), y.max(), regression_eq, fontsize = 12, color = 'red', ha = 'left', va = 'top')
plt.title('Relationship Between Date and Anomaly')
plt.xlabel('Year')
plt.ylabel('Anomaly')
plt.tight_layout()
plt.show()