# Othello Board Game

This project implements the Othello board game in Human vs. Computer mode using Python, utilizing the alpha-beta pruning algorithm for computer moves.

## About Othello

Othello is a strategy board game for two players, played on an 8×8 uncheckered board using 64 disks that are white on one side and black on the other.

Players take turns placing disks with their color facing up, flipping opponent disks to their color when bounded by the newly placed disk and another disk of their color. 

The game ends when no more moves are possible, and the player with the most disks of their color wins.


## Project Requirements

- **Game Mode**: Human vs. Computer mode only.
  
- **Algorithm**: Alpha-beta pruning.
  
- **Programming Language**: Python only.

## Project Features

1. **Game Controller**:
   - Manages game turns between players.
     
   - Receives user moves.
     
   - Updates the game board.
     
   - Declares the end of the game.

2. **Knowledge Representation**:
   - Represents the game state appropriately.

3. **Utility Function**:
   - Evaluates the current game state for a given player.

4. **Alpha-beta Pruning Implementation**:
   - Implement the alpha-beta pruning algorithm.
     
   - Support for different difficulty levels:
     
     - Easy: Depth 1
       
     - Medium: Depth 3
       
     - Hard: Depth 5

5. **GUI**:
   - User interface in Python.


## Game Setup

- The board starts with two black and two white disks at the center.
  
- Each player has 30 disks.

## How the Game Proceeds

1. Players take turns placing a disk on an empty square adjacent to an opponent’s piece.
   
2. Legal moves (outflanking) enclose a straight line of opponent’s pieces, which are then flipped to the player’s color.
   
3. The game continues until no more moves are possible.
   
4. The player with the most disks of their color wins.

## Game Rules

- Black moves first.
  
- If a player cannot flip at least one opponent disk, they miss their turn.
  
- A disk may outflank disks in any direction.
  
- Players cannot skip over their own disks to outflank.
  
- Disks must be outflanked as a direct result of the move.
  
- The game may end if a player runs out of pieces.

## Project Structure
- `controller.py`: Contains the `OthelloController` class that handles the game logic.
  
- `main.py`: Initializes the `OthelloController` and starts the game.
  
- `model.py`: Contains the `Model` class that represents the game state and implements game rules and the alpha-beta pruning algorithm.
  
- `player.py`: Contains the `Player` class that represents a player in the game.
  
- `view.py`: Contains the `OthelloView` class that provides a graphical user interface using Tkinter.

## Usage

- Run the game using Python and follow the prompts to play against the computer. 

- Select the difficulty level to adjust the depth of the alpha-beta pruning algorithm.

## Contributors

We would like to thank the following contributors to this project:

- [Shahd Osama](https://github.com/shahdosama10).
  
- [Ahmed Saad](https://github.com/ahmedsaad123456).
  
- [Ahmed Adel](https://github.com/Dola1122).

- [Yousef Hussien](https://github.com/yousefhussien99).


---

Feel free to contribute to this project by opening issues or submitting pull requests.
