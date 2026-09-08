#
# # import another
# #
# # print(another.another)
#
# from  turtle import  Turtle , Screen
#
# # timmy = turtle.Turtle()      # timmy in object and Turtle in class or blue print
# timmy =  Turtle()
# timmy.shape("turtle")
# timmy.color("blue")
#
# timmy.forward(100)
# timmy.left(120)
# timmy.forward(100)
# timmy.home()
# timmy.forward(200)
# print(timmy)
#
# my_screen = Screen()
#
# print(my_screen.canvheight)  # my_screen is object and canvheight is attributes
# my_screen.exitonclick()       # my_screen is object and exitonclick is method (function)


from prettytable import  PrettyTable

table = PrettyTable()


# table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# table.add_row(["Adelaide", 1295, 1158259, 600.5])
# table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# table.add_row(["Darwin", 112, 120900, 1714.7])
# table.add_row(["Hobart", 1357, 205556, 619.5])
# table.add_row(["Sydney", 2058, 4336374, 1214.8])
# table.add_row(["Melbourne", 1566, 3806092, 646.9])
# table.add_row(["Perth", 5386, 1554769, 869.4])

table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
table.add_rows(
    [
        ["Adelaide", 1295, 1158259, 600.5],
        ["Brisbane", 5905, 1857594, 1146.4],
        ["Darwin", 112, 120900, 1714.7],
        ["Hobart", 1357, 205556, 619.5],
        ["Sydney", 2058, 4336374, 1214.8],
        ["Melbourne", 1566, 3806092, 646.9],
        ["Perth", 5386, 1554769, 869.4],
    ]
)



print(table)

