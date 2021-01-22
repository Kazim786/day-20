from turtle import Turtle 

class Scoreboard(Turtle): #Inheriting from Turtle
    def __init__(self): #Attributes go here and method calls
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", True, align= "center", font= ("Arial", 24, "normal"))
        # self.write("Score = 0", False, align= "center")
        self.increased_score()
        self.gameover()
        self.tailcollision()
        
        #Did all this by myself
        
    def gameover(self):
        self.goto(0,0)
        self.clear()
        self.write("Game over", align= "center", font= ("Arial", 24, "normal"))

    def increased_score(self):
        self.goto(0, 250)
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", True, font= ("Arial", 24, "normal")) #This is working too
    
    def tailcollision(self):
        print("Game over") 
        self.score = 0
        self.clear() #Did by myself
        self.goto(0, 250)
        self.penup()
        self.write("GAME OVER", True, font= ("Arial", 24, "normal")) #This is working too
       