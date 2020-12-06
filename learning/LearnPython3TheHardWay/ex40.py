#ex40.py

class Song(object):
    abc = 5
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

    def print_self(self):
        print(self.abc)

happy_bday = Song(["Happy birthday to you", 
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally arround tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()
bulls_on_parade.sing_me_a_song()

#Tam code
tam_list_of_song = ["Nothing's gonna change my love for you",
                    "I swear",
                    "My love",
                    "Kiep ve sau"]
tam_song = Song(tam_list_of_song)
tam_song.sing_me_a_song()
tam_song.abc = 6
tam_song.print_self()
bulls_on_parade.print_self()