from turtle import Turtle

STARTING_POSITION=(0,-280)
MOVE_DISTANCE=10
FINISH_LINE=280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.start_again()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def start_again(self):
        self.goto(STARTING_POSITION)

    def finish(self):
        if self.ycor()>FINISH_LINE:
            return True
        else:
            return False
