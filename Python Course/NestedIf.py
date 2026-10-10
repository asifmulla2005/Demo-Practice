# nested-if statemnet 
num = 18
if(num < 0):
    print("The number is negative")
elif(num > 0):
    if(num <= 10):
        print("Number is between 0 - 10")
    elif(num > 10 and num <= 20):
        print("Number is between 10 - 20")
    else:
        print("Number is greater than 20")
else:
        print("Number is zero")


