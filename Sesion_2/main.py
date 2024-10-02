import pandas as pd

path = 'Retail.csv'

Retail_data = pd.read_csv(path, encoding='latin1')

print(type(Retail_data))
print(Retail_data)
