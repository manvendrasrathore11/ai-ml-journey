print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill =  0
if height >= 120:
    print("you can ride the rollercoaster")
    age = int(input("enter your age ?"))
    if age <= 12:
        bill = 5
        print("please pay 5$.")
    elif age <=18:
        bill = 7
        print("please pay 7$")
    elif age >=45 and age<=55:
        print("everthing is going to be ok ! have free ride on  us ")
    else:
        bill = 12
        print("please pay  12$")
    photo = input("if you want photo with ride  write y for  yes and n for no  ")

    if photo =='y':
       bill+=3
    print(f"your total bill is {bill}")

else:
    print("sorry you have to grow taller before you can ride .")
