from playwright.sync_api import sync_playwright
import json

class TarotScraper:
    
    def __init__(self):
        
        self.cards_list = []
        self.cards = {}
        
    def scrape_cards(self):

        with sync_playwright() as pw:
            
            browser = pw.chromium.launch(
                headless=True
            )
            
            context = browser.new_context(
                # most common desktop viewport is 1920x1080
                viewport={"width": 1920, "height": 1080}
            )
            
            page = context.new_page()
            
            page.goto("https://labyrinthos.co/blogs/tarot-card-meanings-list")
            
            
            grid_cards = page.locator("//div[@class='grid__item large--one-quarter medium--one-third small--one-half text-center']")
            
            self.extract_card_data(grid_cards)
    
    
    def extract_card_data(self,grid_cards):

        for i in range(grid_cards.count()):
            
            card_grid_elemnt = grid_cards.nth(i)
        
        #checking if the card is a major arcana 
            card_element_grand_parent = card_grid_elemnt.locator("..").locator("..")
            
            grand_parent_id = card_element_grand_parent.get_attribute('id')
            
            major_arcana = False
            
            if(grand_parent_id == "majorarcana"):
                major_arcana = True
            
            #grabbing the name of the card
            name_element = card_grid_elemnt.locator(".card .card__meta h3")
            
            name_text = name_element.inner_text()
            
            filtered_name = name_text.replace(' Meaning', '')
            
            #grabbing the meaning of the card, both upright and reversed
            
            meaning_element =  card_grid_elemnt.locator(".keywords p")
            
            meaning_text = meaning_element.inner_text()
            
            removed_link =  meaning_text.replace('FULL TAROT MEANING', '')
            removed_stars = removed_link.replace('✦', '')
            removed_blank = removed_stars.replace('\xa0', '')
            removed_newline = removed_blank.replace('\n', '')
            
            meaning_split = removed_newline.split(":")
            
            upright = meaning_split[1].replace("Reversed", '').strip()
            reverse = meaning_split[2].strip()
            
            
            self.cards_list.append({'Card Name': filtered_name, 'Upright Meaning': upright, "Reversed Meaning": reverse, 'Major Arcana': major_arcana})

        self.cards['cards'] = self.cards_list


    def get_cards(self):
        return self.cards

    def load_cards(self):
        
        json_array = json.dumps(self.get_cards())
        
        with open("raw_card_data.json", "w") as outfile:
            outfile.write(json_array)
            

ts = TarotScraper()

ts.scrape_cards()

ts.load_cards()