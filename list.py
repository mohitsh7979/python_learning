items=[1,2,3,4,5]

# print(items[1:5:2])   [start:end:jump]

# item=["mohit",1,2,3]
# print(item)
# items[1]="me"
# print(items)

# print(items[2])
# items.append(item);
# print(items)
# print(items[5][2])
# items[5][2]="yes"
# print(items)

# #tuple
# tupl1 = (1,2,3)
# print(tupl1)
# print(tupl1[2])
# # tupl1[2]="mohit"      show error because in tuple we can not modifiy 
# # print(tupl1)

# dictionary
# dict1={1,2,3}
# print(dict1)
# dict1[2]="mohit"  show error 
# # print(dict1)
# dict1={}
# dict1["virat"]=100
# print(dict1)
# dict1["sachin"]=200
# print(dict1)
# print(dict1.get("virat"))
# print(dict1.keys())
# print(dict1.pop("virat"))

# # set
# ls=[1,2,3,4,3,2,1,6,5,6]
# a=set(ls)
# print(a)

# ls="mohit"
# a=list(ls)
# print(a)
# a[2]="no"
# print(a)

# a=tuple(ls)
# print(a)


st=set([1,2,3,4,5])
bt=set([3,4,5,6])
# st.union(bt)
# print(st)
x=st.intersection(bt)
print(x)


map_={

    'first_name':'mohit',
    'last_name':'sharma',
    'company':'regex'
}
#print(map_['first_name'])
print(map_.get('first_name'))
print(map_.get('last_name'))
print(map_.get('company'))
print(map_.keys())
map_.update({'clg':'jecrc'})
print(map_)
print(map_.copy())






