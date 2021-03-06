from turtle import Turtle
import random 

class Food(Turtle):

    def __init__(self): #This primarily handles attributes 
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh() #Adding our own method 

    def refresh(self):
        random_x = random.randint(-280, 280) #returns random integers between these 2 numbers
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)