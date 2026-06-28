Tic-Tac-Toe AI using Minimax Algorithm

Project Overview

This project implements an AI-powered Tic-Tac-Toe game where a human player competes against an unbeatable computer opponent. The AI uses the Minimax algorithm, a classical Artificial Intelligence search algorithm, to evaluate every possible game state and always choose the optimal move.

The project demonstrates the concepts of Artificial Intelligence, Game Theory, Search Algorithms, Decision Making, and Recursive Programming using Python.

---

Objectives

- Develop a console-based Tic-Tac-Toe game.
- Implement the Minimax algorithm for optimal AI decision-making.
- Understand game tree search and recursion.
- Learn game state evaluation techniques.
- Demonstrate basic Artificial Intelligence concepts.

---

Features

- Human vs AI gameplay
- Unbeatable AI using the Minimax algorithm
- Console-based interface
- Input validation
- Win, loss, and draw detection
- Score tracking
- Replay option
- Beginner-friendly and well-commented code

---

Technologies Used

- Python 3
- Python Standard Library

---

Project Structure

Tic-Tac-Toe-AI/
│
├── tic_tac_toe.py
├── README.md
├── LICENSE
│
├── screenshots/
    ├── home.png
    ├── gameplay.png
    └── result.png


---

Installation

1. Install Python 3.

2. Clone the repository:

git clone https://github.com/yourusername/Tic-Tac-Toe-AI.git

3. Navigate to the project folder:

cd Tic-Tac-Toe-AI

4. Run the program:

python tic_tac_toe.py

---

How to Play

- You play as X.
- The AI plays as O.
- Enter a number from 1–9 to place your mark.
- The first player to align three symbols horizontally, vertically, or diagonally wins.
- If all cells are filled without a winner, the game ends in a draw.

---

Minimax Algorithm

The AI uses the Minimax algorithm to evaluate every possible move recursively.

- Maximizing player → AI
- Minimizing player → Human
- AI chooses the move with the highest score.
- Human is assumed to play optimally.

This makes the AI impossible to defeat.

---

Sample Output

TIC-TAC-TOE AI

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

Enter move (1-9): 5

AI played.

 X |   |
---+---+---
   | O |
---+---+---
   |   |

---

Future Enhancements

- Graphical User Interface (Tkinter)
- Alpha-Beta Pruning optimization
- Difficulty levels
- Multiplayer mode
- Voice interaction
- Online multiplayer

---

Author

Sudduneeraja
