"""
Snake Game - Main Module
-----------------------
This is the main entry point for the Snake game. It handles the game loop,
keyboard controls, and collision detection.

The game features:
- Snake movement using arrow keys
- Food collection and snake growth
- Score tracking
- Collision detection with walls and self
"""

import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Initialize the game window
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My Snake Game")

# Create game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Set up keyboard controls
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    # Control game speed
    time.sleep(0.05)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# Keep the window open until clicked
screen.exitonclick()