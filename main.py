from turtle import Turtle, Screen 

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Python Game")
screen.bgcolor("black")
screen.listen()

#So far im doing it by myself
box = []
for boxes in range (0, 4):
    python = Turtle()
    python.color("white")
    python.shape("square")
    python.pencolor("white")
    python.speed(6)
    python.goto(0, 0)
    box.append(boxes)

def move_forward(): 
    python.setheading(0)
    python.forward(30)

# python.onkey(move_forward, "w")
#might have to use forloop to add more squares 
# or a while loop with an if statement 
# so it only adds squares when the snake eats
#Probably going to use this
#xcor()
#ycor() 


# screen = Screen()
# screen.setup(width=600, height=600)
# screen.title("Python Game")
# screen.bgcolor("black")
# screen.listen()
screen.exitonclick()