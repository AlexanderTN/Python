#ex40a.py Just an example for comparing between a dictionary and a module
import ex40a_mystuff

mystuffdict = {'apple': "I AM APPLES!"}
print(mystuffdict['apple'])

ex40a_mystuff.apple()
print(ex40a_mystuff.tangerine)

class MyStuff(object):
    def __init__(self):
        self.tangerine = "And now a thousand years between"

    def apple(self):
        print("I AM A CLASSY APPLES!")

thing = MyStuff()
thing.apple()
print(thing.tangerine)