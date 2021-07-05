import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

mysnake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(mysnake.up, "Up")
screen.onkey(mysnake.down, "Down")
screen.onkey(mysnake.left, "Left")
screen.onkey(mysnake.right, "Right")


game_is_on = True
while game_is_on:#for moving the segments
    screen.update()
    time.sleep(0.1)
    mysnake.move()
    #detect collision with food
    if mysnake.segments[0].distance(food)<15:
        food.refresh()
        mysnake.extend()
        scoreboard.increase_score()
    # detect collision with food
    if mysnake.head.xcor() > 280 or mysnake.head.xcor() < -280 or mysnake.head.ycor() > 280 or mysnake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    for segment in mysnake.segments[1:]:

        if mysnake.head.distance(segment)<10:
            game_is_on = False
            scoreboard.game_over()
    #if head collides with any segment in the tail:
        #trigger game over


screen.exitonclick()