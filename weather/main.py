
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data["day"])
#
# d = data.temp.max()
# print(d)
#
# print(data[data.temp == d])


# list = data["temp"].to_list()
# temp = 0
# for value in list:
#     temp += value
#
# avg = temp/len(list)
# print(round(avg))

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_sqrurirrals = len (data[data["Primary Fur Color"] == "Gray"])
black_sqrurirrals = len (data[data["Primary Fur Color"] == "Black"])
red_sqrurirrals = len (data[data["Primary Fur Color"] == "Cinnamon"])

type = {
    "Fur color": ["Black", "Red", "Gray"],
    "total" : [gray_sqrurirrals, black_sqrurirrals, red_sqrurirrals]

}

dict = (pandas.DataFrame(type))
dict.to_csv("new_file.csv")

