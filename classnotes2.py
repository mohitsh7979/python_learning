
# n=input("Enter Your string")
# m=n.lower()
# map_={}
# for i in m:
#     if i in map_:
#         map_[i]+=1
#     else:
#         map_[i]=1
# print(map_)

# n=input("Enter")
# list=[]
# while True:
#     commands=input()
#     commands_list=commands.split()
#     if commands_list[0]=='stop':
#         break
#     elif commands_list[0]=='push':
#         list.append(commands_list[1])
#         print(list)
#     elif commands_list[0]=='pop':
#         list.append(commands_list[1])
#         print(list)
    

# map_ = {}
# while True:
#     stud_info = input()
#     """
#     stop
#     maths shivank
#     maths aman
#     english aman
#     """
#     stud_info = stud_info.split()
#     """
#     ["stop"]
#     ["maths", "shivank"]
#     ["maths", "aman"]
#     """
#     if stud_info[0] == 'stop':
#         break
#     else:
#         if stud_info[0] in map_:
#             map_[stud_info[0]].add(stud_info[1])
#         else:
#             map_[stud_info[0]] = {stud_info[1]}
#             # map_[stud_info[0]].add(stud_info[1])
    
        
# print(map_)

p=int(0)
q=int(0)
r=int(0)
s=int(0)
psd = input("Enter a password ")
if len(psd) > 0 and len(psd) <= 5:
            
        for j in range(0,len(psd)):
                
            if ord(psd[j]) >= 48 and ord(psd[j]) <= 57:
                p = int(1)  # numbers
            if ord(psd[j]) >= 65 and ord(psd[j]) <= 90:
                q = int(1)  # Capital Alphabets
            if ord(psd[j]) >= 97 and ord(psd[j]) <= 122:
                r = int(1)  # small alphabets
            if ord(psd[j]) >= 33 and ord(psd[j]) <= 47 or ord(psd[j])  == 64 :
                s = int(1)   # special symbols
    
if p == 1 and q == 1 and r == 1 and s == 1:
    print('valid password')
    
else:
    print('Invalid Password')

