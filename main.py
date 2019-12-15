import random
import numpy as np

def get_yes_or_no(prompt=""):
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

    use_free_parking = get_yes_or_no("\nNow, would you like to include the " 
                                        "free parking pool in your game? "
                                        "(y/n): ")
    print("\nOkay! Let's begin!")

    
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
    current_player = first_player
    
    #enter the game loop
    while True:
        print("\nAll right player", current_player+1, "it's your turn!")
        user_choice = input("what would you like to do? (r)oll, or (c)heck "
                            "inventory? ")
        while user_choice.lower() not in ['r', 'c']:
            print("Reponse must start with 'r' or 'c'. Try again!")
            user_choice = input("what would you like to do? (r)oll, or (c)heck "
                            "inventory? ")
        
        if user_choice.lower() == 'c':
            print("This will be the player's inventory when that functionality"
                  "is implemented.")
        else:
            current_roll = roll_n_dice(2)
            print("player "+str(current_player+1)+" rolls a "+
                  str(current_roll[0])+" and a "+str(current_roll[1])+".")
            
            #some temp var until implement player and board functions here
            pass_go = True
            current_player_cash = 0
            # temp space codes are as follows:
            # P = PROPERTY
            # R = RAILROAD
            # U = UTILITY
            # GTJ = GO TO JAIL
            # CC = COMMUNITY CHEST
            # C = CHANCE
            # T = TAXES
            # FP = FREE PARKING
            # JV = JUST VISTING
            space_types = np.array(['P', 'R', 'U', 'GTJ',
                                    'CC', 'C', 'T', 'FP', 'JV'])
            current_space = 'P'
            is_owned = False

            if pass_go:
                current_player_cash += 200
            
            if current_space == space_types[0]:
                if is_owned:
                    print("This property is owned by (insert player name)! You "
                          "owe them (amount) in rent.")
                else:
                    #TODO: display property name, and stats to player
                    buy_prop = get_yes_or_no("Looks like this property isn't "
                                             "owned. would you like to buy this "
                                             "property? ")
                    
                    if buy_prop:
                        print("You just bought (insert property name)!")
                    else:
                        pass

            elif current_space == space_types[1]:
                pass
            elif current_space == space_types[2]:
                pass
            elif current_space == space_types[3]:
                pass
            elif current_space == space_types[4]:
                pass
            elif current_space == space_types[5]:
                pass
            elif current_space == space_types[6]:
                pass
            elif current_space == space_types[7]:
                pass
            elif current_space == space_types[8]:
                pass

            current_player = (current_player + 1) % num_players
            # any other kind of game stats you want to keep track of? such as:
            # number of turns
