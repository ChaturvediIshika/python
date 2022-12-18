from turtle import Turtle,Screen
import random

timmy=Turtle()
timmy.pensize(15)
a=["yellow","gold","orange","red","maroon","violet","magenta","purple","navy","blue","skyblue","cyan","turquoise","lightgreen","green","darkgreen","chocolate","brown","black","gray"]
b=[0,90,180,270]


timmy.speed("fast")
for _ in range(100):
    timmy.color(random.choice(a))
    timmy.forward(50)
    timmy.seth(random.choice(b))






my_screen=Screen()
my_screen.exitonclick()
