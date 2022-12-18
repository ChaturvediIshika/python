# with open("weather_data.csv") as data:
#     d=data.readlines()
#     print(d)

# import csv

# with open("weather_data.csv") as data:
#     d=csv.reader(data)
#     temperature=[]
#     for row in d:
#         if row[1]=="temp":
#             pass
#         else:
#             temperature.append(int(row[1]))
#     print(temperature)

import pandas

data=pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

#data_dict=data.to_dict()
# print(data_dict)

#temp_list=data["temp"].to_list()
# l=len(temp_list)
# s=sum(temp_list)
# print(s/l)

# print(data["temp"].mean())

# m=data["temp"].max()

# monday=data[data.day=="Monday"]
# tc=monday.temp
# tf=(tc*9/5)+32
# print(tf)

# data_dict={
#     "student":["ishika","anuj","mahi"],
#     "scores":[55,65,75]
# }
# data=pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")
g=0
c=0
b=0
for d in data.Primary_Fur_Color:
    if d=="Gray":
        g+=1
    elif d=="Cinnamon":
        c+=1
    elif d=="Black":
        b+=1

data_dict={
    "Fur_Color":["Grey","Cinnamon","Black"],
    "Count":[g,c,b]
}
squirrel=pandas.DataFrame(data_dict)
squirrel.to_csv("new_data.csv")