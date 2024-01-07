import pandas as pd
import os

# Reading data from an Excel file into a DataFrame
# df_excel = pd.read_excel('sheet_example.xlsx', sheet_name='sheet_ex')

# Displaying the DataFrame
# print(df_excel.head())
# file_path = 'sheet_example.xlsx'
print("Current working directory:", os.getcwd())
script_path = os.path.abspath(__file__)
folder_path = os.path.dirname(script_path)
file_path = os.path.join(folder_path, 'sheet_example.xlsx')

df_excel = pd.read_excel(file_path)
print(df_excel.head()) # Returning the file content
print(df_excel.info()) # Returning the file info