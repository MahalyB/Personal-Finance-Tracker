# Personal Finance Tracker
A Python application that imports transaction data from CSV files, automatically categorizes expenses using keyword-based rules, and generates summaries and visualizations of spending by category.

## Features

- Import transaction data from CSV files
- Automatically categorize transactions using keyword-based rules
- Identify uncategorized transactions
- Aggregate spending by expense category
- Generate category-level spending summaries
- Visualize spending using Matplotlib

## Technologies

- Python
- Pandas
- Matplotlib

## How It Works

The application  reads transaction data from a CSV file using Pandas. Each transaction is assigned to a spending category based on keywords found in the transaction description.

The categorized data is then aggregated to calculate spending by category and displayed through visualizations.

## Getting Started

Install the required dependencies:

'''bash
pip install pandas matplotlib
'''

## Project Purpose

I built this project to practice using Python and Pandas for data processing while exploring how transaction data can be automtically categorized and analyzed.

## Future Improvements

- Add and edit transactions directly in the application
- Improve transaction categorization
- Add persistent data storage
- Add additional spending reports and visualizations