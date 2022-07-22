f=open("1.txt","w")
f.write("hello mohit")
f.close()

file=open('1.txt','r')
data=file.read()
file.close()
print(data)
file.writelines(['This is file',
'This is file'])
file=open('demo.txt','a')
file.write('This is demoo file 2')
file.close()


