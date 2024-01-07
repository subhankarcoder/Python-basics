import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Month': ['January','February','March','April','May','June'],
    'Salary': [10000,20000,50000,40000,10000,60000],
    'Expenses': [5000,3000,2000,15000,5000,25000]
}
df = pd.DataFrame(data)
fig,ax = plt.subplots()
# Line chart for Salary
ax.plot(df['Month'], df['Salary'], marker='o', label='Salary', linestyle='-', color='b')

# Line chart for Expenses
ax.plot(df['Month'], df['Expenses'], marker='o', label='Expenses', linestyle='--', color='r')

# Adding labels and title
ax.set_title('Monthly Sales and Expenses')
ax.set_xlabel('Month')
ax.set_ylabel('Amount')
ax.legend()
plt.show()