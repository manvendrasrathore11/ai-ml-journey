import  random

num =  random.randint(1,100)

def dif_easy(num):
    for i in range(10, 0, -1):
        print(f"you have {i} attempts remaining to guess the number")
        user_guess = int(input("Make a guess :"))
        if user_guess > num:
            print("Too high.")
            print("Guess again ")
        elif user_guess < num    :
            print("Too low.")
            print("Guess again ")
        else:
            print(f"You got it !  The answer was {user_guess}")
            break

def dif_hard(num):
    for i in range(5, 0, -1):
        print(f"you have {i} attempts remaining to guess the number")
        user_guess = int(input("Make a guess :"))
        if user_guess > num:
            print("Too high.")
            print("Guess again ")
        elif user_guess < num    :
            print("Too low.")
            print("Guess again ")
        else:
            print(f"You got it !  The answer was {user_guess}")
            break









print("Welcome to the number guessing Game !")
print("I'm thinking of a number between 1 to 100 .")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard' :").lower()

if user_choice == "easy":
    dif_easy(num)
elif  user_choice == "easy":
    dif_hard(num)
else :
    print("chose correct difficulty   level ")


