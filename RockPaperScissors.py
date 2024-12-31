import random



class RockPaperScissors:

    def __init__(self, rounds):

        self.rounds = rounds

        self.choices = ['rock', 'paper', 'scissors']

        self.scores = {}

        self.winner_rules = [('rock', 'scissors'), ('scissors', 'paper'), ('paper', 'rock')]

        self.player1_name = "Player1"

        self.player2_name = "Player2"



    def set_player_names(self, mode):

        if mode == '1':  # Player vs Computer

            self.player1_name = input("Enter your name: ").strip()

            self.scores = {self.player1_name: 0, "Computer": 0}

        elif mode == '2':  # Player vs Player

            self.player1_name = input("Enter name for Player 1: ").strip()

            self.player2_name = input("Enter name for Player 2: ").strip()

            self.scores = {self.player1_name: 0, self.player2_name: 0}



    def get_player_choice(self, player_name):

        while True:

            print(f"{player_name}, please choose:")

            print("1: rock, 2: paper, 3: scissors")

            choice = input("Enter your choice (1/2/3): ").strip()

            if choice in ['1', '2', '3']:

                return self.choices[int(choice) - 1]

            else:

                print("Invalid input, please try again.")



    def get_computer_choice(self):

        return random.choice(self.choices)



    def determine_winner(self, choice1, choice2):

        if choice1 == choice2:

            return "Tie"

        elif (choice1, choice2) in self.winner_rules:

            return "Player1"

        else:

            return "Player2"



    def play_player_vs_computer(self):

        for round_num in range(1, self.rounds + 1):

            print(f"\n--- Round {round_num} ---")

            player_choice = self.get_player_choice(self.player1_name)

            computer_choice = self.get_computer_choice()

            print(f"{self.player1_name} chose: {player_choice}")

            print(f"Computer chose: {computer_choice}")



            result = self.determine_winner(player_choice, computer_choice)

            if result == "Tie":

                print("It's a tie!")

            elif result == "Player1":

                print(f"{self.player1_name} wins this round!")

                self.scores[self.player1_name] += 1

            else:

                print("Computer wins this round!")

                self.scores["Computer"] += 1



    def play_player_vs_player(self):

        for round_num in range(1, self.rounds + 1):

            print(f"\n--- Round {round_num} ---")

            player1_choice = self.get_player_choice(self.player1_name)

            player2_choice = self.get_player_choice(self.player2_name)

            print(f"{self.player1_name} chose: {player1_choice}")

            print(f"{self.player2_name} chose: {player2_choice}")



            result = self.determine_winner(player1_choice, player2_choice)

            if result == "Tie":

                print("It's a tie!")

            elif result == "Player1":

                print(f"{self.player1_name} wins this round!")

                self.scores[self.player1_name] += 1

            else:

                print(f"{self.player2_name} wins this round!")

                self.scores[self.player2_name] += 1



    def declare_final_winner(self):

        print("\n--- Final Scores ---")

        for player, score in self.scores.items():

            print(f"{player}: {score}")



        max_score = max(self.scores.values())

        winners = [player for player, score in self.scores.items() if score == max_score]



        if len(winners) == 1:

            print(f"Congratulations! {winners[0]} is the final winner!")

        else:

            print("It's a tie overall!")



    def start_game(self):

        while True:

            print("Choose game mode:")

            print("1: Player vs Computer")

            print("2: Player vs Player")

            mode = input("Enter your choice (1/2): ").strip()



            if mode in ['1', '2']:

                self.set_player_names(mode)

                if mode == '1':

                    self.play_player_vs_computer()

                elif mode == '2':

                    self.play_player_vs_player()

                break

            else:

                print("Invalid input, please try again.")



        self.declare_final_winner()





# اجرای بازی

if __name__ == "__main__":

    while True:

        try:

            rounds = int(input("How many rounds do you want to play? "))

            if rounds > 0:

                game = RockPaperScissors(rounds)

                game.start_game()

                break

            else:

                print("Please enter a positive number.")

        except ValueError:

            print("Invalid input. Please enter a valid number.")

