# Default Arguments 
def name(fname,mname = "farukh",lname = "Mulla"):
    print("Hello ",fname,mname,lname)
name("Asif")

# Keyword Arguments
def name(fname,mname,lname):
    print("Hello ",fname,mname,lname)
name(mname = "Farukh", lname = "Mulla", fname = "Asif")

# Required Arguments
def name(fname,mname,lname):
    print("Hello ",fname,mname,lname)
name("Asif", "Farukh", "Mulla")

# Variable length Arguments
def name(*name):
    print("Hello ",name[0],name[1],name[2])
name("King", "Harry", "Potter")

def name(**name):
    print("Hello ",name["fname"], name["mname"], name["lname"])
name(mname = "Buchhan", lname = "Burnes", fname = "James")