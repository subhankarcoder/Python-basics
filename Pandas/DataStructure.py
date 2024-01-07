import pandas as pd
# There are two main data structures in Pandas. One is DataFrame and one is Series
# Series is a one dimensional dataset with advanced indexing. It is like a table of only one coloumn. Here data can be of any type
data_series = [1,2,3,4,5]
series = pd.Series(data_series)
print(series) # Here the data type and the advanced indexing is being added automatically (Internally)
data_series_custom = {'a':1,'b':2,'c':3} # Custom indexing of Series
print(pd.Series(data_series_custom))
print(series[1]) # Accessing elements with index
print(pd.Series(data_series_custom)['a']) # Accessing custom element

# DataFrame is a powerfull two dimensional representation of dataset. It is like a table consisting of multiple rows and coloumns to perform advanced operations
data_dataFrame = {
    'Name': ['Subhankar','Tirthankar','Dhrubo'],
    'City': ['Kolkata','Bangalore','Chennai'],
    'Salary': [1000000,10000000,1000000]
}
dataFrame = pd.DataFrame(data_dataFrame)
print(dataFrame)
# Advanced Indexing
dataFrame_2 = pd.DataFrame(data_dataFrame,index=['a','b','c'])
print(dataFrame_2)
# Accessing Elements
print(dataFrame_2.loc['a','City']) # Same as below
print(dataFrame_2.iloc[0,1]) # 1st row 2nd coloumn
