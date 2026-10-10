# Range of index 
# syntax = tuple(start : end : jumpIndex)
animals = ("cat", "dog", "bat", "mouse", "pig", "horse", "donkey", "goat", "cow")
print(animals[3:7])
print(animals[-7:-2])
print(animals[4:])
print(animals[-5:])
print(animals[:6])
print(animals[:-3])
print(animals[::2])
print(animals[1:8:3])
print(animals[-8:-2:2])


# Concatenate two tuples 
a = ("apple", "banana", "mango")
b = ("india", "china", "russia")
c = a + b
print(c)