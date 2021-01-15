from turtle import Turtle, Screen 



STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POS:
            python = Turtle()
            python.color("white")
            python.shape("square")
            python.pencolor("white")
            python.penup()
            python.speed(6)
            python.goto(position)
            
            self.segments.append(python)



    def move(self):
        for boxes in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[boxes - 1].xcor()
            new_y = self.segments[boxes - 1].ycor()
            self.segments[boxes].goto(new_x, new_y)
            
        self.segments[0].forward(MOVE_DISTANCE)



