#Item.py
from Utils import check_preconditions

class Item:
    """Items are objects that a player can get, or scenery that a player can
    examine."""
    def __init__(self,
               name,
               description,
               examine_text="",
               take_text="",
               start_at=None,
               gettable=True,
               end_game=False):
        # The name of the object
        self.name = name
        # The default description of the object.
        self.description = description
        # The detailed description of the player examines the object.
        self.examine_text = examine_text
        # Text that displays when player takes an object.
        self.take_text = take_text if take_text else ("You take the %s." % self.name)
        # Indicates whether a player can get the object and put it in their inventory.
        self.gettable = gettable
        # True if entering this location should end the game.
        self.end_game = end_game
        # The location in the Game where the object starts.
        if start_at:
            start_at.add_item(name, self)
        self.commands = {}


    def get_commands(self):
        """Returns a list of special commands associated with this object"""
        return self.commands.keys()

    def add_action(self, command_text, function, arguments, preconditions={}):
        """Add a special action associated with this item"""
        self.commands[command_text] = (function, arguments, preconditions)

    def do_action(self, command_text, game):
        """Perform a special action associated with this item"""
        end_game = False  # Switches to True if this action ends the game.
        if command_text in self.commands:
            function, arguments, preconditions = self.commands[command_text]
            if check_preconditions(preconditions, game):
                end_game = function(game, arguments)
        else:
            print("Cannot perform the action %s" % command_text)
        return end_game