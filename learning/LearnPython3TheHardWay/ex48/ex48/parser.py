#import lexicon #This work fine with running the module file as python, but not work with Nosetests : ModuleNotFoundError: No module named 'lexicon'
#from ex48 import lexicon #Why I cannot do this if I call parser.py directly in the current directory, there will be error like ModuleNotFoundError: No module named 'ex48'. But it works fine with Nosetests
import ex48.lexicon as lexicon # This works fine for both cases: Running parser.py directly and running via Nosetests
#from . import lexicon # This works fine too
#absolute & relative import?

class ParserError(Exception):
    """
    Error if:
    there are more than 1 subject, verb, or object (or the sentence contain no verb, or no object)
    In case there is no subject, implicit set the subject to "player"
    """
    #print("Give me another command(s) please!")
    print(Exception)
    
class Sentence(object):
    def __init__(self, subject, verb, obj):
        self.subject = subject[1]
        self.verb = verb[1]
        self.obj = obj[1]

def parse(sentence): # Tam implementation
    result = lexicon.scan(sentence)
    print(result)
    sentenceObject = "sentenceObject"
    sentenceVerb = "sentenceVerb"
    for pairOfWord in result:
        print(pairOfWord)
        if pairOfWord[0] == "nouns":
            sentenceObject = pairOfWord[1]
        elif pairOfWord[0] == "verbs":
            sentenceVerb = pairOfWord[1]
    FinalSentence = Sentence(None, sentenceVerb, sentenceObject)
    
    if (FinalSentence.verb, FinalSentence.obj) == ("go", "cabinet"):
        print("YOU WIN THE GAME")
    return FinalSentence

def peek(word_list):
    if word_list:
        word = word_list[0]
        return word[0]
    else:
        return None

def match(word_list, expecting): #<Tam> Do we really need the expecting?
    if word_list:
        word = word_list.pop(0)

        if word[0] == expecting:
            return word
        else:
            return None
    else:
        return None

def skip(word_list, word_type):
    while peek(word_list) == word_type:
        match(word_list, word_type)

def parse_verb(word_list):
    skip(word_list, 'stop')

    if peek(word_list) == 'verb':
        return match(word_list, 'verb')
    else:
        raise ParserError("Expected a verb next.")

def parse_object(word_list):
    skip(word_list, 'stop')

    next_word = peek(word_list)
    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'direction':
        return match(word_list, 'direction')
    else:
        raise ParserError("Expected a noun or direction next.")

def parse_subject(word_list):
    skip(word_list, 'stop')
    next_word = peek(word_list)

    if next_word == 'noun':
        return match(word_list, 'noun')
    elif next_word == 'verb':
        return ('noun', 'player')
    else:
        raise ParserError("Expect a verb next.")

def parse_sentence(word_list):
    subj = parse_subject(word_list)
    verb = parse_verb(word_list)
    obj = parse_object(word_list)

    return Sentence(subj, verb, obj)


#parse("I want to take my wife with me to go to the cabinet")