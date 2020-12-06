#Utils.py

def check_preconditions(preconditions, game, print_failure_reasons=True):
    """Checks whether the player has met all of the specified preconditions"""
    all_conditions_met = True
    for check in preconditions: 
        if check == "inventory_contains":
            item = preconditions[check]
            if not game.is_in_inventory(item):
                all_conditions_met = False
                if print_failure_reasons:
                    print("You don't have the %s" % item.name)
        if check == "in_location":
            location = preconditions[check]
            if not game.curr_location == location:
                all_conditions_met = False
                if print_failure_reasons:
                    print("You aren't in the correct location")
        if check == "location_has_item":
            item = preconditions[check]
            if not item.name in game.curr_location.items:
                all_conditions_met = False
                if print_failure_reasons:
                    print("The %s isn't in this location" % item.name)
    # todo - add other types of preconditions
    return all_conditions_met

def add_item_to_inventory(game, *args):
    """ Add a newly created Item and add it to your inventory."""
    (item, action_description, already_done_description) = args[0]
    if(not game.is_in_inventory(item)):
                    print(action_description)
                    game.add_to_inventory(item)
    else:
                    print(already_done_description)
    return False

def describe_something(game, *args):
    """Describe some aspect of the Item"""
    (description) = args[0]
    print(description)
    return False

def destroy_item(game, *args):
    """Removes an Item from the game by setting its location is set to None."""
    (item, action_description) = args[0]
    if game.is_in_inventory(item):
                    game.inventory.pop(item.name)
                    print(action_description)
    elif item.name in game.curr_location.items:
                    game.curr_location.remove_item(item)
                    print(action_description)
    else:
                    pass#print(already_done_description)
    return False

def end_game(game, *args):
    """Ends the game."""
    end_message = args[0]
    print(end_message)
    return True