# Hw EXam[le : Reading sales data from a CSV file and creating a dataframe
import pandas as pd     
new_data=pd.read_csv('C:\\Users\\buddh\\Data Science\\Rohan Data Science\\Data-Analysis-Lab\\sales_data.csv')
#print(new_data)
#new_data.info()

# Slicing and dicing the data
# generating sales data for sales grater than 10000
#new_data=new_data[new_data['Sales']>10000]
#print(new_data)

# generating sales representative(Brian Moss) data for sales greater than 2000
new_data=new_data[(new_data['Sales Rep']=='Brian Moss') & (new_data['Sales']>2000)]
print(new_data)
