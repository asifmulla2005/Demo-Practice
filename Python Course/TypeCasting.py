# Type casting 
string = "15"
number = 7
string_number = int(string)
sum = number + string_number
print("The sum of both the numbers is :",sum)

# Example of implicit typecasting 
# Python automatically converts
# a to float
a = 7
print(type(a))
 
# Python automatically converts b to float
b = 3.0
print(type(b))
 
# Python automatically converts c to float as it is a float addition
c = a + b
print(c)
print(type(c))