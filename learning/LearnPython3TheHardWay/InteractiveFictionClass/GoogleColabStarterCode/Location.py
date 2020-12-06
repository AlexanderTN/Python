#Location.py
import sqlite3
from Utils import check_preconditions
#from Main import createLocationObject
# Define the ID for the game:

class Location:
    """Locations are the places in the game that a player can visit.
    Internally they are represented nodes in a graph.  Each location stores
    a description of the location, any items in the location, its connections
    to adjacent locations, and any blocks that prevent movement to an adjacent
    location.  The connections is a dictionary whose keys are directions and
    whose values are the location that is the result of traveling in that 
    direction.  The travel_descriptions also has directions as keys, and its 
    values are an optional short desciption of traveling to that location.
    """
    def __init__(self, name, description, end_game=False):
        # A short name for the location
        self.name = name
        # A description of the location
        self.description = description
        # True if entering this location should end the game
        self.end_game = end_game
        # Dictionary mapping from directions to other Location objects
        self.connections = {}
        # Dictionary mapping from directions to text description of the path there
        self.travel_descriptions = {}
        # Dictionary mapping from item name to Item objects present in this location
        self.items = {}
        # Dictionary mapping from direction to Block object in that direction
        self.blocks = {}
        # Flag that gets set to True once this location has been visited by player
        self.has_been_visited = False

    def add_connection(self, direction, connected_location, travel_description=""):
        """Add a connection from the current location to a connected location.
            Direction is a string that the player can use to get to the connected
            location.  If the direction is a cardinal direction, then we also 
            automatically make a connection in the reverse direction."""
        self.connections[direction] = connected_location
        self.travel_descriptions[direction] = travel_description
        if direction == 'north':
            connected_location.connections["south"] = self
            connected_location.travel_descriptions["south"] = ""
        if direction == 'south':
            connected_location.connections["north"] = self
            connected_location.travel_descriptions["north"] = ""
        if direction == 'east':
            connected_location.connections["west"] = self
            connected_location.travel_descriptions["west"] = ""
        if direction == 'west':
            connected_location.connections["east"] = self
            connected_location.travel_descriptions["east"] = ""
        if direction == 'up':
            connected_location.connections["down"] = self
            connected_location.travel_descriptions["down"] = ""
        if direction == 'down':
            connected_location.connections["up"] = self
            connected_location.travel_descriptions["up"] = ""
        if direction == 'in':
            connected_location.connections["out"] = self
            connected_location.travel_descriptions["out"] = ""
        if direction == 'out':
            connected_location.connections["in"] = self
            connected_location.travel_descriptions["in"] = ""


    def add_item(self, name, item):
        """Put an item in this location."""
        self.items[name] = item

    def remove_item(self, item):
        """Remove an item from this location (for instance, if the player picks it
        up and puts it in their inventory)."""
        self.items.pop(item.name)


    def is_blocked(self, direction, game):
        """Check to if there is an obstacle in this direction."""
        if not direction in self.blocks:
            return False
        (block_description, preconditions) = self.blocks[direction]
        if check_preconditions(preconditions, game):
            # All the preconditions have been met.  You may pass.
            return False
        else: 
            # There are still obstalces to overcome or puzzles to solve.
            return True

    def get_block_description(self, direction):
        """Check to if there is an obstacle in this direction."""
        if not direction in self.blocks:
            return ""
        else:
            (block_description, preconditions) = self.blocks[direction]
            return block_description

    def add_block(self, blocked_direction, block_description, preconditions):
        """Create an obstacle that prevents a player from moving in the blocked 
        location until the preconditions are all met."""
        self.blocks[blocked_direction] = (block_description, preconditions)

def createLocationObject(name):
    connection = sqlite3.connect("K:\TamCloud\OneDrive\TrainingProgram_byTam3\ProductionTraining\Language\Python\LearnPythonTheHardway\Exercises_LearnPython3TheHardway\InteractiveFictionClass\GoogleColabStarterCode\ActionCastle.db")
    crsr = connection.cursor()
    commandLine = "SELECT * FROM Locations WHERE lID='{}'".format(name)
    crsr.execute(commandLine)
    query = crsr.fetchall()
    print(query)
    connection.close()
    return Location(query[0][1], query[0][2], query[0][3])

LocationID = {
    'cottage' : createLocationObject('LOCATION_COTTAGE'),
    'garden_path' : createLocationObject('LOCATION_GARDEN_PATH'),
    'cliff' : createLocationObject('LOCATION_CLIFF'),
    'fishing_pond' : createLocationObject('LOCATION_FISHING_POND'),
}
