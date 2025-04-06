"""
Snake Game - Scoreboard Module
-----------------------------
This module contains the Scoreboard class which handles the display and
tracking of the player's score and lives in the game.
"""
from turtle import Turtle

# Display constants
ALIGNMENT = "center"
FONT = ("Arial", 24, "bold")  # Changed to bold for better visibility
GAME_OVER_FONT = ("Arial", 36, "bold")  # Larger font for game over message

class Scoreboard(Turtle):
    """
    A class representing the game's scoreboard.
    
    The scoreboard displays the current score and lives at the top of the screen
    and shows a game over message when the game ends.
    """
    def __init__(self):
        """
        Initialize the scoreboard with initial score, lives, and display properties.
        
        The scoreboard starts at 0 score and 3 lives, displayed at the top of the screen.
        """
        super().__init__()
        self.score = 0
        self.lives = 3  # Start with 3 lives
        self.color("white")
        self.penup()
        # Position at the top of the screen
        self.goto(0, 260)
        # Hide the turtle cursor
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the score and lives display on the screen.
        
        Shows the current score and remaining lives in the center of the top of the screen.
        """
        self.clear()  # Clear previous score
        self.write(f"Score: {self.score} | Lives: {self.lives}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increment the score and update the display.
        
        Called when the snake eats food.
        """
        self.score += 1
        self.update_scoreboard()

    def lose_life(self):
        """
        Decrease the number of lives by 1 and update the display.
        
        Returns:
            bool: True if the player still has lives remaining, False if game over
        """
        self.lives -= 1
        self.update_scoreboard()
        return self.lives > 0

    def game_over(self):
        """
        Display the game over message.
        
        Shows "GAME OVER" in the center of the screen when the game ends.
        """
        self.goto(0, 0)
        self.color("red")  # Change color to red for game over message
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
        
        # Add final score below game over message
        self.goto(0, -40)
        self.color("white")
        self.write(f"Final Score: {self.score}", align=ALIGNMENT, font=FONT)