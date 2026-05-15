python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
data = pd.read_csv('Water_Consumption_Data_2021_2025.csv')

# Convert the Year column to type int
data['Year'] = data['Year'].astype(int)

# Filter data for a specific region (e.g., Etihad WE)
etihad_data = data[data['Region'] == 'Etihad WE']

# Generate a line plot for water consumption trends
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Water_Consumption_MCM', hue='Region', data=data)
plt.title('Water Consumption Trends by Region (2021-2025)')
plt.xlabel('Year')
plt.ylabel('Water Consumption (MCM)')
plt.legend(title='Region')
plt.grid(True)
plt.show()

# Predict future trends (simple linear regression example)
from sklearn.linear_model import LinearRegression
import numpy as np

# Prepare data for prediction
X = etihad_data[['Year']]
y = etihad_data['Water_Consumption_MCM']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Predict for future years
future_years = pd.DataFrame({'Year': np.arange(2026, 2031)})
predictions = model.predict(future_years)

# Display predictions
future_data = future_years.copy()
future_data['Predicted_Water_Consumption_MCM'] = predictions
print(future_data)
