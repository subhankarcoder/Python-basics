import pandas as pd
data = {
    'Name': ['Subhankar','Tirthankar','Dhrubo'],
    'City': ['Kolkata','Bangalore','Chennai'],
    'Salary': [1000000,10000000,1000000]
}
dataFrame = pd.DataFrame(data)
print(dataFrame)