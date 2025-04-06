"""
Snake Game - Food Module
-----------------------
This module contains the Food class which handles the food item's behavior
and appearance in the game.
"""

import random
from turtle import Turtle

class Food(Turtle):
    """
    A class representing the food item in the game.
    
    The food appears as a colorful circle at random positions on the screen.
    When eaten by the snake, it will reappear at a new random location.
    """

    def __init__(self):
        """
        Initialize the food item with its appearance and properties.
        
        The food is represented as a colorful circle that can move
        to random positions on the screen.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.7, 0.7)  # Make the food slightly larger
        self.color("red")  # Default color
        self.speed("fastest")  # Ensure instant movement
        self.food_colors = ["red", "blue", "green", "yellow", "purple", "orange"]
        self.refresh()

    def refresh(self):
        """
        Move the food to a new random position on the screen and change its color.
        
        The food will appear within the game boundaries (-280 to 280 on both axes)
        with a random color from the food_colors list.
        """
        # Change to a random color
        self.color(random.choice(self.food_colors))
        # Move to a random position
        self.goto(random.randint(-280, 280), random.randint(-280, 280))
        # Add a small visual effect - briefly make it larger then return to normal
        self.shapesize(1.0, 1.0)
        self.shapesize(0.7, 0.7)