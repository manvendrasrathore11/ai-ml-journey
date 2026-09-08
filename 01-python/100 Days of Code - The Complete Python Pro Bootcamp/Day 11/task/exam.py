# print("enter two numbers  ")
# n1 =  int(input("enter  first number "))
# n2 =  int(input("enter  second  number "))
#
# i = 2
# res = 1
#
# while 1:
#     if( n1 % i==0 or n2%i == 0 ):
#         res = res *i
#         if n1 % i ==0:
#             n1 = n1 /i
#         if n2 % i ==0:
#             n2 = n2/i
#
#     else:
#         i =i+1
#         if n1 == 1 and n2 == 1 :
#             break
# print("lcm =",res)
#
#
# numbers = input("enter number : ")
# number_list = numbers.split(",")
# number_tuple = tuple(number_list)
# print(number_list)
# print(number_tuple)
#
# import  math
# x1 = int(input("enter x1 "))
# x2 = int(input("enter x2 "))
# y1 = int(input("enter y1"))
# y2 = int(input("enter y2 "))
#
# distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
# print(distance)
#
# i = 3
# sum = 2
# while i <= 2000000:
#     f = 1
#     j = 2
#     for j in range(2,int(i**0.5)+1):
#         if i %j == 0 :
#             f =  0
#             break
#         j = j+1
# if f ==1:
#     sum = sum +i
# i = i+1
# print(sum)


#
# a = int(input("x1 : "))
# b = int(input("x1 : "))
# c = int(input("x1 : "))
#
# d = max(a,b,c)
#
# print(d)


# def count_char(input_string):
#     char_count = {}
#     for char in input_string:
#         if char  in char_count:
#             char_count[char] +=1
#
#         else :
#             char_count[char]  =  1
#
#     return char_count
#
# user = input("enter ")
# result = count_char(user)
# print(result)

birthdays = {
    "rahul" : "23-03-06",
    "daksh"  : "21-06-07",
 }

# def find_birthday(name):
#     if name in birthdays:
#         birthday = birthdays[name]
#         day,month,year = birthday.split("-")
#         formated_birth = "/".join([day,month,year])
#         return f"{name}'s bithday is  on {formated_birth}"
#     else:
#         return f"{name}'s bithday is  not found "
# name = input("enter")
# print(find_birthday(name))