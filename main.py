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

# Assuming 'Month', 'Automobile_Sales', and 'Seasonality_Weight' are the correct column names, modify them accordingly
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Month', y='Automobile_Sales', hue='Season', size='Seasonality_Weight', data=df, palette='viridis', sizes=(50, 500))

# Add labels and title
plt.xlabel('Month')
plt.ylabel('Automobile Sales')
plt.title('Impact of Seasonality on Automobile Sales')

# Add legend
plt.legend(title='Season')

plt.show()



# Save the bubble plot as "Bubble.png"
plt.figure(figsize=(12, 8))
sns.scatterplot(x='Month', y='Automobile_Sales', hue='Season', size='Seasonality_Weight', data=df, palette='viridis', sizes=(50, 500))
plt.xlabel('Month')
plt.ylabel('Automobile Sales')
plt.title('Impact of Seasonality on Automobile Sales')
plt.legend(title='Season')
plt.savefig('Bubble.png')
plt.show()

# Scatter plot for correlation between consumer confidence and automobile sales during recession
recession_data = df[df['Recession'] == 1]
plt.figure(figsize=(10, 6))
plt.scatter(x=recession_data['Consumer_Confidence'], y=recession_data['Automobile_Sales'], alpha=0.7, c='blue', marker='o')
plt.xlabel('Consumer Confidence')
plt.ylabel('Automobile Sales')
plt.title('Consumer Confidence and Automobile Sales during Recessions')
plt.savefig('Consumer_Confidence_vs_Sales.png')
plt.show()



# Create dataframes for recession and non-recession periods
df_recession = df[df['Recession'] == 1]
df_non_recession = df[df['Recession'] == 0]

# Calculate the sum of Advertising_Expenditure for both periods
total_ad_expenditure_recession = df_recession['Advertising_Expenditure'].sum()
total_ad_expenditure_non_recession = df_non_recession['Advertising_Expenditure'].sum()

# Data for the pie chart
labels = ['Recession', 'Non-Recession']
sizes = [total_ad_expenditure_recession, total_ad_expenditure_non_recession]
colors = ['red', 'green']  # You can choose your own colors

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Advertising Expenditure during Recession and Non-Recession Periods')
plt.savefig('Pie_Chart_Ad_Expenditure.png')
plt.show()


# Data for the pie chart
labels = ['Recession', 'Non-Recession']
sizes = [total_ad_expenditure_recession, total_ad_expenditure_non_recession]
colors = ['red', 'green']  # You can choose your own colors

# Create a pie chart
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
plt.title('Advertising Expenditure of XYZAutomotives During Recession and Non-Recession Periods')
plt.savefig('Pie_1.png')
plt.show()

# Filter the data
Rdata = df[df['Recession'] == 1]

# Calculate the advertising expenditure by vehicle type during recessions
VTadexpenditure = Rdata.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()

# Create a pie chart for the share of each vehicle type in total advertisement expenditure during recessions
plt.figure(figsize=(8, 6))

labels = VTadexpenditure.index
sizes = VTadexpenditure.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)

plt.title('Share of Each Vehicle Type in Total Advertisement Expenditure during Recessions')

plt.show()


# Filter the data for recession period
recession_data = df[df['Recession'] == 1]

# Calculate the advertisement expenditure by vehicle type during recessions
vehicle_type_ad_expenditure = recession_data.groupby('Vehicle_Type')['Advertising_Expenditure'].sum()

# Create a pie chart for the total advertisement expenditure by vehicle type
plt.figure(figsize=(8, 6))
labels = vehicle_type_ad_expenditure.index
sizes = vehicle_type_ad_expenditure.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Total Advertisement Expenditure by Vehicle Type During Recessions')
plt.show()


# Calculate the sales volume by vehicle type during recessions
vehicle_type_sales = recession_data.groupby('Vehicle_Type')['Automobile_Sales'].sum()

# Create a pie chart for the share of each vehicle type in total sales during recessions
plt.figure(figsize=(8, 6))
labels = vehicle_type_sales.index
sizes = vehicle_type_sales.values
plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
plt.title('Share of Each Vehicle Type in Total Sales during Recessions')
plt.show()


# Filter out the data for the recession period
data = df[df['Recession'] == 1]

plt.figure(figsize=(10, 6))

# Create a countplot to analyze the effect of the unemployment rate on vehicle type and sales
sns.countplot(data=data, x='unemployment_rate', hue='Vehicle_Type')

plt.xlabel('Unemployment Rate')
plt.ylabel('Count')
plt.title('Effect of Unemployment Rate on Vehicle Type and Sales')
plt.legend(loc='upper right')

# Save the countplot as "count_plot.png"
plt.savefig('count_plot.png')

# Display the plot
plt.show()







import folium

# Assuming you have a column named 'Sales' representing sales data by region
# Replace 'YourDataFrame' and 'Sales' with your actual DataFrame and column names
# For simplicity, let's assume the DataFrame is named 'df'
df_recession = df[df['Recession'] == 1]
region_sales = df_recession.groupby('Region')['Automobile_Sales'].sum().reset_index()

# Find the region with the highest sales during the recession period
highest_sales_region = region_sales.loc[region_sales['Automobile_Sales'].idxmax(), 'Region']

# Create a map centered around the United States
m = folium.Map(location=[37, -95], zoom_start=4)

# Add markers for each region's office location
for index, row in df_recession.iterrows():
    folium.Marker(
        location=[row['Latitude'], row['Longitude']],
        popup=f"Region: {row['Region']}<br>Sales: {row['Automobile_Sales']}",
        icon=folium.Icon(color='blue', icon='info-sign')
    ).add_to(m)

# Highlight the region with the highest sales during the recession period
folium.Marker(
    location=[df_recession[df_recession['Region'] == highest_sales_region]['Latitude'].mean(),
              df_recession[df_recession['Region'] == highest_sales_region]['Longitude'].mean()],
    popup=f'Highest Sales Region: {highest_sales_region}',
    icon=folium.Icon(color='red', icon='info-sign')
).add_to(m)

# Save the map as an HTML file
m.save('highest_sales_region_map.html')






























