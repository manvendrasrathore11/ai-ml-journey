weight = float(input("enter your  weight : "))
height = float(input("enter your height :"))

bmi = weight / (height ** 2)

if bmi < 18.5:
    print("underwight")
elif bmi < 25:
    print("normal weight ")
elif   bmi>= 25:
    print("overweight")
else:
     print("entered wrong input ")