from googletrans import Translator



#Translation Code
def getTranslation(text, scLanguage='bn', dtLanguage='en'):
    #initiate translation
    translator = Translator()

    translated = translator.translate(text, src=scLanguage, dest=dtLanguage)
    
    return translated.text