"""
Snake Game - Snake Module
------------------------
This module contains the Snake class which handles the snake's behavior,
including movement, growth, and direction changes.
"""

from turtle import Turtle

# Game constants
# Initial snake segment positions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  
# Pixels to move in each step
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    A class representing the snake in the game.
    
    The snake consists of multiple segments that follow the head's movement.
    The snake can grow when eating food and cannot turn 180 degrees.
    """

    def __init__(self):
        """Initialize the snake with three segments in the starting position."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Create the initial snake body with three segments."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Add a new segment to the snake at the specified position.
        
        Args:
            position (tuple): The (x, y) coordinates for the new segment
        """
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add a new segment to the end of the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Move the snake forward.
        
        The head moves forward, and each segment follows the segment in front of it.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turn the snake upward if it's not moving downward."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Turn the snake downward if it's not moving upward."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Turn the snake left if it's not moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Turn the snake right if it's not moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)