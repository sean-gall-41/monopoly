import numpy as np
# TODO: Make a space class, representing which space the player is on...
# NOTE: spaces should be distinguished into two classes: properties and
# special spaces. Special spaces include GO, JAIL, JUST VISTING, etc. 
total_num_spaces = 7
#TODO: change location of total_num_spaces to gameboard, or other file

class player():
    def __init__(self, play_id=0):
        # TODO: change money attrib to a map, where keys are strings of each
        # value and the values are the quantity of each bill
        self.player_id = play_id
        self.total_funds = 0
        self.money = 0
        self.position = 0
        # TODO: find out how many properties are in the game, initialize array
        # to that size
        # NOTE: maybe make the properties attrib a set so that if we try to add 
        # an already existing property, get an error
        # OR make the overall properties attrib (The container of all prop)
        # a set and pop each one as players buy them so that the actual 
        # properties will be traded in memory as they'll be traded in the game 
        self.properties = np.array([])
        self.chance_cards = np.array([])

    def move_player(self, num_spaces):
        self.position = (self.position + num_spaces) % total_num_spaces 

