import random
from replit import clear
from art import logo, vs
from game_data import data

# Global variable to store the score
score = 0

# Function to display a success message when the player guesses correctly
def display_success_message():
    # Clear the screen
    clear()
    # Display the game logo
    print(logo)
    # Display the success message and current score
    print(f"You're right! Current score: {score}.")

# Function to display the game over message when the player guesses incorrectly
def game_over():
    # Clear the screen
    clear()
    # Display the game logo
    print(logo)
    # Display the game over message and final score
    print(f"Sorry, that's wrong. Final score: {score}")

# Main function to play the game
def play_game():
    global score
    # Select a random account from the data as account A
    account_A = random.choice(data)
    print(logo)
    
    is_correct_answer = True
    while is_correct_answer:
        # Remove account A from the data to avoid duplicate selection
        data.remove(account_A)
        # Select a random account from the data as account B
        account_B = random.choice(data)
        # Re-add account A back to the data
        data.append(account_A)
        # Determine the correct answer based on follower count
        correct_answer = "A" if account_A["follower_count"] > account_B["follower_count"] else "B"
        
        # Display account A's details
        print(f'Compare A: {account_A["name"]}, a {account_A["description"]}, from {account_A["country"]}')
        print(vs)
        # Display account B's details
        print(f'Against B: {account_B["name"]}, a {account_B["description"]}, from {account_B["country"]}')
        
        # Get the player's guess
        if input("Who has more followers? Type 'A' or 'B': ") == correct_answer:
            # Increment the score if the player guesses correctly
            score += 1
            # Display the success message
            display_success_message()
            # Set account A to account B for the next round
            account_A = account_B
        else:
            # Clear the screen and display the game over message
            clear()
            game_over()
            # End the game loop
            is_correct_answer = False

# Start the game
play_game()
