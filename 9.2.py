import numpy as np
import pandas as pd
df=pd.DataFrame({
    'Name':['Mohit','Sohan'],
    'Age':[19,20]
})
df2=pd.DataFrame({
    'Name':['Rohan','Ram'],
    'Age':[17,18]
})
print(df)
print(df2)
result=pd.concat([df,df2])
print(result)
