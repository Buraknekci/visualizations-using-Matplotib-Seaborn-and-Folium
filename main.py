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


# Assuming you have information about recession periods in the 'Recession' column
# You may need to adjust this condition based on your actual dataset
recession_condition = df['Recession'] == 1

# Assuming 'Vehicle_Type' is the correct column name, modify it accordingly
countplot_data = df.loc[recession_condition, ['Vehicle_Type', 'Unemployment_Rate']]

# Create a countplot
plt.figure(figsize=(12, 8))
sns.countplot(x='Vehicle_Type', hue='Unemployment_Rate', data=countplot_data)

# Add labels and title
plt.xlabel('Vehicle Type')
plt.ylabel('Count')
plt.title('Effect of Unemployment Rate on Vehicle Type and Sales During Recession')

plt.show()