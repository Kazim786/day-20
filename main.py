from turtle import Turtle, Screen 

#So far im doing it by myself
python = Turtle()
python.color("white")
python.shape("square")
python.pencolor("white")

#might have to use forloop to add more squares 
# or a while loop with an if statement 
# so it only adds squares when the snake eats
#Probably going to use this
#xcor()
#ycor() 


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Python Game")
screen.bgcolor("black")
screen.exitonclick()