from dotenv import load_dotenv
import os
import openai
from bardapi import BardCookies, Bard
import tts as tts
import translate as translate
import player as play
import pygame


load_dotenv()

def getAssisted(Query,sourceLang):

    #First translate from bengali to english language
    print("Translating...")
    translatedQuery = translate.getTranslation(Query, sourceLang, os.getenv('ASSIST_LANG'))
    print(f"Translated query: {translatedQuery}")    
    print("Sending query for assistance...")

    #Concat string to make sure response is in text format
    translatedQuery = translatedQuery + ', in detailed text form, no shorthand'

    message = translatedQuery

    #Get reply from Bard
    reply = assistAIEngine(message)

    #Replace * with blank
    reply = reply.replace('*','')
    
    urlInText = play.Find(reply)
    
    if urlInText:
        for urls in urlInText:
            play.palyVideo(urls)
    else:    
        print(f"Reply: {reply}")

        print("Translating reply to source language...")
        #Second translate reply from english to bengali language
        translatedReply = translate.getTranslation(reply, os.getenv('ASSIST_LANG'), sourceLang)

        print(f"Assistance: {translatedReply}")
        # messages.append({"role": "assistant", "content": translatedReply})

        #Text to speech
        pygame.init()
        pygame.mixer.init()
        tts.speak(translatedReply, sourceLang)



#Ai assistance (Currently using BARD, optional OPENAI)
def assistAIEngine(message):
    #Set bard Cookie dictionaryAssist
    cookie_dict = {
        "__Secure-1PSID": os.getenv('GOOGLE_BARD_SECURE_1PSID'),
        "__Secure-1PSIDTS": os.getenv('GOOGLE_BARD_SECURE_1PSIDTS'),
        "__Secure-1PSIDCC": os.getenv('GOOGLE_BARD_SECURE_1PSIDCC')
    }

    #Set BARD cookies and generate instance
    bard = BardCookies(cookie_dict=cookie_dict)
    #Get answers from BARD AI
    reply = bard.get_answer(str(message))['content']

    #If choice is assist then call OpenAI API to collect information
    # messages = [ {"role": "system", "content": "You are an intelligent assistant."} ]

    # openai.api_key = os.getenv('OPENAI_APIKEY')
    # if message:
    #     messages.append(
    #         {"role": "user", "content": message},
    #     )
    #     chat = openai.ChatCompletion.create(
    #         model="gpt-3.5-turbo", messages=messages
    #     )
    # reply = chat.choices[0].message.content

    return reply