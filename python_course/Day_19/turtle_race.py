from turtle import Turtle, Screen
import random

screen=Screen()
screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet.", prompt="Which turtle will win the race? Enter your color:")
colors=['red','yellow','blue','black','green','purple','brown']
y_position=[150,100,50,0,-50,-100,-150]
all_turtles=[]
is_race_on=True

for turtle_index in range(7):
    timmy=Turtle(shape="turtle")
    timmy.penup()
    timmy.color(colors[turtle_index])
    timmy.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(timmy)

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            winner=turtle.pencolor()
            if winner==user_bet:
                print(f"You've won!The {winner} turtle is the winner.")
            else:
                print(f"You've lost!The {winner} turtle is the winner.")
        dist=random.randint(1, 10)
        turtle.forward(dist)

screen.exitonclick()