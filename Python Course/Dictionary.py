# Dictionaries in python 
info = {"name":"Asif", "age":20, "elligible":True, "DOB":2005}
print(info)


# Accesing dictionary items in python 
info = {"name":"Asif", "age":20, "elligible":True, "DOB":2005}
print(info["name"])
print(info.keys())
print(info.values())
print(info.items())


for key, value in info.items():
    print(f"The values corresponding to th key {key} is {value}")
