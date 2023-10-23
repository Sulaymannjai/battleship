## BattleShip

Battleship Game is an exhilarating single-player naval warfare experience, where you take on the role of a cunning commander aiming to sink the computer's battleship. Sharpen your strategic skills and test your luck in this classic game of wits!

Table of Contents
.Introduction
.Features
.How to Play
.Usage
.Example Gameplay

## Introduction
Battleship Game is a Python implementation of the classic Battleship board game. It provides an interactive and engaging platform for players to challenge their logical reasoning and deduction skills. The game is played on a grid-based board, and the objective is to accurately guess and destroy the computer's hidden battleship within a limited number of turns.

## Features
### User-Friendly Interface:
 A simple and intuitive interface that allows players of all ages to enjoy the game effortlessly.
### Dynamic Board: 
The game board is displayed dynamically after each move, showing the player's hits and misses, enhancing the gaming experience.
Randomized Battleship Placement: The battleship's position is randomized at the beginning of each game, ensuring a unique challenge every time.
### Turn-Based Gameplay: 
Players have a limited number of turns to guess the battleship's location, adding an element of suspense and urgency to the game.

## How to Play

### Board Setup:

The game board is a square grid with rows and columns.
The battleship is placed randomly on the board at the start of the game.

### Game Rules:

You have a limited number of turns to guess the battleship's location.
Enter your guess for the row and column when prompted.
If your guess matches the battleship's location, you win! Otherwise, the game will inform you if you missed.

### Game Status:

The game will display the updated board after each guess. Your guesses are marked with 'X'.
If you don't guess the battleship's location within the given number of turns, the game will reveal the battleship's position.

## Usage
Upon launching the game, follow the on-screen instructions to input your guesses for the battleship's location.
Analyze the board after each guess to strategize your next move.
Keep playing until you either sink the battleship or exhaust all your turns.

## Example Gameplay

### Turn 1
Guess Row: 2
Guess Col: 3
You missed my battleship!
Current Board:
O O O O O
O O O O O
O O X O O
O O O O O
O O O O O

...

### Turn 2
Guess Row: 2
Guess Col: 3
Congratulations! You sunk my battleship!
Current Board:
O O O O O
O O O O O
O X O O O
O O O O O
O O O O O

You sunk my battleship in 2 turns! Well done!