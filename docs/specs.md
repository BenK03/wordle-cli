# Terminal Wordle: Requirements Specification
This document outlines the requirements for a command-line Wordle game.

## 1. Functional Requirements
These requirements define the specific behaviors and rules of the application.

### 1.1. Game Start
- The application shall start a new game when the `--start` command-line flag is provided.

### 1.2. Target Word Selection
- The application shall select one random target word at the start of each game.
- The target word shall be exactly 5 letters long.

### 1.3. Guess Attempts
- The user shall be allowed a maximum of 6 valid guesses per game.
- Each valid guess shall consist of exactly 5 alphabetic characters.
- Invalid guesses shall not count toward the 6-guess limit.

### 1.4. Guess Evaluation
- After each valid guess, the application shall provide feedback for each letter:
  - Green if the letter is correct and in the correct position.
  - Yellow if the letter is correct but in the wrong position.
  - Gray if the letter does not appear in the target word.
- Duplicate letters shall be evaluated using standard Wordle rules:
  - Correct-position matches shall be evaluated first.
  - Remaining letters shall be marked yellow only up to the remaining count in the target word.

### 1.5. Game Completion
- The application shall declare a win if the user correctly guesses the target word within 6 valid guesses.
- The application shall declare a loss if the user fails to guess the target word after 6 valid guesses.
- Upon game completion, the application shall prompt the user to indicate whether they want to play again.

## 2. Non-Functional Requirements
These requirements define the technical constraints and standards for the application.

### 2.1. Technology Stack
- The application shall be written in Python 3.13.
- Command-line argument parsing shall be implemented using the Python standard library.
- Dependencies shall be managed using uv.

### 2.2. Output Requirements
- Letter feedback shall be displayed using terminal color output.
- The application shall correctly reset terminal formatting after colored output.

### 2.3. Code Quality
- The code shall be readable, modular, and maintainable.

## 3. High-Level Implementation Plan
1. Setup Project Structure: Create the project directory structure and define the main entrypoint for the application.
2. CLI Handling: Implement command-line argument handling to control application behavior.
3. Core Game Logic: Implement the main game logic, including word selection, guess handling, and game completion conditions.
4. Feedback Rendering: Display appropriate feedback to the user after each guess.
5. Replay Handling: Allow the user to start a new game after completion or exit the application.
6. Testing: Write unit tests for appropriate parts of the application to ensure correctness.