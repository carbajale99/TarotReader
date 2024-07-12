import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
class ReadingGenerator:
    
    def __init__(self):
        
        GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

        genai.configure(api_key=GOOGLE_API_KEY)

        self.model = genai.GenerativeModel('gemini-1.5-pro')

    def generate_reading(self, cards, subject):
        if len(subject) == 0:
            response = self.model.generate_content("Given these tarot cards:" + cards + ". Give me a tarot reading for the day")
        else:
            response = self.model.generate_content("Given these tarot cards:" + cards + ". Given this subject are:" + subject +  ". Give me a tarot reading for the day")
       
        return response.text 


