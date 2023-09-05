from googletrans import Translator
from dotenv import load_dotenv
import os

load_dotenv()

#Translation Code
def getTranslation(text, scLanguage, dtLanguage=os.getenv('ASSIST_LANG')):
    #initiate translation
    translator = Translator()

    translated = translator.translate(text, src=scLanguage, dest=dtLanguage)
    
    return translated.text