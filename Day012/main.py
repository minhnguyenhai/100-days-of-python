############### The Number Guessing Game Project #####################
import random
from art import logo

# Function to greet the player and introduce the game
def greeting():
    print(logo)
    print("Welcome to the Number Guessing game!")
    print("I'm thinking of a number between 1 and 100")

# Function to choose the difficulty level of the game
# Returns the number of attempts based on the chosen difficulty
def choose_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    
    if difficulty == "easy":
        return 10
    elif difficulty == "hard":
        return 5
    else:
        print("Invalid input. Try again!")
        return choose_difficulty()  # Recursively call the function if the input is invalid

# Main function to play the guessing game
def play_game():
    secret_number = random.randint(1, 100)  # Generate a random secret number between 1 and 100
    
    greeting()  # Display the greeting and game introduction
    number_of_attempts = choose_difficulty()  # Choose the difficulty and get the number of attempts
    
    is_guessed = False  # Variable to check if the number has been guessed correctly
    while not is_guessed:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        guessing_number = input("Make a guess: ")
        
        try:
            guessing_number = int(guessing_number)  # Try to convert the input to an integer
        except ValueError:
            number_of_attempts -= 1  # Decrease the number of attempts if the input is invalid
            print("Invalid input. Guess again.")
            continue  # Skip the current iteration and continue with the next one
        
        if guessing_number == secret_number:
            print(f"You got it! The answer was {secret_number}.")
            is_guessed = True  # Number guessed correctly, end the game
        else:
            if guessing_number > secret_number:
                print("Too high.")
            else:
                print("Too low.")
            
            number_of_attempts -= 1  # Decrease the number of attempts if the guess is incorrect
            
            if number_of_attempts == 0:
                print(f"You've run out of guesses, you lose. The number was {secret_number}.")
                break  # No more attempts left, end the game
            else:
                print("Guess again.")

# Start the game
play_game()
