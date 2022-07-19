# s="shivank is bacvkend developer"
# s.split()
# print(s)




# n=int(input("Enter no"))
# for i in range(n):
#     op=input()
#     op_list=op.split()
#     if op_list[0]=='add':
#         first_number=int(op_list[1])
#         second_number=int(op_list[2])
#         print(first_number+second_number)
#     elif op_list[0]=='mul':
#         first_number=int(op_list[1])
#         second_number=int(op_list[2])
#         print(first_number*second_number)
#     elif op_list[0]=='sub':
#         first_number=int(op_list[1])
#         second_number=int(op_list[2])
#         print(first_number-second_number)
#     elif op_list[0]=='divid':
#         first_number=int(op_list[1])
#         second_number=int(op_list[2])
#         print(first_number/second_number)
    

# n=int(input("Enter no: "))
# sum = 0
# mul=1
# for i in range(n):
#     op=input()
#     op_list=op.split()
        
#     if op_list[0]=='add':
#         for j in range(1,len(op_list)):
#             sum=sum + int(op_list[j])
#         print(sum)
#     elif op_list[0]=='mul':
#          for j in range(1,len(op_list)):
#               mul=mul * int(op_list[j])
#          print(mul)
          
# n=int(input("Enter no"))
# fact=1
# for i in range(1,n+1):
    
#     fact=fact * i

#     print(fact)

# palindrone or not 




# n=int(input())
# print(chr(n))
# m=int(input())
# print(chr(m))
# g=int(input())
# print(chr(g))
# a=int(input())
# print(chr(a))
# b=int(input())
# print(chr(b))
# v=int(input())
# print(chr(v))

# print(chr(n)+chr(m)+chr(g)+chr(a)+chr(b)+chr(v))


# n  = input()
# n = int(n)
# s = ''

# for i in range(n):
#     ascii_number = int(input())
#     char_at_ascii = chr(ascii_number)
#     s += char_at_ascii
#     print(s)
    

ascii_numbers = input()
ascii_numbers_list = ascii_numbers .split()

print(ascii_numbers_list)
s = ''

for i in ascii_numbers_list:
    s += chr(int(i))
    print(s)