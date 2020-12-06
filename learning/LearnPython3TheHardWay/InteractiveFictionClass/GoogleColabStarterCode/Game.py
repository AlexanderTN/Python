#Game.py
import Location
import Item
class Game:
    """The Game class represents the world.  Internally, we use a 
    graph of Location objects and Item objects, which can be at a 
    Location or in the player's inventory.  Each locations has a set of
    exits which are the directions that a player can move to get to an
    adjacent location. The player can move from one location to another
    location by typing a command like "Go North".
    """

    def __init__(self, start_at):
            # start_at is the location in the game where the player starts
            self.curr_location = start_at
            self.curr_location.has_been_visited = True
            # inventory is the set of objects that the player has collected/
            self.inventory = {}
            # Print the special commands associated with items in the game (helpful 
            # for debugging and for novice players).
            self.print_commands = True

    def describe(self):
            """Describe the current game state by first describing the current 
        location, then listing any exits, and then describing any objects
        in the current location."""
            self.describe_current_location()
            self.describe_exits()
            self.describe_items()

    def describe_current_location(self):
            """Describe the current location by printing its description field."""
            print(self.curr_location.description)

    def describe_exits(self):
            """List the directions that the player can take to exit from the current
        location."""
            exits = []
            for exit in self.curr_location.connections.keys():
                    exits.append(exit.capitalize())
            if len(exits) > 0:
                    print("Exits: ", end = '')
                    print(*exits, sep = ", ",)
    
    def describe_items(self):
            """Describe what objects are in the current location."""
            if len(self.curr_location.items) > 0:
                    print("You see: ")
                    for item_name in self.curr_location.items:
                            item = self.curr_location.items[item_name]
                            print(item.description)
                    if self.print_commands:
                            special_commands = item.get_commands()
                            for cmd in special_commands:
                                    print('\t', cmd)

    def add_to_inventory(self, item):
            """Add an item to the player's inventory."""
            self.inventory[item.name] = item
    
    def is_in_inventory(self,item):
            return item.name in self.inventory

    def get_items_in_scope(self):
            """Returns a list of items in the current location and in the inventory"""
            items_in_scope = []
            for item_name in self.curr_location.items:
                    items_in_scope.append(self.curr_location.items[item_name])
            for item_name in self.inventory:
                    items_in_scope.append(self.inventory[item_name])
            return items_in_scope