
import random

class DeckShuffler:
    
    def __init__(self, deck):
        self.deck = deck
        
    def shuffle_deck(self, name ='', birthday ='', star_sign = '', question = ''):
                
        num_of_shuffles = len(name) + len(birthday) + len(star_sign) + len(question) + 1
        
        for i in range(num_of_shuffles):
            random.shuffle(self.deck)
            
    def get_deck(self):
        return self.deck