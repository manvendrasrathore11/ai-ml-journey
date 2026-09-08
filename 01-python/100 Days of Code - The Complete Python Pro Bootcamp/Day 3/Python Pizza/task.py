name = input("enter your Good name : ")

print(f"Welcome {name} to Python Pizza Deliveries!")
size = input(f"{name} What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
prize = 0
if size == 'S':
    prize = 15
    if pepperoni == 'y':
        prize+=2
    if extra_cheese == 'y':
        prize+=1
elif size == 'M':
    prize = 15
    if pepperoni == 'y':
        prize+=3
    if extra_cheese == 'y':
        prize+=1
elif size == 'L':
    prize = 15
    if pepperoni == 'y':
        prize+=3
    if extra_cheese == 'y':
        prize+=1
else :
    print("cheak your detail and rewrite once again ")


print(f"Thank you {name} for chosing us \nmeet you soon")
print(f"your total bill is ${prize}")
