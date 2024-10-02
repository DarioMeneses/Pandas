import pandas as pd

path = 'ClassicMetal.csv'

Retail_data = pd.read_csv(path, encoding='latin1')

print(type(Retail_data))
print(Retail_data)
