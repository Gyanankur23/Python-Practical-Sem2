tuple_of_lists = ((1, 2), (3, 4), (5, 6), (7, 8))
flatten = tuple(item for sublist in tuple_of_lists for item in sublist)
print(flatten)