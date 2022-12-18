from turtle import Turtle,Screen

timmy=Turtle()

def forward():
    timmy.forward(10)

def backward():
    timmy.backward(10)

def counter_clockwise():
    timmy.left(10)

def clockwise():
    timmy.right(10)

def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

def cirlce():
    timmy.circle(50,40)

screen=Screen()
screen.listen()
screen.onkey(forward, "W")
screen.onkey(backward, "B")
screen.onkey(counter_clockwise, "A")
screen.onkey(clockwise, "D")
screen.onkey(cirlce, "C")
screen.onkey(clear, "P")
screen.exitonclick()