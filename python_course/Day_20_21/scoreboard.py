from turtle import Turtle

class ScoreBoard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as h:
            self.high_score=int(h.read())
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.update()
        self.hideturtle()
        self.update_high_score()
        
    def update(self):
        self.clear()
        self.write(f"score : {self.score} High Score={self.high_score}",align="center",font=("Arial",20,"normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()

    def update_high_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("data.txt",mode="w") as t:
                t.write(f"{self.high_score}")
        self.score=0
        self.update()