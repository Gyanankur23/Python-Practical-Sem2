import numpy as np
import pandas as pd
data_dict={'a':1,'b':2,'c':3,'d':4}
series_dict=pd.Series(data_dict)
print(data_dict)
print(series_dict)
series_array=pd.Series(np.array([10,20,30,40,50,60]))
print(series_array)