# print("Enetr No")
# var=int(input())
# if(var>4):
#     print(var,"is grater then 4 ")
# elif(var==2):
#     print(var,"is equal 2")
# else:
#     print(var,"is less then 4")

# print("Enter your age")
# age=int(input())
# if(age>18):
#     print("You are elegible to vote")
# else:
#     print("you are not elegible to vote")

# a=int(input("Enter first no"))
# b=int(input("Enter second no"))
# c=int(input("Enter third no"))
# if(a>b):
#     if(a>c):
#         print(a)
#     else:
#         print(c)
# else:
#     if(b>c):
#         print(b)
#     else:
#         print(c)

# a=str(input("Enter your string :"))
# for i in a:
#     if ord(i)%2==0:
#         print(i,"even")

# n=int(input("Enter no"))
# lst=[]
# for i in range(0,n):
#     a=input()
#     lst.append(a)

# print(lst)

from math import dist
from optparse import Values


# n=int(input("Enter no"))
# list1=[]
# list2=[]
# for i in range(0,n*2):
#     if(n==1):
#         data_type=input()
#     elif(n==2):
#         value=input()
#     elif(n==3):
#         data_type=input()
#     elif(n==4):
#         value=input()

#     list1[data_type] 
#     list2[value]
    
no_of_elm=int(input())
map_={
    'str':[],
    'int':[],
    'float':[]
}

for i in range(no_of_elm):
    dt=input('Enter Datatype:')
    value=input('Enter value for above datatype:')
    if dt=='str':
        map_['str'].append(value)
    elif dt=='int':
        map_['int'].append(int(value))
    elif dt=='float':
        map_['float'].append(float(value))
    else:
        print("please intailise a empty list for {dt}".format(dt))

print(map_)









        

 