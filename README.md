# Snake Game

A classic Snake game implementation in Python using the Turtle graphics library.

## Features

### Game Mechanics
- **Snake Movement**: Control the snake using arrow keys (Up, Down, Left, Right)
- **Snake Growth**: The snake grows longer each time it eats food
- **Food Collection**: Collect food items to increase your score
- **Collision Detection**: 
  - Wall collisions (game ends if snake hits the screen boundaries)
  - Self collisions (game ends if snake hits its own body)
- **Score Tracking**: Keep track of your score as you collect food

### Visual Elements
- **Snake**: White square segments that follow the head's movement
- **Food**: Small blue circles that appear at random positions
- **Scoreboard**: White text displaying current score at the top of the screen
- **Game Over Screen**: Centered "GAME OVER" message when the game ends

### Technical Features
- **Modular Design**: Code organized into separate modules for better maintainability
  - `main.py`: Game loop and main logic
  - `snake.py`: Snake behavior and movement
  - `food.py`: Food item behavior
  - `scoreboard.py`: Score tracking and display
- **Smooth Movement**: Snake segments follow the head's movement in a fluid motion
- **Prevent 180° Turns**: Snake cannot turn directly back on itself
- **Random Food Placement**: Food appears at random positions within game boundaries

## How to Play

1. Run the game by executing `main.py`
2. Use the arrow keys to control the snake's direction
3. Collect food items to grow longer and increase your score
4. Avoid hitting the walls or your own tail
5. Try to achieve the highest score possible

## Game Controls
- **Up Arrow**: Move snake upward
- **Down Arrow**: Move snake downward
- **Left Arrow**: Move snake left
- **Right Arrow**: Move snake right

## Game Rules
- The game ends if the snake hits the wall (screen boundaries)
- The game ends if the snake hits its own body
- Each food item collected increases your score by 1
- The snake grows longer each time it eats food

## Technical Details
- **Game Window**: 600x600 pixels with black background
- **Game Speed**: Fixed at 0.05 seconds per frame
- **Snake Movement**: 20 pixels per step
- **Food Boundaries**: Random position between -280 and 280 on both axes
- **Collision Detection**: 
  - Wall collision: When snake head is beyond ±280 on either axis
  - Food collision: When snake head is within 15 pixels of food
  - Tail collision: When snake head is within 10 pixels of any segment

## Dependencies
- Python 3.x
- Turtle graphics library (included in Python standard library)

## File Structure
- `main.py`: Main game loop and initialization
- `snake.py`: Snake class implementation
- `food.py`: Food class implementation
- `scoreboard.py`: Score tracking and display

## Future Enhancements
Potential improvements that could be added:
- Increasing difficulty as the snake grows
- Speed control options
- Game restart functionality
- High score system
- Different difficulty levels
- Visual enhancements (colors, effects)
- Power-ups or special food items
- Obstacles or walls
- Multiple lives
- Sound effects 