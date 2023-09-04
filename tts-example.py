from gtts import gTTS
from io import BytesIO
import pygame
import time


def wait():
    while pygame.mixer.get_busy():
        time.sleep(4)
def speak(text, language='bn'):
    ''' speaks without saving the audio file '''
    mp3_fo = BytesIO()
    tts = gTTS(text, lang=language)
    tts.write_to_fp(mp3_fo)
    mp3_fo.seek(0)
    
    sound = pygame.mixer.Sound(mp3_fo)
    wait()
    sound.play()
    wait()
    
pygame.init()
pygame.mixer.init(frequency=555000)
wait()
if pygame.mixer.get_init():
    speak("থাকবো নাকো ")