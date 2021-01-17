from turtle import Turtle 

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write(f"Score = {self.score}", True, align= "center")
        # self.write("Score = 0", False, align= "center")

        self.goto(0, 250)
        self.pencolor("white")
        