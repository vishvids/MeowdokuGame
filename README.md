# MeowdokuGame
# 🐱 Meowdoku – A Simple Cat-Finding Game

Meowdoku is a simple, text-based game built with Python. The goal is to find all the hidden cats on a game board by guessing their row and column positions.

The game generates a coloured board with hidden cat locations. Players make guesses, receive feedback, and continue until all the cats have been found.

## 🎮 How to Play

1. Run the Python program.
2. The game displays a board containing different coloured regions.
3. Enter a row number when prompted.
4. Enter a column number.
5. The game tells you whether you found a cat.
6. Keep guessing until you find all the cats!

**Game symbols:**
- `_` — An unguessed position.
- `C` — A correctly guessed cat location.
- `X` — An incorrect guess.

**Note:** Row and column indices start at `0`. On the default 4 × 4 board, valid indices are `0` to `3`.

## ✨ Features

- Text-based gameplay in the terminal.
- Randomly selected board solution.
- Shuffled colours for different board arrangements.
- Input validation for row and column selections.
- Feedback for correct and incorrect guesses.
- Tracks the number of guesses taken to find all cats.
- Customisable board size through the game classes.

## 🛠️ Technologies Used

- Python 3
- Python `random` module

## 🚀 How to Run

**Prerequisites:** Install Python 3.

1. Clone this repository:

   ```bash
   git clone YOUR_REPOSITORY_URL
   ```

2. Navigate to the project folder:

   ```bash
   cd YOUR_PROJECT_FOLDER
   ```

3. Run the game:

   ```bash
   python "medowku game.2.py"
   ```

   If your file has a different name, replace the filename in the command.

## 📚 What I Learned

Through this project, I practised:

- Object-oriented programming using Python classes.
- Representing a game board with two-dimensional lists.
- Using loops and conditional statements to manage game logic.
- Generating randomised game configurations.
- Validating user input and handling invalid entries.
- Separating board management from the main game logic.

## 🔮 Future Improvements

- Add clearer messages when players enter invalid input.
- Prevent repeated guesses from counting towards the total.
- Improve the game interface and display.
- Add difficulty levels and more board configurations.
- Add a restart option after completing a game.

---

*Built as a Python learning project.* 🐾
