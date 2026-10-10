# Tuple in Python 
tuple = (1, 2, 2, 3, 5, 4, 6)
tuple2 = ("red", "green", "blue")
print(tuple)
print(tuple2)

details = ("Asif", 20, "AIDS", 8.95)
print(details)


# Tuple indexing 

country = ("spain", "italy", "india", "england", "gemany")
print(country[0])
print(country[1])
print(country[2])
print(country[-1])
print(country[-2])
print(country[-4])


# Check for item 

country = ("spain", "italy", "india", "england", "gemany")
if "spain" in country:
    print("spain is present")
else:
    print("spain is absent")

if "russia" in country:
    print("russia is present")
else:
    print("russia is absent")
