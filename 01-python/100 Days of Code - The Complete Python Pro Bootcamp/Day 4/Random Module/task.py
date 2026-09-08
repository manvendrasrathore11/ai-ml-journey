# learn about what is random and random pseudo code from khan's academy ,
# complete heads ND Tails

import  random


# from random import choice

# import my_module
#
# ran = random.randint(1,10)
# print(ran)
# print(my_module.my_fav_car)

# ran_0_to_1 = random.random() # 0<=num<1 we can expend the range by just multiply
# print(ran_0_to_1)

# rand = random.uniform(1,10)
# print(rand)

# makin program for heads and tails

print("Toss time ")
choice  = input('what\'s your call "Heads" or "tails"').lower()

ran = random.randint(1,2)

if ran == 1:
    com_choice = "heads"
else:
    com_choice = "tails"


if choice == com_choice:
    print()
