from turtle import Turtle 

class Scoreboard(Turtle): #Inheriting from Turtle
    def __init__(self): #Attributes go here and method calls
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", True, align= "center", font= ("Arial", 24, "normal"))
        # self.write("Score = 0", False, align= "center")
        
        #Did all this by myself
        