# Docstrings in python 
def square(n):
    ''' take a number n, returns the square of n '''
    print(n**2)
square(5)
print(square.__doc__)


def add(num1, num2):
    ''' Addition of two integer numbers '''
    print(add.__doc__)
    print(num1 + num2)
add(7, 3)
