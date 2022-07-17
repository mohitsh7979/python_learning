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