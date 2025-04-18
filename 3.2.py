tuple1=(1,2,3,4)
print(3 in tuple1)
tuple1=tuple(x if x!=3 else 10 for x in tuple1 )
print(tuple1)