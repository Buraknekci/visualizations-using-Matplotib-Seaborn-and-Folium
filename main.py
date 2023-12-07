import io
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# Load the dataset
URL = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/historical_automobile_sales.csv"
response = requests.get(URL)
text = io.BytesIO(response.content)
df = pd.read_csv(text)

# Assuming 'Year' and 'Automobile_Sales' are the correct column names, modify them accordingly
df_grouped = df.groupby('Year')['Automobile_Sales'].mean()

# Create a line chart
plt.figure(figsize=(10, 6))
df_grouped.plot(kind='line')

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Average Automobile Sales')
plt.title('Automobile Sales from Year to Year')

plt.show()

# Assuming 'Year' and 'Automobile_Sales' are the correct column names, modify them accordingly
df_grouped = df.groupby(['Year', 'Vehicle_Type'])['Automobile_Sales'].mean().unstack()

# Create a line chart for each vehicle type
fig, ax = plt.subplots(figsize=(10, 6))
for vehicle_type in df_grouped.columns:
    df_grouped[vehicle_type].plot(kind='line', ax=ax, label=vehicle_type)

# Add labels and title
ax.set_xlabel('Year')
ax.set_ylabel('Average Automobile Sales')
ax.set_title('Automobile Sales from Year to Year by Vehicle Type')
ax.legend()

plt.show()

# Assuming you have information about recession periods in the 'Recession' column
# You may need to adjust this condition based on your actual dataset
recession_condition = df['Recession'] == 1

# Create a line plot using Seaborn
plt.figure(figsize=(12, 8))
sns.lineplot(x='Year', y='Automobile_Sales', hue='Vehicle_Type', data=df, errorbar=None, style=recession_condition)

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Automobile Sales')
plt.title('Sales Trend per Vehicle Type - Recession vs Non-Recession')

# Add legend
plt.legend(title='Recession', labels=['Non-Recession', 'Recession'])

plt.show()
# Assuming you have information about recession periods in the 'Recession' column
# You may need to adjust this condition based on your actual dataset
recession_condition = df['Recession'] == 1

# Create subplots for recession and non-recession periods
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 10), sharex=True)

# Plot for non-recession period
non_recession_data = df[~recession_condition]
sns.lineplot(x='Year', y='GDP', hue='Vehicle_Type', data=non_recession_data, ax=axes[0], errorbar=None)
axes[0].set_title('GDP Variation - Non-Recession Period')
axes[0].set_ylabel('GDP')

# Plot for recession period
recession_data = df[recession_condition]
sns.lineplot(x='Year', y='GDP', hue='Vehicle_Type', data=recession_data, ax=axes[1], errorbar=None)
axes[1].set_title('GDP Variation - Recession Period')
axes[1].set_xlabel('Year')
axes[1].set_ylabel('GDP')

# Add legend
axes[0].legend(title='Vehicle_Type')
axes[1].legend(title='Vehicle_Type')

plt.tight_layout()
plt.show()

df['Month'] = pd.to_datetime(df['Month'], format='%b').dt.month

df['Season'] = pd.cut(df['Month'], [0, 3, 6, 9, 12], labels=['Winter', 'Spring', 'Summer', 'Fall'])
# Assuming 'Year' and 'Automobile_Sales' are the correct column names, modify them accordingly
df_grouped = df.groupby(['Year', 'Season'], observed=False)['Automobile_Sales'].mean().reset_index()
# Create a bubble plot using Seaborn
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Year', y='Automobile_Sales', hue='Season', size='Automobile_Sales', data=df_grouped, palette='viridis', sizes=(50, 500))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Automobile Sales')
plt.title('Impact of Seasonality on Automobile Sales')

# Add legend
plt.legend(title='Season')

plt.show()

# Assuming you have a column named 'Consumer_Confidence'
plt.figure(figsize=(10, 6))
plt.scatter(x=df.loc[recession_condition, 'Consumer_Confidence'],
            y=df.loc[recession_condition, 'Automobile_Sales'],
            alpha=0.7,  # Adjust transparency
            c='blue',   # Color of points
            marker='o') # Marker style

# Add labels and title
plt.xlabel('Consumer Confidence')
plt.ylabel('Automobile Sales')
plt.title('Correlation Between Consumer Confidence and Sales During Recession')

plt.show()

import matplotlib.pyplot as plt

# Assuming you have a column named 'Advertising_Expenditure' and 'Recession'
advertising_expenditure_recession = df.loc[df['Recession'] == 1, 'Advertising_Expenditure'].sum()
advertising_expenditure_non_recession = df.loc[df['Recession'] == 0, 'Advertising_Expenditure'].sum()

# Data for the pie chart
labels = ['Recession', 'Non-Recession']
sizes = [advertising_expenditure_recession, advertising_expenditure_non_recession]
colors = ['red', 'green']  # You can choose your own colors

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Add title
plt.title('Advertising Expenditure Distribution During Recession vs Non-Recession')

plt.show()


import matplotlib.pyplot as plt

# Assuming you have columns named 'Vehicle_Type', 'Advertising_Expenditure', and 'Recession'
recession_condition = df['Recession'] == 1

# Filter data for recession period
df_recession = df[recession_condition]

# Group by 'Vehicle_Type' and calculate total advertising expenditure for each type
df_grouped = df_recession.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()

# Data for the pie chart
labels = df_grouped.index
sizes = df_grouped.values
colors = plt.cm.viridis.colors  # You can choose your own colors

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)

# Add title
plt.title('Total Advertising Expenditure by Vehicle Type During Recession')

plt.show()
