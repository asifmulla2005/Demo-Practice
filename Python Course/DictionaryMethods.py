# Dictionary Methods 
info = {"name":"Asif", "age":19, "elligible":True}
print(info)
info.update({"age":20})
info.update({"DOB":2005})
print(info)

info.pop("elligible")
print(info)

info.popitem()
print(info)

info.clear()
print(info)
