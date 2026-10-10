# in-Built set methods in python 
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "India", "Kabul", "Russia"}
cities3 = {"Tokyo", "Madrid"}
print(cities.isdisjoint(cities2))
print(cities.issuperset(cities2))
print(cities.issuperset(cities3))
print(cities3.issubset(cities))
cities.add("Pakistan")
print(cities)
cities.update(cities2)
print(cities)
cities.remove("Tokyo")
print(cities)
print(cities.pop())
cities.clear()
print(cities)

info = {"Asif", 20, True, 8.95}
if "Asif" in info:
    print("Asif is present")
else:
    print("Asif is absent")
