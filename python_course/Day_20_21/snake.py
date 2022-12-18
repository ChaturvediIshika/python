from turtle import Turtle,Screen

POSITIONS=[(0,0),(-20,0),(-40,0)]

class Snake:

    def __init__(self):
        self.segment=[]
        self.create_snake()
        self.head=self.segment[0]

    def create_snake(self):
        for pos in POSITIONS:
            self.add_body(pos)
            

    def add_body(self, pos):
        s=Turtle("circle")
        s.color("white")
        s.penup()
        s.goto(pos)
        self.segment.append(s)

    def extend(self):
        self.add_body(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment)-1,0,-1):
            x=self.segment[i-1].xcor()
            y=self.segment[i-1].ycor()
            self.segment[i].goto(x,y)
        self.head.forward(20)

    def reset(self):
        for s in self.segment:
            s.goto(1000,1000)
        self.segment.clear()
        self.create_snake()
        self.head=self.segment[0]

    def up(self):
        if self.head.heading() !=270: 
            self.head.setheading(90)

    def down(self):
        if self.head.heading() !=90: 
            self.head.setheading(270)

    def right(self):
        if self.head.heading() !=180: 
            self.head.setheading(0)

    def left(self):
        if self.head.heading() !=0: 
            self.head.setheading(180)