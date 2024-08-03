############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

######################################################         My code below this line 👇        ########################################################

import random
from replit import clear
from art import logo

# List of possible card values in a deck
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Lists to hold the cards for the user and computer
user_cards = []
computer_cards = []

# Scores for the user and computer
user_score = 0
computer_score = 0

# Function to add a new card to the given hand (user or computer)
def hit(current_cards):
    current_score = sum(current_cards)
    hit_card = random.choice(cards)
    # If the new card is an Ace and it would cause the score to go over 21, treat it as 1 instead of 11
    if hit_card == 11 and current_score + hit_card > 21:
        hit_card = 1

    current_cards.append(hit_card)

# Function to adjust the score if there are Aces and the score is over 21
def adjust_score(current_cards):
    current_score = sum(current_cards)
    # Change Aces from 11 to 1 if the score is over 21
    while current_score > 21 and 11 in current_cards:
        index_ace = current_cards.index(11)
        current_cards[index_ace] = 1
        current_score = sum(current_cards)

# Function to display a winning message when the user wins with a Blackjack
def win_with_blackjack():
    print(f"Your cards: {user_cards}, current score: 0")
    print(f"Computer's first card: {computer_cards[0]}")
    print(f"Your final hand: {user_cards}, final score: 0")
    print(f"Computer's final hand: [{computer_cards[0]}], final score: {computer_cards[0]}")
    print(f"Win with a Blackjack 😎")

# Function to display a losing message when the computer wins with a Blackjack
def lose_by_blackjack():
    print(f"Computer's final hand: {computer_cards}, final score: 0")
    print(f"Lose, opponent has Blackjack 😱")

# Function to determine the outcome of the game and display appropriate messages
def showdown():
    global user_score, computer_score
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    
    if user_score > 21:
        print(f"Computer's final hand: [{computer_cards[0]}], final score: {computer_cards[0]}")
        print("You went over. You lose 😭")
    elif computer_score == 21 and len(computer_cards) == 2:
        lose_by_blackjack()
    else:
        while computer_score < 17:
            hit(computer_cards)
            computer_score = sum(computer_cards)
            
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        if computer_score > 21:
            print("Opponent went over. You win 😁")
        elif user_score > computer_score:
            print("You win 😃")
        elif user_score < computer_score:
            print("You lose 😤")
        else:
            print("Draw 🙃")

# Main function to play the game
def play_game():
    global user_score, computer_score
    print(logo)
    
    # Reset cards and scores
    user_cards.clear()
    computer_cards.clear()
    user_score = 0
    computer_score = 0

    # Deal initial two cards to user and computer
    for i in range(2):
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        user_score += user_cards[i]
        computer_score += computer_cards[i]
    
    if user_score == 21:
        win_with_blackjack()
    else:
        # Adjust the score if initial two cards are 11, 11
        if user_score > 21:
            adjust_score(user_cards)
            user_score = sum(user_cards)
        if computer_score > 21:
            computer_cards[1] = 1
            computer_score = sum(computer_cards)
    
        should_continue = True
        while should_continue:
            print(f"Your cards: {user_cards}, current score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")
        
            if user_score > 21:
                showdown()
                should_continue = False
            else:
                if input("Type 'y' to get another card, type 'n' to pass: ") == "y":
                    hit(user_cards)
                    adjust_score(user_cards)
                    user_score = sum(user_cards)
                else:
                    showdown()
                    should_continue = False
    
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
        clear()
        play_game()

# Start the game
play_game()
