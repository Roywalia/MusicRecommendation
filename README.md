# Arrange-Puzzle-Game

#### This is a C-based implementation of a 4x4 sliding puzzle game where the player can move tiles by pressing the 'w', 'a', 's', 'd' keys and aim to arrange the numbers in order.

## Game Overview
* The game board is a 4x4 grid, with 15 numbered tiles (1-15) and 1 empty space (represented by 0).
* The goal is to arrange the tiles in the correct order:

| 15  |  2  |  6  |  9  |
| --- | --- | --- | --- |
|  1  |  7  | 11  |  8  |
| 14  |  3  | 10  | 12  |
|  5  |  4  | 13  |     |

* The player can move the tiles around the empty space using the following controls:
  * `W` - To move the tile down
  * `A` - To move the tile right
  * `S` - To move the tile up
  * `D` - To move the tile left
 
## Requirements
#### A C compiler (e.g., GCC)

## How to run
1. Clone the repository:
  ```bash
    git clone https://github.com/yourusername/Arrange-Puzzle-Game.git
    cd Arrange-Puzzle-Game
  ```

2. Compile the program:
  ```bash
    gcc -o arrange-puzzle-game main.c
  ```

3. Run the game:
   ```bash
   ./arrange-puzzle-game
   ```

## Controls
* `W` - To move the tile down
* `A` - To move the tile right
* `S` - To move the tile up
* `D` - To move the tile left
