import numpy as np
import pandas as pd
df=pd.DataFrame({
    'Name':['Rohan','Mohan'],
    'Percentage obtained':[80,95]    
})
result=df[df['Percentage obtained']>90]

print(df)
print(result)