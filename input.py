print("Enter your Name")
name=input()
print("Enter your class")
cls=input()
print(name,"and",cls)
full_details='{n} and {c}'.format(n=name,c=cls)
print(full_details)