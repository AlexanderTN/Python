#Main.py
import sqlite3
from Parser import Parser
from Location import Location,LocationID,createLocationObject
from Item import Item
from Game import Game
from Utils import add_item_to_inventory, describe_something, end_game


def build_game():
    #connection = sqlite3.connect("K:\TamCloud\OneDrive\TrainingProgram_byTam3\ProductionTraining\Language\Python\LearnPythonTheHardway\Exercises_LearnPython3TheHardway\InteractiveFictionClass\GoogleColabStarterCode\ActionCastle.db")
    #crsr = connection.cursor()

    # Locations
    # crsr.execute("SELECT * FROM Locations WHERE lID='LOCATION_COTTAGE'")#.format(LocationID['cottage']))
    # query = crsr.fetchall()
    # print(query)
    # cottage = Location(query[0][1], query[0][2], query[0][3])
    #for key in LocationID.keys():
        #key = createLocationObject(LocationID[key])
    #cottage = createLocationObject(LocationID['cottage'])
    #cottage = Location("Cottage", "You are standing in a small cottage.")
    #garden_path = Location("Garden Path", "You are standing on a lush garden path. There is a cottage here.")
    #garden_path = createLocationObject(LocationID['garden_path'])
    #cliff = Location("Cliff", "There is a steep cliff here. You fall off the cliff and lose the game. THE END.", end_game=True)
    #cliff = createLocationObject(LocationID['cliff'])
    #fishing_pond = Location("Fishing Pond", "You are at the edge of a small fishing pond.")
    #fishing_pond = createLocationObject(LocationID['garden_path'])

    # Connections
    LocationID['cottage'].add_connection("out", LocationID['garden_path'])
    LocationID['garden_path'].add_connection("west", LocationID['cliff'])
    LocationID['garden_path'].add_connection("south", LocationID['fishing_pond'])    

    # Items that you can pick up
    fishing_pole = Item("pole", "a fishing pole", "A SIMPLE FISHING POLE.", start_at=LocationID['cottage'])
    potion = Item("potion", "a poisonous potion", "IT'S BRIGHT GREEN AND STEAMING.", start_at=LocationID['cottage'], take_text='As you near the potion, the fumes cause you to faint and lose the game. THE END.', end_game=True)
    rosebush = Item("rosebush", "a rosebush", "THE ROSEBUSH CONTAINS A SINGLE RED ROSE.  IT IS BEAUTIFUL.", start_at=LocationID['garden_path'])
    rose = Item("rose", "a red rose", "IT SMELLS GOOD.",  start_at=None)
    fish = Item("fish", "a dead fish", "IT SMELLS TERRIBLE.", start_at=None)

    # Add blocks
    LocationID['cottage'].add_block("out", "You cannot go out of the house without taking an item inside.", preconditions={"inventory_contains":fishing_pole})

    # Sceneary (not things that you can pick up)
    pond = Item("pond", "a small fishing pond", "THERE ARE FISH IN THE POND.", start_at=LocationID['fishing_pond'], gettable=False)

    # Add special functions to your items
    rosebush.add_action("pick rose",  add_item_to_inventory, (rose, "You pick the lone rose from the rosebush.", "You already picked the rose."))
    rose.add_action("smell rose",  describe_something, "It smells sweet.")
    pond.add_action("catch fish",  describe_something, ("You reach into the pond and try to catch a fish with your hands, but they are too fast."))
    pond.add_action("catch fish with pole",  add_item_to_inventory, (fish, "You dip your hook into the pond and catch a fish.","You weren't able to catch another fish."), preconditions={"inventory_contains":fishing_pole})
    fish.add_action("eat fish",  end_game, ("That's disgusting! It's raw! And definitely not sashimi-grade! But you've won this version of the game. THE END."))

    return Game(LocationID['cottage'])

def game_loop():
    game = build_game()
    parser = Parser(game)
    game.describe()

    command = ""
    while not (command.lower() == "exit" or command.lower == "q"):
        command = input(">")
        end_game = parser.parse_command(command)
        if end_game:
            return

game_loop()
print('THE GAME HAS ENDED.')