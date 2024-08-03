from replit import clear
#HINT: You can call clear() to clear the output in the console.

# Import the logo from art.py
from art import logo
print(logo)
print("Welcome to the secret auction program.")

# Create a dictionary to store the bidders
bidders = {}
# Create a function to add the bidders
def add_bidder(name, bid):
  bidders[name] = bid
# Create a variable to store the highest bid
highest_bid = 0
name_of_highest_bidder = ""

end = False
while not end:
  # Ask for the name of the bidder
  name = input("What is your name?: ")
  # Ask for the bid
  bid = int(input("What's your bid?: $"))
  add_bidder(name, bid)
  if bid > highest_bid:
    highest_bid = bid
  # Ask if there are other bidders
  other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  # If there are other bidders, clear the screen and start again
  if other_bidders == "yes":
    clear()
  else:
    end = True

for bidder in bidders:
  if bidders[bidder] == highest_bid:
    name_of_highest_bidder = bidder

print(f"The winner is {name_of_highest_bidder} with a bid of ${highest_bid}")
