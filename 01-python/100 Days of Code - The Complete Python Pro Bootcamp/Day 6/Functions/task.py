# def my_fun():
#     print("hello Man")
#     print("or kesa hai ")
#
# my_fun()
import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(chosen_word)

placeholder = ""
for place in chosen_word:
    placeholder = placeholder + "_"
print(placeholder)
