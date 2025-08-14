import random

class RockPaperScissors:
    """
    A class that implements the Rock Paper Scissors game logic.
    Allows a user to play against the computer in a command-line interface.
    """

    def __init__(self):
        """
        Initialize the game with valid choices.
        """
        self.choices = ["rock","paper","scissors"]

    def get_user_choice(self):
        """
        Get and validate the user's choice input.

        Returns:
            str: A valid choice (rock, paper, or scissors)
        """
        user_choice = input("please select your choice: (rock, paper or scissors) ").lower()
        if user_choice in self.choices:
            return user_choice
        else:
            print("please select a valid choice within the available options!")
            return self.get_user_choice()

    def get_system_choice(self):
        """
        Generate a random choice for the computer.

        Returns:
            str: Random choice from available options (rock, paper, or scissors)
        """
        system_choice = random.choice(self.choices)
        return system_choice

    def evaluate(self, user_choice, system_choice):
        """
        Determine the winner based on both choices.

        Args:
            user_choice (str): The user's choice
            system_choice (str): The computer's choice

        Returns:
            str: Result message indicating who won or if it's a tie
        """
        if user_choice == system_choice:
            return "Equal!"
        elif (user_choice == 'rock' and system_choice == 'scissors') or \
             (user_choice == 'paper' and system_choice == 'rock') or \
             (user_choice == 'scissors' and system_choice == 'paper'):
                return "Congrats, You Won"
        else:
            return "Oh shit, System Won"

    def play(self):
        """
        Execute one round of the game.
        Gets choices from both user and computer, displays the result.
        """
        user_choice = self.get_user_choice()
        system_choice = self.get_system_choice()
        print(f"the computer choice was: {system_choice}")

        print(self.evaluate(user_choice, system_choice))


if __name__ == "__main__":
    game = RockPaperScissors()

    while True:
        game.play()

        play_again = input("Press q to quit, press any key to play again: ")
        if play_again.lower() == 'q':
            break
