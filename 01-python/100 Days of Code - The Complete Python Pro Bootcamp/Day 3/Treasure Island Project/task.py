
print(r'''


                            _.--.
                        _.-'_:-'||
                    _.-'_.-::::'||
               _.-:'_.-::::::'  ||
             .'`-.-:::::::'     ||
            /.'`;|:::::::'      ||_
           ||   ||::::::'     _.;._'-._
           ||   ||:::::'  _.-!oo @.!-._'-.
           \'.  ||:::::.-!()oo @!()@.-'_.|
            '.'-;|:.-'.&$@.& ()$%-'o.'\U||
              `>'-.!@%()@'@_%-'_.-o _.|'||
               ||-._'-.@.-'_.-' _.-o  |'||
               ||=[ '-._.-\U/.-'    o |'||
               || '-.]=|| |'|      o  |'||
               ||      || |'|        _| ';
               ||      || |'|    _.-'_.-'
               |'-._   || |'|_.-'_.-'
            jgs '-._'-.|| |' `_.-'
                    '-.||_/.-'

''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
choice = input('you\'re at a cross road. where do you want to go? \n       type "left" or "right" . ').lower()

if choice == "left":
    choice2 = input('you\'ve  come to a lake. There is an island in the middle of the lake. \n   Type "wait" to wait for a boat . Type "swim" across .').lower()
    if choice2 == "wait":
        choice3 = input('You arrive at the island unharmed . There is a house with 3 doors.\n   One red , one yellow and one blue. which colour do you choose?').lower()
        if choice3 == "yellow":
            print("You found the treasure ! congratulation you win !")
        elif choice3 == "red":
            print("it's room full of fire .Game over . ")
        elif choice3 == "blue":
            print("you entered a room  of beast . Game over.")
        else :
            print("You entered wrong choice please recorrect you choice .")
    else:
        print("lake is full of crocodiles . Game over ")
elif choice == "right":
    print("you fell in a hole . Game over .")
else:
    print("You entered wrong choice please recorrect you choice .")
