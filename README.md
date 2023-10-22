# Battleship Game

Battleship Game is a simple text-based single-player game implemented in Python. Try to sink the computer's battleship by guessing its location on the game board.

## Table of Contents
- [Game Overview](#game-overview)
- [How to Play](#how-to-play)
- [Getting Started](#getting-started)
- [Customization](#customization)
- [Example Gameplay](#example-gameplay)
- [Contributing](#contributing)
- [License](#license)

## Game Overview

Battleship is a turn-based game where you attempt to guess the coordinates of the hidden battleship on the game board. The game provides visual feedback on your guesses, allowing you to refine your strategy with each turn. The objective is to sink the battleship within a limited number of attempts.

## How to Play

1. **Board Setup:**
    - The game board is a square grid with rows and columns.
    - The battleship is placed randomly on the board at the start of the game.

2. **Game Rules:**
    - You have a limited number of turns to guess the battleship's location.
    - Enter your guess for the row and column when prompted.
    - If your guess matches the battleship's location, you win! Otherwise, the game will inform you if you missed.

3. **Game Status:**
    - The game will display the updated board after each guess. Your guesses are marked with 'X'.
    - If you don't guess the battleship's location within the given number of turns, the game will reveal the battleship's position.
