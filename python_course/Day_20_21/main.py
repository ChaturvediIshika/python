from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_on=True
while game_on:
    screen.update()
    time.sleep(0.15)
    snake.move()

    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()>290 or snake.head.ycor()<-290:
        scoreboard.update_high_score()
        snake.reset()

    for seg in snake.segment:
        if seg==snake.head:
            pass
        elif snake.head.distance(seg)<10:
            scoreboard.update_high_score()
            snake.reset()





screen.exitonclick()