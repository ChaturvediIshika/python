from turtle import Turtle,Screen

timmy=Turtle()
screen=Screen()

def move():
    timmy.forward(10)


screen.listen()
screen.onkey(move,"space")
screen.exitonclick()