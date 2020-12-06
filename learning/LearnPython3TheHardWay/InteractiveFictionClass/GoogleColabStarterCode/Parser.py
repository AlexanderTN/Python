class Parser:
    """The Parser is the class that handles the player's input.  The player 
    writes commands, and the parser performs natural language understanding
    in order to interpret what the player intended, and how that intent
    is reflected in the simulated world. 
    """
    def __init__(self, game):
        # A list of all of the commands that the player has issued.
        self.command_history = []
        # A pointer to the game.
        self.game = game

    def get_player_intent(self,command):
        command = command.lower()
        if "," in command:
            # Let the player type in a comma separted sequence of commands
            return "sequence"
        elif self.get_direction(command):
            # Check for the direction intent
            return "direction"
        elif command.lower() == "look" or command.lower() == "l":
            # when the user issues a "look" command, re-describe what they see
            return "redescribe"
        elif "examine " in command or command.lower().startswith("x "):
            return "examine"
        elif  "take " in command or "get " in command:
            return "take"
        elif "drop " in command:
            return "drop"
        elif "inventory" in command or command.lower() == "i":
            return "inventory"
        else: 
            for item in self.game.get_items_in_scope():
                special_commands = item.get_commands()
                for special_command in special_commands:
                    if command == special_command.lower():
                        return "special"

    def parse_command(self, command):
        # add this command to the history
        self.command_history.append(command)

        # By default, none of the intents end the game. The following are ways this
        # flag can be changed to True.
        # * Going to a certain place.
        # * Entering a certain special command
        # * Picking up a certain object.

        end_game = False

        # Intents are functions that can be executed
        intent = self.get_player_intent(command)
        if intent == "direction":
            end_game = self.go_in_direction(command)
        elif intent == "redescribe":
            self.game.describe()
        elif intent == "examine":
            self.examine(command)
        elif intent == "take":
            end_game = self.take(command)
        elif intent == "drop":
            self.drop(command)
        elif intent == "inventory":
            self.check_inventory() #Tam: Actually there is no usage of the command in here, so I will remove it out of the parameters list passed in the function, old: self.check_inventory(command)
        elif intent == "special":
            end_game = self.run_special_command(command)
        elif intent == "sequence":
            #end_game = self.execute_sequence(command)
            self.execute_sequence(command) #Tam3 change it as this function dont return value
        else:
            print("I'm not sure what you want to do.")
        return end_game

    ### Intent Functions ###

    def go_in_direction(self, command):
        """ The user wants to in some direction """
        direction = self.get_direction(command)

        if direction:
            if direction in self.game.curr_location.connections:
                if self.game.curr_location.is_blocked(direction, self.game):
                    # check to see whether that direction is blocked.
                    print(self.game.curr_location.get_block_description(direction))
                else:
                    # if it's not blocked, then move there 
                    self.game.curr_location = self.game.curr_location.connections[direction]

                    # If moving to this location ends the game, only describe the location
                    # and not the available items or actions.
                    if self.game.curr_location.end_game:
                        self.game.describe_current_location()
                    else:
                        self.game.describe()
            else:
                print("You can't go %s from here." % direction.capitalize())
        return self.game.curr_location.end_game

    def check_inventory(self): #Tam: Actually there is no usage of the command in here, so I will remove it out of the parameters list passed in the function, old: def check_inventory(self,command):
        """ The player wants to check their inventory"""
        if len(self.game.inventory) == 0:
            print("You don't have anything.")
        else:
            descriptions = []
            for item_name in self.game.inventory:
                item = self.game.inventory[item_name]
                descriptions.append(item.description)
            print("You have: ", end = '')
            print(*descriptions, sep = ", ",)
  

    def examine(self, command):
        """ The player wants to examine something """
        command = command.lower()
        matched_item = False
        # check whether any of the items at this location match the command
        for item_name in self.game.curr_location.items:
            if item_name in command:
                item = self.game.curr_location.items[item_name]
                if item.examine_text:
                    print(item.examine_text)
                    matched_item = True
                break
        # check whether any of the items in the inventory match the command
        for item_name in self.game.inventory:
            if item_name in command:
                item = self.game.inventory[item_name]
                if item.examine_text:
                    print(item.examine_text)
                    matched_item = True
        # fail
        if not matched_item:
            print("You don't see anything special.")


    def take(self, command):
        """ The player wants to put something in their inventory """
        command = command.lower()
        matched_item = False

        # This gets set to True if posession of this object ends the game.
        end_game = False

        # check whether any of the items at this location match the command
        for item_name in self.game.curr_location.items:
            if item_name in command:
                item = self.game.curr_location.items[item_name]
                if item.gettable:
                    self.game.add_to_inventory(item)
                    self.game.curr_location.remove_item(item)
                    print(item.take_text)
                    end_game = item.end_game
                else:
                    print("You cannot take the %s." % item_name)
                matched_item = True
                break
        # check whether any of the items in the inventory match the command
        if not matched_item:
            for item_name in self.game.inventory:
                if item_name in command:
                    print("You already have the %s." % item_name)
                    matched_item = True
        # fail
        if not matched_item:
            print("You can't find it.")

        return end_game

    def drop(self, command):
        """ The player wants to remove something from their inventory """
        command = command.lower()
        matched_item = False
        # check whether any of the items in the inventory match the command
        if not matched_item:
            for item_name in self.game.inventory:
                if item_name in command:
                    matched_item = True
                    item = self.game.inventory[item_name]
                    self.game.curr_location.add_item(item_name, item)
                    self.game.inventory.pop(item_name)
                    print("You drop the %s." % item_name)
                    break
        # fail
        if not matched_item:
            print("You don't have that.")


    def run_special_command(self, command):
        """Run a special command associated with one of the items in this location
       or in the player's inventory"""
        for item in self.game.get_items_in_scope():
                special_commands = item.get_commands()
                for special_command in special_commands:
                    if command == special_command.lower():
                        return item.do_action(special_command, self.game)

    def execute_sequence(self, command):
        for cmd in command.split(","):
            cmd = cmd.strip()
            self.parse_command(cmd)
        #return 1 #Tam add to pass the error
    def get_direction(self, command):
        command = command.lower()
        if command == "n" or "north" in command:
            return "north" 
        if command == "s" or "south" in command:
            return "south"
        if command == "e" or "east" in command: 
            return "east"
        if command == "w" or "west" in command:
            return "west"
        if command == "up":
            return "up"
        if command == "down":
            return "down"
        if command.startswith("go out"):
            return "out"
        if command.startswith("go in"):
            return "in"
        for exit in self.game.curr_location.connections.keys():
            if command == exit.lower() or command == "go " + exit.lower():
                return exit
        return None