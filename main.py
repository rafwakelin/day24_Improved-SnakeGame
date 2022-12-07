from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Sets up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Creates the initial body of the snake, piece of food, and initializes the score
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Listens to keyboard entries to control the snake headingLook
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:

    # Updates the screen for the initial snake set up
    screen.update()
    time.sleep(0.18)

    # Places the snake in position (0, 0) and starts moving east of the screen
    snake.move()

    # Detects if snake ate the food and places a new piece of food at a random location on the screen
    if snake.snake_body[0].distance(food) < 15:
        food.new_food()
        scoreboard.increase_score()
        snake.add()

    # Detects if snake hit the wall
    if snake.snake_body[0].xcor() > 295 or snake.snake_body[0].xcor() < -295 or snake.snake_body[0].ycor() > 295 \
            or snake.snake_body[0].ycor() < - 295:
        scoreboard.reset()
        snake.reset()

    # Detects if snake hit itself
    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
