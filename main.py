import csv
import pandas


FILE = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

with open(file="weather_data.csv") as data_file:
    data = csv.reader(data_file)
    tempreature1 = []

    field = next(data)
    for row in data:
        print(row)

print(tempreature1)
tempreature2 = []
data = pandas.read_csv("weather_data.csv")
tempreature2 = data["temp"].to_list()
print(tempreature2)
total = 0
total = sum(tempreature2)
average = total/len(tempreature2)
print(average)
print(data["temp"].mean())
print(data["temp"].max())
print(data["temp"].min())
print(data)
print(data["temp"].nlargest(2))
print(data.temp)
max_day = data["temp"].max()
monday = data[data.day == "Monday"]
print(data[data.temp == max_day])
print((monday.temp * 9/5)+32)
data = pandas.read_csv(FILE)

gray_count = len(data[data["Primary Fur Color"] == "Gray"])
print(gray_count)
black_count = len(data[data["Primary Fur Color"] == "Black"])
print(black_count)
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(cinnamon_count)

color_list = data["Primary Fur Color"].to_list()
gray = black = cinnamon = 0
for color in color_list:
    if color == "Gray":
        gray += 1
    elif color == "Cinnamon":
        cinnamon += 1
    elif color == "Black":
        black += 1
count = {"colors": ["gray", "black", "cinnamon"], "number of squirrel": [gray, black, cinnamon]}
print(pandas.DataFrame(count))



