from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.level=1
        self.goto(-280,250)
        self.level_count()

    def level_count(self):
        self.clear()
        self.write(f"LEVEL: {self.level}",align="left",font=("Courier",24,"normal"))

    def increase_level(self):
        self.level+=1
        self.level_count()

    def game_over(self):
        self.goto(-60,0)
        self.write("GAME OVER",align="left",font=("Courier",30,"normal"))
