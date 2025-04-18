import numpy as np
import pandas as pd
df=pd.DataFrame({
    'Name':['Mohit','Sohan','Mohit'],
    'Age':[19,20,19]
})
result=df.drop_duplicates()
print(df)
print(result)