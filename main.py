from turtle import Turtle, Screen 

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Python Game")
screen.bgcolor("black")
screen.listen()

#So far im doing it by myself
box = []

x_pos = [0, -20, -40]

for boxes in range (0, 3):
    python = Turtle()
    python.color("white")
    python.shape("square")
    python.pencolor("white")
    python.speed(6)
    python.goto(x = x_pos[boxes], y= 0)
    box.append(boxes)

# print(box)


# def move_forward(): 
#     python.setheading(0)
#     python.forward(30)

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