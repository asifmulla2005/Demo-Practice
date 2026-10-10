# Continue Statement 
for i in range(12):
    print(i)
    if(i == 10):
        print("Skip the iteration")
        continue
    print("5 x ",i ,"=",5*i)

print("\n")
for i in [2, 3, 4, 6, 8, 9, 0]:
    if(i%2 != 0):
        continue
    print(i)