# import required module
import speech_recognition as sr
import translate as translate
import assist as assist
import tts as tts
import pygame
from langdetect import detect
from dotenv import load_dotenv
import os

load_dotenv()

#Specify language codes
languageCodes = {
    "English": "en",
    "Hindi": "hi-In",
    "Bengali": "bn-In"
}

# explicit function to take input commands 
# and recognize them
def takeCommandHindi():
    
    #Ask user for preferred language   
    langChoice = input("Please choose a language, English, Hindi, or Bengali: ")

    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            
            # seconds of non-speaking audio before 
            # a phrase is considered complete
            print('Listening')
            r.pause_threshold = 0.7  
            audio = r.listen(source)  
            try:
                print("Recognizing")
                Query = r.recognize_google(audio, language=languageCodes.get(str(langChoice)))
                
                # for listening the command in indian english
                print("the query is printed='", Query, "'")
                
                #Detect language of the query
                sourceLang = detect(Query)

                #Ask user for choice for assist or translate
                print("Please enter Assist for Assistance or Translate to Translate in English")
                choice = input("Enter: ")

                if choice == "Assist":
                    assist.getAssisted(Query,sourceLang)

                elif choice == "Translate":
                    translatedQuery = translate.getTranslation(Query, sourceLang, dtLanguage=os.getenv('ASSIST_LANG'))
                    print(f'{translatedQuery}')
                    
                    #Text to speech in source language
                    pygame.init()
                    pygame.mixer.init()
                    tts.wait()
                    tts.speak(Query, sourceLang)

            # handling the exception, so that assistant can 
            # ask for telling again the command
            except Exception as e:
                print(e)  
                print("Say that again")
                return "None"
            #return Query



# call the function
takeCommandHindi()