#ex43.py Basic Object-Oriented Analysis and design
# The analysis of a Simple Game Engine
def Tam_Test():
    pass#TamTodo

class Scene(object):
    def enter(self):
        pass#TamTodo

class Engine(object):
    def __init__(self, scene_map):
        pass#TamTodo
    def play(self):
        pass#TamTodo

class Death(Scene):
    def enter(self):
        pass#TamTodo

class CentralCorridor(Scene):
    def enter(self):
        pass#TamTodo

class LaserWeaponArmony(Scene):
    def enter(self):
        pass#TamTodo

class Map(object):
    def __init__(self, start_scene):
        pass#TamTodo
    def get_scene(self, scene_name):
        pass#TamTodo
    def opening_scene(self):
        pass#TamTodo

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()