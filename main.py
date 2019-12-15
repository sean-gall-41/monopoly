import random
import numpy as np

def use_free_parking(prompt=""):
    response = input(prompt)
    while response[0].lower() not in ['y', 'n']:
        print("answer must start with 'y' or 'n'. Please try again.")
        response = input(prompt)
    if response[0].lower() == 'y':
        return True
    else:
        return False

# returns a list of the results of rolling n dice
def roll_n_dice(n):
    return [random.randint(1,6) for _ in np.arange(n)]


#This file runs the game events loop itself
print("====================================================================")
print("                  WELCOME TO THE GAME OF MONOPOLY                   ")
print("====================================================================")
print("Monopoly is a game all about capital: buy properties and charge rent")
print("to your competitors. Obtain full sets of like color properties to")
print("begin making houses and hotels to raise the rent on your properties!")
print("Be the last player with money and assets on the board to win!")


while True:
    try:
        num_players = int(input("\nTo begin, how many players will be " 
                                "playing?"))
        while num_players <= 1 or num_players >= 5:
            print("You can only play with 2, 3, or 4 players in this version!")
            num_players = int(input("To begin, how many players will be "
                                    "playing?"))
    except ValueError:
       print("You must enter a number to continue!") 

    use_free_parking = use_free_parking("\nNow, would you like to include the " 
                                        "free parking pool in your game? "
                                        "(y/n): ")
    print("\nOkay! Let's begin!")

    while True:
        print("Let's roll the dice to determine who goes first!\n")
        starting_rolls = []
        for i in np.arange(num_players):
            player_i_roll = roll_n_dice(2)
            print("player "+str(i+1)+" rolls a "+str(player_i_roll[0])+" and a "
                  +str(player_i_roll[1])+".")
            starting_rolls.append(player_i_roll)
        starting_rolls = np.array(starting_rolls)
        sums = [sum(starting_rolls[i]) for i in np.arange(num_players)]
        # assuming there exists a maximum value...(for now)
        # we're identifying players as the indices in range(n)
        first_player = sums.index(max(sums))

        print("\nAll right player", first_player+1, "it's your turn!")
        user_choice = input("what would you like to do?")



