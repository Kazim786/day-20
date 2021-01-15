from turtle import Turtle, Screen 



STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

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



    def up(self):
        if self.segments[0].heading != DOWN:
            self.segments[0].setheading(UP)
            self.segments[0].forward(MOVE_DISTANCE)


    def right(self):
        if self.segments[0].heading != LEFT:
            self.segments[0].setheading(RIGHT)
            self.segments[0].forward(MOVE_DISTANCE)
    def left(self):
        if self.segments[0].heading != RIGHT:
            self.segments[0].setheading(LEFT)
            self.segments[0].forward(MOVE_DISTANCE)

    def down(DOWN):
        if self.segments[0].heading != UP:
            self.segments[0].setheading(270)
            self.segments[0].forward(MOVE_DISTANCE)




