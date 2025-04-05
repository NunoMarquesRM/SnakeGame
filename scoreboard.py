"""
Snake Game - Scoreboard Module
-----------------------------
This module contains the Scoreboard class which handles the display and
tracking of the player's score in the game.
"""
from turtle import Turtle

# Display constants
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    """
    A class representing the game's scoreboard.
    
    The scoreboard displays the current score at the top of the screen
    and shows a game over message when the game ends.
    """
    def __init__(self):
        """
        Initialize the scoreboard with initial score and display properties.
        
        The scoreboard starts at 0 and is displayed at the top of the screen.
        """
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        # Position at the top of the screen
        self.goto(0, 260)
        # Hide the turtle cursor
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the score display on the screen.
        
        Shows the current score in the center of the top of the screen.
        """
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increment the score and update the display.
        
        Called when the snake eats food.
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        """
        Display the game over message.
        
        Shows "GAME OVER" in the center of the screen when the game ends.
        """
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)