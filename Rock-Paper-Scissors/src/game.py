import random


class RockPaperScissors:

    def __init__(self):
        self.name = input("Hello my friend! Please enter your name: ")
        self.choices = ['rock', 'paper', 'scissors']
        self.user_score = 0
        self.computer_score = 0
        print(f"Welcome {self.name}! Welcome to Rock, Paper, Scissors game!")

    def get_user_choice(self):
        """Get user choice with better validation"""
        while True:
            print(f"\nAvailable choices: {', '.join(self.choices)}")
            user_choice = input("What's your choice? ").lower().strip()
            
            if user_choice in self.choices:
                print(f"Your choice: {user_choice}")
                return user_choice
            else:
                print(f"❌ Invalid choice! Please choose one of: {', '.join(self.choices)}")

    def get_computer_choice(self):
        """Get computer choice"""
        computer_choice = random.choice(self.choices)
        print(f"Computer choice: {computer_choice}")
        return computer_choice

    def determine_winner(self, user_choice, computer_choice):
        """Determine winner and update scores"""
        if user_choice == computer_choice:
            print("🤝 It's a tie!")
            return "tie"
        elif (
            (user_choice == 'rock' and computer_choice == 'scissors') or
            (user_choice == 'scissors' and computer_choice == 'paper') or
            (user_choice == 'paper' and computer_choice == 'rock')
        ):
            print("🎉 Congratulations! You win!")
            self.user_score += 1
            return "user"
        else:
            print("😔 Sorry! Computer wins!")
            self.computer_score += 1
            return "computer"

    def display_scores(self):
        """Display scores"""
        print(f"\n📊 Scores:")
        print(f"You: {self.user_score}")
        print(f"Computer: {self.computer_score}")

    def start_game(self):
        """Start a new game round"""
        print(f"\n{'='*40}")
        print(f"New Round - {self.name} vs Computer")
        print(f"{'='*40}")
        
        user_choice = self.get_user_choice()
        computer_choice = self.get_computer_choice()
        
        self.determine_winner(user_choice, computer_choice)
        self.display_scores()

    def play_again(self):
        """Ask for another game"""
        while True:
            response = input("\nDo you want to play again? (y/n): ").lower().strip()
            if response in ['y', 'yes']:
                return True
            elif response in ['n', 'no']:
                return False
            else:
                print("❌ Please enter 'y' or 'n'!")


def main():
    """Main program function"""
    print("🎮 Rock, Paper, Scissors Game")
    print("=" * 40)
    
    game = RockPaperScissors()
    
    while True:
        game.start_game()
        
        if not game.play_again():
            print(f"\n👋 Goodbye {game.name}! Hope you enjoyed the game!")
            print(f"Your final score: {game.user_score}")
            print(f"Computer's final score: {game.computer_score}")
            
            if game.user_score > game.computer_score:
                print("🏆 You won the overall game!")
            elif game.computer_score > game.user_score:
                print("😔 Computer won the overall game!")
            else:
                print("🤝 The overall game was a tie!")
            break


if __name__ == '__main__':
    main()
