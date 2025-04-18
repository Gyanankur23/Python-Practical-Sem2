import numpy as np
import pandas as pd
df=pd.DataFrame({
    'Name':['Mohit','Sohan'],
    'Age':[19,20]
})
result=df[df['Age']==19]
print(df)
print(result)