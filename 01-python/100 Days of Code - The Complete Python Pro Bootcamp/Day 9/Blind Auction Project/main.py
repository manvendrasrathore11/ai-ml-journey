# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary


from art import logo

print(logo)


def find_highestbider(dict):  # we can also use max function to ding highest bid
    winner = ""
    highest_bid = 0
    for bider in dict:
        bid_amount = dict[bider]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bider
    print(f"The winner is {winner} with a bid of ${highest_bid}")


data = {}
biding_finished = False
while not biding_finished:
    name = input("what is your name?:")
    bid =  input("what is your bid?: $")
    data[name] = int(bid)
    other_bider = input("Are there any other bidders? Type 'yes' or 'no'.").lower()
    if other_bider == "yes":
        print("\n"*30)

    else:
        biding_finished = True
        find_highestbider(data)



