# Rock Paper Scissors Game

A simple command-line implementation of the classic **Rock Paper Scissors** game in Python. Play against the computer, test your luck, and enjoy a fun interactive experience in your terminal!

---

<img src="RockPaperScissors.jpg" alt="Rock Paper Scissors Picture" width=400>


## Table of Contents

- [Project Description](#project-description)
- [Features](#features)
- [Installation](#installation)
  - [Requirements](#requirements)
- [Usage](#usage)
  - [Running the Game](#running-the-game)
  - [Game Flow](#game-flow)
- [Code Structure](#code-structure)
  - [Class: RockPaperScissors](#class-rockpaperscissors)
  - [Methods](#methods)
    - [`__init__`](#__init__)
    - [`get_user_choise`](#get_user_choise)
    - [`get_system_choise`](#get_system_choise)
    - [`evaluate`](#evaluate)
    - [`play`](#play)
- [Arguments and Return Values](#arguments-and-return-values)
- [License](#license)
- [Author](#author)

---

## Project Description

This project is a minimal Python implementation of Rock Paper Scissors, designed for educational purposes and quick play. The script offers a user-friendly interface, allowing you to play multiple rounds and see immediate results.

---

## Features

- Play against the computer in your terminal.
- Input validation ensures only valid choices are accepted.
- Displays both your and the computer's choices.
- Announces the winner or if the round is a tie.
- Option to continue playing or quit at any time.

---

## Installation

Simply clone the repository and you are ready to go.

```sh
git clone https://github.com/themohammadreza/Rock-Paper-Scissors.git
cd Rock-Paper-Scissors
```

### Requirements

The only dependency is Python's standard library:

```
random
```

**requirements.txt**
```txt
# No external dependencies required.
```

---

## Usage

### Running the Game

Simply execute the script using Python 3:

```sh
python main.py
```

### Game Flow

1. The game will prompt you to enter your choice: `rock`, `paper`, or `scissors`.
2. The computer will randomly select its choice.
3. The result will be displayed: win, lose, or tie.
4. You can press any key to play again, or `q` to quit.

---

## Code Structure

### Class: `RockPaperScissors`

Implements the entire game logic and flow.

#### Methods

##### `__init__`

- Initializes the game with valid choices.

##### `get_user_choise`

- Prompts the user for input.
- Validates the input.
- Returns: `str` - one of `"rock"`, `"paper"`, `"scissors"`.

##### `get_system_choise`

- Randomly selects a choice for the computer.
- Returns: `str` - one of `"rock"`, `"paper"`, `"scissors"`.

##### `evaluate(user_choise, system_choise)`

- Compares choices and determines the result.
- Arguments:
  - `user_choise` (`str`): User's selection.
  - `system_choise` (`str`): Computer's selection.
- Returns: `str` - Result message (`"Equal!"`, `"Congrats, You Won"`, or `"Oh shit, System Won"`).

##### `play`

- Executes a round of the game.
- Handles input/output and result display.

---

## Arguments and Return Values

- **User Input**: `"rock"`, `"paper"`, `"scissors"` (case-sensitive, must be typed exactly).
- **System Output**: Shows computer's choice, announces winner/tie.

---

## License

This project is licensed under the [MIT License](LICENSE).

```
MIT License

Copyright (c) 2025 Mohammad Reza

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

## Author

- **MohammadReza Naseri**  
  GitHub: [themohammadreza](https://github.com/themohammadreza)

---

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## Acknowledgements

Inspired by classic childhood games and Python learning projects.
