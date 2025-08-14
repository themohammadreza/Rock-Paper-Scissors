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
        self.choises = ["rock","paper","scissors"]

    def get_user_choise(self):
        """
        Get and validate the user's choice input.

        Returns:
            str: A valid choice (rock, paper, or scissors)
        """
        user_choise = input("please select your choise: (rock, paper or scissors) ")
        if user_choise in self.choises:
            return user_choise
        else:
            print("please select a valid choise whithin the available options!")
            return self.get_user_choise()

    def get_system_choise(self):
        """
        Generate a random choice for the computer.

        Returns:
            str: Random choice from available options (rock, paper, or scissors)
        """
        system_choise = random.choice(self.choises)
        return system_choise

    def evaluate(self, user_choise, system_choise):
        """
        Determine the winner based on both choices.

        Args:
            user_choise (str): The user's choice
            system_choise (str): The computer's choice

        Returns:
            str: Result message indicating who won or if it's a tie
        """
        if user_choise == system_choise:
            return "Equal!"
        elif (user_choise == 'rock' and system_choise == 'scissors') or \
             (user_choise == 'paper' and system_choise == 'rock') or \
             (user_choise == 'scissors' and system_choise == 'paper'):
                return "Congrats, You Won"
        else:
            return "Oh shit, System Won"

    def play(self):
        """
        Execute one round of the game.
        Gets choices from both user and computer, displays the result.
        """
        user_choise = self.get_user_choise()
        system_choise = self.get_system_choise()
        print(f"the computer choise was: {system_choise}")

        print(self.evaluate(user_choise, system_choise))


if __name__ == "__main__":
    game = RockPaperScissors()

    while True:
        game.play()

        play_again = input("Press q to quit, press any key to play again: ")
        if play_again.lower() == 'q':
            break
