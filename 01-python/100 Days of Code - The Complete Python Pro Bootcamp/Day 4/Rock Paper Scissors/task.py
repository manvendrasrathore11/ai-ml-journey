
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("WELCOME TO ROCK - PAPER - SCISSORS GAME")

choice = int(input('''Lets go ! chose any one

1 for rock 
    _______
---'   ____)
      (_____)       
      (_____)   
      (____)
---.__(___)  

2 for paper
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

3 for scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
chose any one :'''))

com_choise = random.randint(1,3)

r_p_s = [0,rock,paper,scissors ]

print(f"your chose : {choice}")
print(r_p_s[choice])
print(f"opponent chose : {com_choise}")
print(r_p_s[com_choise])
if com_choise == choice:
    print("IT's A DRAW ")
elif choice == 1:
    if com_choise == 2:
        print("you lose ")
    else :
        print("congratulation you win ")

elif choice == 2:
    if com_choise == 1:
        print("congratulation you win  ")
    else :
        print("you lose")

elif choice == 3:
    if com_choise == 1:
        print("you lose  ")
    else :
        print("congratulation you win ")

else:
    print("recheak you chose wrong symbol")

