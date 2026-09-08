# with  open("weather_data.csv.csv") as file :
#     x = file.readlines()
# print(x)

# import csv
#
# with open("weather_data.csv.csv") as  data_file:
#     data =  csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         temp = row[1]
#         if row[1] != "temp":
#             temperatures.append(int(temp))
# print(temperatures)

import pandas
#
# data = pandas.read_csv("weather_data.csv.csv")
# print(data)
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].tolist()

# average_of_temp =  sum(temp_list) /len(temp_list)
# print("avg:" , average_of_temp)
# avg = data["temp"].mean()
# print(avg)
# max_in_temp = data["temp"].max()
# print(max_in_temp)

# print(data["condition"])
# print(data.condition)  # Both work same its  depend on yo which want you chose

# print(data[data.day == "Monday"])

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# monday_temp = monday.temp[0]
# monday_temp_f = monday_temp * 9/5 +32
# print(monday_temp_f)

#create a dataframe from scratch

# data_dict = {
#     "student" : ["amy" ,  "james",  "angela"],
#     "scores" : [76,78,76]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

import pandas

data = pandas.read_csv("2018_Central_Squirrel_Data.csv.csv")
grey_squirrels_count =  len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count =  len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count =  len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur color" : ["Gray" ,"Cinnamon","Black"],
    "Count" : [grey_squirrels_count,red_squirrels_count,black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")