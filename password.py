from ast import Str


password=input("Enter your password")
if(password==Str("A-Z")):
    if(password==int(1-9)):
        if(password==chr('a-z')):
            print("Correct Password")
        else:
            print("please enter correct password")
    else:
        print("please enter correct password")
else:
    print("Please enter correct password")