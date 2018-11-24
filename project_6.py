from datetime import datetime

# Current time
def CurrTime():
    return datetime.utcnow()
# Upper literal
def NameToUpperCase(name):
    return str(name).upper()
# Decoration :)
def Decor():
    print("*" * 50)
# User name
def ValidUser(name):
    person = ["IVAN", "DAVID", "ANDY", "KATE", "ANNA", "ALEX"]
    if NameToUpperCase(name) in person:
        print("Hello, " + NameToUpperCase(name) + "!")
        print(CurrTime())
    else:
        print("User not found - access denied!")
# output part of the program
Decor()
ValidUser(input("Input your name: "))
Decor()