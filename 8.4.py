import numpy as np
import pandas as pd
a=pd.Series([10,20,30,40])
b=pd.Series([5,10,15,20])
print(a)
print(b)
c=pd.concat([a,b])
print(c)