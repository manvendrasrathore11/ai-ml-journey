#
#
# try:
#     file = open("a_file.txt")
#     a_dict = {"key" : "value"}
#     print(a_dict["key"])
# except FileNotFoundError:
#     file = open("a_file.txt" , "w")
#     file.write("manvendra")
# except KeyError as error_message:
#     print(f"the key {error_message} does not exist:")
#
# else:
#     content = file.read()
#     print(content)
#
# finally :
#     print("closing file")
#     file.close()


#     raise
# one mmore keyword for this work is raise
#  its used to raise are on error
# error which are not give my interpreter
#  example if we take an  hight input from user
# and user write an unexpected and not possible
# output that time we can use raise keyword to generate are erroer
#
# height = float(input("Hight : "))
# weight = int(input("weight : "))
#
# if height > 3 :
#     raise ValueError("human height should not be over 3 meters")
#
# bmi = weight/height ** 2
# print(bmi)
fruits = ["Apple", "Pear", "Orange"]
fruit = fruits[4]
