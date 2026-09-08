print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total_af_tip = tip/100 * bill +bill # bill * (1 + tip/100)
each_pay = total_af_tip/people
final = round(each_pay,2)
print(f"Each person should pay: ${final}")
