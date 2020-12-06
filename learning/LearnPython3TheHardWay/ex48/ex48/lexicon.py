
directions = ["north", "south", "east", "west", "down", "up", "left", "right", "back"]
verbs = ["go", "stop", "kill", "eat"]
stop_words = ["the", "in", "to", "of", "from", "at", "it"]
nouns = ["door", "bear", "princess", "cabinet"]
numbers = [0, 1, 2, 3, 4, 5, 6 , 7, 8, 9]

def convert_number(s):
    try:
        return int(s)
    except ValueError:
        return None        

def scan(user_input):
    pass
    words = user_input.split()
    sentences = []
    for word in words:
        if word in directions:
            tp = ("direction", word)            
        elif word in verbs:
            tp = ("verbs", word)            
        elif word in stop_words:
            tp = ("stop_words", word)            
        elif word in nouns:
            tp = ("nouns", word)            
        elif convert_number(word):
            tp = ("numbers", int(word))
        else:
            tp = ("errors", word)
        #Then finally we got what we need
        sentences.append(tp)
    return sentences
        

