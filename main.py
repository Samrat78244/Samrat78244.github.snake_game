### Main

from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake
import time

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

my_screen.listen()
my_screen.onkey(snake.up, "w")
my_screen.onkey(snake.down, "s")
my_screen.onkey(snake.left, "a")
my_screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    my_screen.update()
    time.sleep(0.1)
    snake.move()

# Detecting collision with food
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

# Detecting collision with food
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

# Detecting collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment)<15:
            game_is_on = False
            scoreboard.game_over()


my_screen.exitonclick()
