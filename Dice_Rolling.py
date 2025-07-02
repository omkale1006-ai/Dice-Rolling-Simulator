# 🎲 1`` Simulator 🎲
# A fun Python project using random module to simulate dice roll

import random

# Generate a secret number between 1 and 6
secret_number = random.randint(1, 6)

# Function to simulate dice roll
def dice_roll():
    print("🎲 Welcome to the Dice Rolling Simulator!")
    print("🎯 Try to guess the number the dice will roll (1 to 6).")
    print("🔁 Type 'start' to roll the dice or 'end' to exit the game.")

    user_command = input("👉 Enter command (start/end): ").lower()

    if user_command == 'start':
        try:
            user_guess = int(input("🔢 Enter your guess (1 to 6): "))

            if 1 <= user_guess <= 6:
                print("🎲 Rolling the dice...")
                if user_guess == secret_number:
                    print("🎉 You guessed it right! You win! 🏆")
                else:
                    print("😢 Oops! Your guess didn't match the rolled number.")
                print(f"📌 Your guess: {user_guess}")
                print(f"🎲 Dice rolled: {secret_number}")
            else:
                print("⚠️ Please enter a number between 1 and 6.")
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
    
    elif user_command == 'end':
        print("👋 Exiting the game. Thanks for playing!")
    
    else:
        print("⚠️ Invalid command. Please type 'start' or 'end'.")

# Call the function to start the game
dice_roll()
