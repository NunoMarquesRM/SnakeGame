# Snake Game

A classic Snake game implementation in Python using the Turtle graphics library.

## Features

### Game Mechanics
- **Snake Movement**: Control the snake using arrow keys (Up, Down, Left, Right)
- **Snake Growth**: The snake grows longer each time it eats food
- **Food Collection**: Collect food items to increase your score
- **Collision Detection**: 
  - Wall collisions (lose a life if snake hits the screen boundaries)
  - Self collisions (lose a life if snake hits its own body)
- **Multiple Lives**: Start with 3 lives and continue playing after collisions
- **Score Tracking**: Keep track of your score as you collect food
- **Dynamic Difficulty**: Game speed increases as your score grows, making it progressively more challenging

### Visual Elements
- **Colorful Snake**: 
  - Green head for easy identification
  - Colorful body segments in light green, yellow, orange, and red
- **Dynamic Food**: 
  - Colorful food items that change color when eaten
  - Visual effect (size change) when food appears
- **Starry Background**: 
  - Navy blue background with randomly placed stars
  - Light blue border around the game area
- **Enhanced Scoreboard**: 
  - Bold text for better visibility
  - Displays current score and remaining lives
  - Red "GAME OVER" message with larger font
  - Final score display after game over

### Technical Features
- **Modular Design**: Code organized into separate modules for better maintainability
  - `main.py`: Game loop and main logic
  - `snake.py`: Snake behavior and movement
  - `food.py`: Food item behavior
  - `scoreboard.py`: Score tracking and display
- **Smooth Movement**: Snake segments follow the head's movement in a fluid motion
- **Prevent 180° Turns**: Snake cannot turn directly back on itself
- **Random Food Placement**: Food appears at random positions within game boundaries
- **Progressive Difficulty**: Game speed increases with score, creating a more challenging experience
- **Visual Effects**: Color changes, size animations, and starry background for enhanced gameplay
- **Life System**: Multiple lives with snake reset after collision

## How to Play

1. Run the game by executing `main.py`
2. Use the arrow keys to control the snake's direction
3. Collect food items to grow longer and increase your score
4. Avoid hitting the walls or your own tail
5. You have 3 lives - each collision costs one life
6. Try to achieve the highest score possible
7. Be prepared for increasing speed as your score grows

## Game Controls
- **Up Arrow**: Move snake upward
- **Down Arrow**: Move snake downward
- **Left Arrow**: Move snake left
- **Right Arrow**: Move snake right

## Game Rules
- The game starts with 3 lives
- Each collision with a wall or the snake's own body costs one life
- When a life is lost, the snake resets to its starting position and size
- The game ends when all lives are lost
- Each food item collected increases your score by 1
- The snake grows longer each time it eats food
- The game speed increases with each food item collected

## Technical Details
- **Game Window**: 600x600 pixels with navy blue background and starry night effect
- **Game Speed**: 
  - Starts at 0.1 seconds per frame
  - Decreases by 0.005 seconds for each food eaten
  - Has a minimum speed of 0.02 seconds per frame
- **Snake Movement**: 20 pixels per step
- **Snake Appearance**: Green head with colorful body segments
- **Food Appearance**: Colorful circles that change color when eaten
- **Food Boundaries**: Random position between -280 and 280 on both axes
- **Collision Detection**: 
  - Wall collision: When snake head is beyond ±280 on either axis
  - Food collision: When snake head is within 15 pixels of food
  - Tail collision: When snake head is within 10 pixels of any segment
- **Lives System**: 3 starting lives, snake resets after collision

## Dependencies
- Python 3.x
- Turtle graphics library (included in Python standard library)

## File Structure
- `main.py`: Main game loop and initialization
- `snake.py`: Snake class implementation
- `food.py`: Food item behavior
- `scoreboard.py`: Score tracking and display

## Future Enhancements
Potential improvements that could be added:
- Game restart functionality
- High score system
- Different difficulty levels
- Power-ups or special food items
- Obstacles or walls
- Sound effects 