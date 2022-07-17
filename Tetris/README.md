# Tetris
A clone of the Gameboy version of Tetris

Control the falling blocks with the left and right arrows.
Holding the down arrow will make the block fall faster.
The spacebar rotates the current block.

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 Tetris 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- Tetris              (source code for game)
  +-- game              (specific game classes)
    +-- assets         (Media files)
    +-- blocks       (colorful blocks)
    +-- services       (various service classes)
    +-- shared        (various shared classes)
  +-- __main__.py       (entry point for program)
  +-- constants.py      (game constants)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Joshua Beale (bea177044@byui.edu)