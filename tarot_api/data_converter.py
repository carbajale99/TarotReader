import json
import pandas as pd
from deck_shuffler import DeckShuffler

class DataManager:
    
    def __init__(self):
    
        self.cards_data = []
        self.csv_file = "cards_data.csv"
        self.json_file = "raw_card_data.json"
        self.extract_json_data()
        self.deck_shuffler = DeckShuffler(self.cards_data)
        

    #extracts data from the json file
    def extract_json_data(self):
    
        with open(self.json_file, 'r') as json_data:
            self.cards_data = json.load(json_data)
            
    
    #fills csv with default data from website
    def fill_csv_default(self):
                
        default_df = pd.DataFrame(self.cards_data)
        default_df.to_csv(self.csv_file, index=False)
        
    def fill_csv_shuffled(self, name ='', birthday ='', star_sign = '', question = ''):
        
        self.deck_shuffler.shuffle_deck(name, birthday, star_sign, question)
        
        
        shuffled_df = pd.DataFrame(self.deck_shuffler.get_deck())
        shuffled_df.to_csv(self.csv_file, index=False)
        
    def get_json_data(self, name ='', birthday ='', star_sign = '', question = ''):
        self.deck_shuffler.shuffle_deck()
        
        return self.deck_shuffler.get_deck()
        
    
    def get_csv(self):
        
        try:
            return open(self.csv_file, mode='r')
        except:
            return None
