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
- Dynamic game speed that increases with score
- Visual enhancements including colorful snake, food effects, and starry background
- Multiple lives system allowing players to continue after collisions
"""

import time
import random
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Initialize the game window
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("navy")  # Change background to navy blue for a night sky effect
screen.title("My Snake Game")
screen.tracer(0)  # Turn off automatic updates for smoother animation

# Create a starry background
def create_starry_background():
    """Create a starry night background with small stars."""
    stars = Turtle()
    stars.hideturtle()
    stars.penup()
    stars.color("white")
    stars.speed(0)  # Fastest speed
    
    # Draw stars (small white dots)
    for _ in range(100):  # Create 100 stars
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        stars.goto(x, y)
        stars.dot(random.randint(1, 3))  # Stars of different sizes
    
    # Draw a subtle border
    border = Turtle()
    border.hideturtle()
    border.penup()
    border.color("light blue")
    border.pensize(2)
    border.goto(-290, -290)
    border.pendown()
    for _ in range(4):
        border.forward(580)
        border.left(90)

# Create the starry background
create_starry_background()

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

# Game speed settings
INITIAL_SPEED = 0.1  # Starting speed (slower than original for better control)
MIN_SPEED = 0.02    # Fastest possible speed
SPEED_INCREASE = 0.005  # How much to increase speed by for each food eaten

# Main game loop
game_is_on = True
current_speed = INITIAL_SPEED

while game_is_on:
    screen.update()
    # Control game speed - decreases as score increases
    time.sleep(current_speed)

    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        
        # Increase game speed with each food eaten
        current_speed = max(MIN_SPEED, INITIAL_SPEED - (scoreboard.score * SPEED_INCREASE))

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # Check if player has lives remaining
        if scoreboard.lose_life():
            # Reset snake position and continue game
            snake.reset()
            food.refresh()
            # Pause briefly to show the collision
            time.sleep(1)
        else:
            # No lives left, game over
            game_is_on = False
            scoreboard.game_over()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            # Check if player has lives remaining
            if scoreboard.lose_life():
                # Reset snake position and continue game
                snake.reset()
                food.refresh()
                # Pause briefly to show the collision
                time.sleep(1)
            else:
                # No lives left, game over
                game_is_on = False
                scoreboard.game_over()

# Keep the window open until clicked
screen.exitonclick()