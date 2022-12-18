from turtle import Screen
import time
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen=Screen()
screen.tracer(0)
screen.setup(600,600)

player=Player()
car_manager=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_on=True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    for car in car_manager.cars:
        if car.distance(player)<20:
            game_on=False
            scoreboard.game_over()

    if player.finish():
        player.start_again()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()
