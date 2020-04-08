# Write a class to hold player information, e.g. what room they are in
# currently.

class Player():
    def __init__(self, location, inventory):
        # if self.location == None:
        #     self.location = room['outside']
        # else:
        self.location = location
        # if self.inventory == None:
        #     self.inventory = {}
        # else:
        self.inventory = inventory
