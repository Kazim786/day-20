from turtle import Screen #Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Python Game")
screen.bgcolor("black")
screen.tracer(0) #turns tracer off





snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


#So far im doing it by myself
box = []

x_pos = [0, -20, -40]

#If you want to make multiple versions of a thing just use a for loop
# for boxes in range (0, 3):
#     python = Turtle()
#     python.color("white")
#     python.shape("square")
#     python.pencolor("white")
#     python.penup()
#     python.speed(6)
#     python.goto(x = x_pos[boxes], y= 0)
    
#     box.append(python)





game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision from food

    if snake.head.distance(food) < 15:
        food.refresh()
        #Most likely going to put scoreboard updating code here too
        #Did it by myself
        scoreboard.goto(0, 250)
        scoreboard.clear()
        scoreboard.score += 1
        scoreboard.write(f"Score: {scoreboard.score}", True, font= ("Arial", 24, "normal")) #This is working too
        
        print(scoreboard.score)


#If the tail and head collide
    if snake.head.distance(snake.tail) <= 1: #THIS IS WORKING! DID IT BY MYSELF
        print("Game over") 
        scoreboard.score = 0
        scoreboard.clear() #Did by myself
        scoreboard.goto(0, 250)
        scoreboard.penup()
        scoreboard.write("GAME OVER", True, font= ("Arial", 24, "normal")) #This is working too

    # if snake.head.distance(wall) #for wall


#we have refactored our code so this has been commented out
#     for boxes in range(len(box) - 1, 0, -1):
#         new_x = box[boxes - 1].xcor()
#         new_y = box[boxes - 1].ycor()
#         box[boxes].goto(new_x, new_y)
        
#     box[0].forward(20)
#     box[0].left(90)
    
    # snake_obj.move()
    
    #not using this anymore
    # for boxes in box:
    #     boxes.forward(20)


















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



screen.exitonclick()