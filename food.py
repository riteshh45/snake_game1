import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.speed("fastest")
        self.shapesize(0.5,0.5)
        self.refresh()

    def refresh(self):
        x_cor=random.randint(-280,280)
        y_cor=random.randint(-280,280)
        self.goto(x_cor,y_cor)


