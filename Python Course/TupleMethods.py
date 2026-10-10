# Tuple Methods 

# Tuple is a immutable i.e.  if we want to change in tuple then 
# firstly we should convert this tuple into one list 
# then change the list as per requirements 
# and then last convert this list into tuple

country = ("spain", "italy", "india", "england", "germany")
temp = list(country)
temp.append("russia")
temp.pop(3)
country = tuple(temp)
print(country)

# count 
tuple1 = (0, 1, 2, 3, 2, 3, 4, 1, 3, 2)
res = tuple1.count(2)
print(res)

# index
tuple2 = (0, 1, 2, 3, 2, 3, 4, 1, 3, 2)
res = tuple2.index(4)
print(res)