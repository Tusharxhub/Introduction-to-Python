# Build a simple command-line game of Rock-Paper-Scissors against the computer.



import random
import time

def get_user_choice():
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        print("Invalid choice. Please try again.")

def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user, computer):
    if user == computer:
        return 'tie'
    
    if (user == 'rock' and computer == 'scissors') or \
       (user == 'scissors' and computer == 'paper') or \
       (user == 'paper' and computer == 'rock'):
        return 'win'
        
    return 'lose'

def main():
    user_score = 0
    computer_score = 0
    ties = 0

    print("--- Welcome to Rock-Paper-Scissors! ---")
    print("Type 'quit' at any time to end the game.")
    
    while True:
        print("\n" + "="*30)
        user_choice_input = input("Enter your choice (rock, paper, or scissors): ").lower()

        if user_choice_input == 'quit':
            break
            
        if user_choice_input not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = get_computer_choice()
        
        print("...")
        time.sleep(0.5)
        print(f"You chose: {user_choice_input}")
        time.sleep(0.5)
        print(f"Computer chose: {computer_choice}")
        time.sleep(0.5)
        print("...")
        time.sleep(0.5)

        result = determine_winner(user_choice_input, computer_choice)

        if result == 'win':
            print("🎉 You win!")
            user_score += 1
        elif result == 'lose':
            print("😞 You lose.")
            computer_score += 1
        else:
            print("🤝 It's a tie.")
            ties += 1
            
        print(f"Score: You {user_score} - Computer {computer_score} (Ties: {ties})")

    print("\n--- Thanks for playing! ---")
    print(f"Final Score: You {user_score} - Computer {computer_score} (Ties: {ties})")


if __name__ == "__main__":
    main()
