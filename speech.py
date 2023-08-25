# import required module
import speech_recognition as sr
import openai
from googletrans import Translator


# explicit function to take input commands 
# and recognize them
def takeCommandHindi():
    openai.api_key = 'OpenAI API Key'
    translator = Translator()
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
                Query = r.recognize_google(audio, language='bn-In')
                
                # for listening the command in indian english
                print("the query is printed='", Query, "'")
                
                #Ask user for choice for assist or translate
                print("Please enter Assist for Assistance or Translate to Translate in English")
                choice = input("Enter: ")

                if choice == "Assist":
                    #First translate from bengali to english language
                    print("Translating...")
                    translated = translator.translate(Query, src='bn', dest='en')
                    print(f"Translated query: {translated.text}")    
                    print("Sending query for assistance...")

                    #If choice is assist then call OpenAI API to collect information
                    messages = [ {"role": "system", "content": "You are an intelligent assistant."} ]
                    message = translated.text
                    if message:
                        messages.append(
                            {"role": "user", "content": message},
                        )
                        chat = openai.ChatCompletion.create(
                            model="gpt-3.5-turbo", messages=messages
                        )
                    reply = chat.choices[0].message.content

                    print(f"Reply: {reply}")
                    print("Translating reply to source language...")
                    #Second translate reply from english to bengali language
                    translatedReply = translator.translate(reply, src='en', dest='bn')

                    print(f"Assistance: {translatedReply.text}")
                    messages.append({"role": "assistant", "content": translatedReply.text})

                elif choice == "Translate":
                    translated = translator.translate(Query, src='bn', dest='en')
                    print(f'{translated.origin} -> {translated.text}')

            # handling the exception, so that assistant can 
            # ask for telling again the command
            except Exception as e:
                print(e)  
                print("Say that again")
                return "None"
            #return Query

# Driver Code

# call the function
takeCommandHindi()