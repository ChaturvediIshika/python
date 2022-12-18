from turtle import Turtle
import random

COLORS=["red","blue","green","yellow","orange","purple"]
starting_move_distance=5
move_increment=5

class CarManager:

    def __init__(self):
        self.cars=[]
        self.car_speed=starting_move_distance

    def create_car(self):
        chance=random.randint(1, 10)
        if chance==1:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y=random.randint(-250, 250)
            new_car.goto(300,random_y)
            self.cars.append(new_car)

    def move_car(self):
        for car in self.cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed+=move_increment
