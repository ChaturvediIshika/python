from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen=Screen()

t=0.1

screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG GAME")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_leftup, "w")
screen.onkey(l_paddle.go_leftdown, "s")

game_on=True
while game_on:
    time.sleep(t)
    screen.update()
    ball.move()

    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
        t*=0.9

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()
        t*=0.9
        
    
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
        t=0.1

    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()
        t=0.1



screen.exitonclick()