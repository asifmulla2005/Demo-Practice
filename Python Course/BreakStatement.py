# Break statement 
i = 0
while True:
    print(i)
    i = i + 1
    if(i == 15):
        break
print("\n")

for i in range(1, 100):
    print(i, end =" ")
    i = i + 1
    if(i == 50):
        print("Stop Here")
        break