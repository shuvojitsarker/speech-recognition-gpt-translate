import pyttsx3
from gtts import gTTS
from io import BytesIO
import pygame
import time

#Convert text to speech
def textToSpeechReply(reply):
    # init function to get an engine instance for the speech synthesis
    engine = pyttsx3.init()
    
    #Get the engine voices
    voices = engine.getProperty('voices')

    #Set the engine voice as Hindi
    engine.setProperty("voice", voices[1].id)

    #Ask engine to speak the reply
    engine.say(reply)

    #Run engine and wait
    engine.runAndWait()

def wait():
    while pygame.mixer.get_busy():
        time.sleep(1)
        
def speak(text, language='bn'):
    ''' speaks without saving the audio file '''
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    sound = pygame.mixer.Sound(mp3_fo)
    sound.play()
    wait()