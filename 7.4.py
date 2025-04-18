import numpy as np
arr=np.array([1,2,4,6,8,9])
max_value=np.max(arr)
filter_arr=arr[arr==max_value]
print(arr)
print(max_value)
print(filter_arr)

