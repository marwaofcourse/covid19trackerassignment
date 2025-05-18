# covid19trackerassignment
# COVID-19 Global Data Tracker

This project aims to build a data analysis and reporting notebook that tracks global COVID-19 trends. It analyzes cases, deaths, recoveries, and vaccinations across countries and time, providing insights through data visualization and narrative explanations.

## 📋 Project Objectives

* Import and clean COVID-19 global data.
* Analyze time trends (cases, deaths, vaccinations).
* Compare metrics across countries/regions.
* Visualize trends with charts and maps.
* Communicate findings in a Jupyter Notebook or PDF report.

## 🗂️ Project Structure

```
📁 COVID-19_Global_Data_Tracker
├── data/
│   └── owid-covid-data.csv
│   └── cleaned_covid_data.csv
├── notebooks/
│   └── COVID-19_Global_Data_Tracker.ipynb
├── outputs/
│   └── visualizations/
├── scripts/
│   └── data_cleaning.py
└── README.md
```

## 🛠️ Requirements

* Python 3.8+
* pandas
* matplotlib
* seaborn
* plotly (optional for advanced visualizations)

Install the required packages with:

```bash
pip install pandas matplotlib seaborn plotly
```

## 🚀 Getting Started

1. Clone this repository.
2. Download the COVID-19 dataset (**owid-covid-data.csv**) and place it in the **data/** directory.
3. Run the Jupyter notebook to generate insights and visualizations.

## 📊 Key Features

* Data loading, cleaning, and preparation.
* Exploratory data analysis (EDA) with line and bar charts.
* Vaccination analysis and optional choropleth maps.

## 📈 Example Output

![Example Chart](./outputs/visualizations/example_chart.png)

## 📚 References

* Our World in Data COVID-19 Dataset
* Johns Hopkins University GitHub Repository
