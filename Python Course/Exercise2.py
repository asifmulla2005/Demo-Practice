# Exercise 2 
# time = float(input("Enter the time :",))
# print("The time is ",time)

# if(6.00 < time < 12.00):
#     print("Good Morning")
# elif(12.01 <= time < 17.00):
#     print("Good Afternoon")
# else:
#     print("Good Night")


import time
t = time.strftime('%H:%M:%S') 
hour = int(time.strftime('%H'))
# hour = int(input("Enter hour: "))
print(hour)

if(hour>=0 and hour<12):
  print("Good Morning Sir!")
elif(hour>=12 and hour<17):
  print("Good Afternoon Sir!")
elif(hour>=17 and hour<24):
  print("Good Night Sir!")