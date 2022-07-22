# f=open("2.txt","w")
# f.write("Maths Shivank \n English Shivank \n Maths Nootan \n English Computer \n science abhishek")
# f.close()
# f=open("2.txt","r")
# a=f.readines()

# # map_={}
# # def my_list(a):
# #     new_list=0
# #     for i in a:
# #         new_list=int(a)[i]
# #         return new_list
# # print(my_list(a))
    

# def my_file(a):
#     for i in a:
        

#         return map_
# print(my_file(a))

# file=open("3.txt","w")
# file.write("The Cat and the Canary is a 1927 American silent comedy horror film directed by the German Expressionist filmmaker Paul Leni. An adaptation of John Willard's 1922 black-comedy play of the same name, the film stars Laura La Plante as Annabelle West, Forrest Stanley as Charlie Wilder, and Creighton Hale as Paul Jones. The plot revolves around the death of Cyrus West, who is Annabelle, Charlie, and Paul's uncle, and the reading of his will twenty years later. Annabelle inherits her uncle's fortune, but when she and her family spend the night in his haunted mansion they are stalked by a mysterious figure. Meanwhile, a lunatic known as the Cat escapes from an asylum and hides in the mansion.")
# file.close()
# map_={}

# def my_media(file):
#     file=open("3.txt","r")
#     data=file.readlines()
#     for i in data:
#         a=i.split()
#         for j in a:
#             if j in map_:
#                 map_[j]+=1
#             else:
#                 map_[j]=1
            
#     return map_

# print(my_media(map_))

# myfile=open("4.txt",'w')


# for key,value in map_.items():
#     print(key,value)
#     str_ = f'{key} {value} \n'
#     myfile.write(str_)


# myfile.close()

file=open("5.txt","w")
file.write("2\n4\n6\n8\n10\n12\n14\n16\n18\n20")
file=open("5.txt","r")
a=file.readline()
b=a.split()
true=0
def my_table(file):

  for i in b:
    if b%2==0:
        true=1
    else:
        true=0
        return true

if true==1:
    print("True")
else:
    print("False")

my_table(file)
    

        


