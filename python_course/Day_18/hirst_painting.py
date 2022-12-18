# import colorgram

# rgb_color=[]
# colors = colorgram.extract('hrist.jpg', 30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_color.append(new_color)

# print(rgb_color)
import turtle as t
import random

timmy=t.Turtle()
t.colormode(255)

color_list=[(221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162), (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157), (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221), (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210), (65, 66, 56)]

timmy.penup()
timmy.setheading(225)
timmy.forward(250)
timmy.setheading(0)
timmy.pendown()
for i in range(10):
    for _ in range(10):
        timmy.dot(20,random.choice(color_list))
        timmy.penup()
        timmy.forward(50)
        timmy.pendown()
    timmy.penup()
    timmy.setheading(90)
    timmy.forward(50)
    if i%2==0:
        timmy.setheading(180)
    else:
        timmy.setheading(360)
    timmy.forward(50)
    timmy.pendown()


screen=t.Screen()
screen.exitonclick()