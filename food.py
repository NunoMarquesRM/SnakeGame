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
    
    The food appears as a small blue circle at random positions on the screen.
    When eaten by the snake, it will reappear at a new random location.
    """

    def __init__(self):
        """
        Initialize the food item with its appearance and properties.
        
        The food is represented as a small blue circle that can move
        to random positions on the screen.
        """
        super().__init__()
        self.shape("circle")
        self.penup()
        # Make the food smaller than default
        self.shapesize(0.5, 0.5)
        self.color("blue")
        # Ensure instant movement
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Move the food to a new random position on the screen.
        
        The food will appear within the game boundaries (-280 to 280 on both axes).
        """
        self.goto(random.randint(-280, 280), random.randint(-280, 280))