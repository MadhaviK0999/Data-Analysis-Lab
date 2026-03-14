# Creating dataframe for coffee sold data
import pandas as pd
import matplotlib.pyplot as plt

# Since we don't have an external file, we'll create the data right here!
data = {
    'Day': ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
    'Coffee_Sold': [91, 95, 88, 102, 120, 160, 155],
    'Revenue': [350, 380, 352, 408, 480, 640, 620],
    'Temperature_F': [70, 72, 75, 68, 65, 60, 62]
}

# Load the data into a Pandas DataFrame
df =  pd.DataFrame(data)
# Display the DataFrame
print(df)

#print('row count : ', len(df))
#print(df.tail())
#print(df.head())
print('\n -----Data Info-----')
print(df.info())  
print('\n -----Statistical Summary-----') # statistical summary describes the count,mean,max,min,std of the data.
print(df.describe())