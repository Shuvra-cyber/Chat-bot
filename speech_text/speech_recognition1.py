
import speech_recognition as sr  
import os
from gtts import gTTS
from nltk.tokenize import sent_tokenize
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

conv = open('robot_text.txt','r')
sent = conv.read()
text = sent_tokenize(sent)

chatbot = ChatBot('Dan' )
trainer = ListTrainer(chatbot)

trainer.train(text)

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   
with sr.Microphone() as source:                                                                       
    print("Speak:")                                                                                   
    audio = r.listen(source)   

language = 'en'

while True:
    try:
        give = input("Say: ")
        if give == '':
            print()
            print("Have a good day")
            break
        bot_input = chatbot.get_response(give)
    
        print("bot: ",bot_input)
        print()
        
    except(KeyboardInterrupt,EOFError,SystemExit):
        break

try:
    print("You said " + r.recognize_google(audio))
    tts = gTTS(text=r.recognize_google(audio), lang='en')
    tts.save("good.mp3")
    os.system("mpg321 good.mp3")

except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
