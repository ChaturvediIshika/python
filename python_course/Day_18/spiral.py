import turtle as t
import random

tim=t.Turtle()
t.colormode(255)

def random_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

tim.speed("fastest")

def draw(gap):
    for _ in  range(360//gap):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap)

draw(5)


screen=t.Screen()
screen.exitonclick()

