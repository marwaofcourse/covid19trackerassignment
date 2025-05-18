# COVID-19 Global Data Tracker

# Importing Required Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# File Path
file_path = './data/owid-covid-data.csv'

# Loading the Data
try:
    df = pd.read_csv(file_path)
    print("Data loaded successfully.")
except FileNotFoundError:
    print("File not found. Please ensure the data file is in the correct directory.")

# Previewing the Data
print("\nData Preview:")
print(df.head())

# Inspecting Data Structure
print("\nData Columns:")
print(df.columns)

# Checking for Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Data Cleaning
# Filtering for Selected Countries
selected_countries = ['Kenya', 'United States', 'India', 'Brazil', 'United Kingdom']
df = df[df['location'].isin(selected_countries)]

# Converting date to datetime format
df['date'] = pd.to_datetime(df['date'])

# Handling Missing Numeric Values
df.fillna(0, inplace=True)

# Basic EDA - Total Cases Over Time
plt.figure(figsize=(12,6))
sns.lineplot(data=df, x='date', y='total_cases', hue='location')
plt.title('Total COVID-19 Cases Over Time (Selected Countries)')
plt.xlabel('Date')
plt.ylabel('Total Cases')
plt.xticks(rotation=45)
plt.show()

# Saving Cleaned Data for Further Use
df.to_csv('./data/cleaned_covid_data.csv', index=False)
print("\nData cleaned and saved successfully.")
