import pandas as pd
import numpy as np

data = np.array([[1,2,3],[4,5,6],[7,8,9]])
dt_from_array = pd.DataFrame(data, columns=['A', 'B', 'C'])
print(dt_from_array)

print()

data2 = [[1, 'Dario', 29], [2, 'Daniela', 25]]
df_from_list = pd.DataFrame(data2, columns=['ID', 'NOMBRE', 'EDAD'])
print(df_from_list)

print()

data3 = [{
         'ID': 1,
         'NOMBRE': 'DARIO',
         'EDAD': 29},
         {
         'ID': 2,
         'NOMBRE': 'DANIELA',
         'EDAD': 25}            
         ]

dt_from_dict_list = pd.DataFrame(data3)
print(dt_from_dict_list)

print()

data4 = {
    'ID': [1,2,3],
    'NOMBRE': ['Dario', 'Daniela', 'Copo'],
    'EDAD': [29, 25, 9]
}

df_from_dict = pd.DataFrame(data4)
print(df_from_dict)

print()

data5 = {
   'ID': pd.Series([1,2,3]),
   'NOMBRE': pd.Series(['Dario', 'Daniela', 'Copo']),
   'EDAD': pd.Series([29, 25, 9]) 
}

df_from_series_dict = pd.DataFrame(data5)
print(df_from_series_dict)
