import pandas as pd
import matplotlib.pyplot as plt

# Create a personal finance tracker with the following features: add transactions, categorize spending, generate reports, store data locally
df_transactions = pd.read_csv('SampleExpenses.csv')
print(df_transactions.head())

# Categories
categories_dict = {
    "Food": ["grocery", "HEB", "Walmart"],
    "Utilities": ["bill"],
    "Food & Drink": ["coffee"]
}

# Function that takes in descriptons and returns the category
def categorize(description):
    for key, value in categories_dict.items():
        for keyword in value:
            if keyword in description:
                return key
    else:
        return "Uncategorized"

# How to apply categorize() to entire Description coloumn
category = []
for descriptions in df_transactions['Description']:
    category.append(categorize(descriptions))
            
df_transactions['Category'] = category

report = df_transactions.groupby('Category')['Amount'].sum()
report = report.reset_index()
report = report.rename(columns={'Amount': 'Total Expenses'})
report.drop(report.index[2], inplace=True)
report['Total Expenses'] = report['Total Expenses'].abs()

# Create pie chart, set the categorical column as index and plot
report.set_index('Category').plot.pie(y='Total Expenses', autopct='%1.1f%%', legend=False)

# clean up layout and display
plt.ylabel('')
plt.title('Personal Finance Expenses Report')
plt.show()