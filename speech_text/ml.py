import pyttsx3
import datetime
import webbrowser
import wikipedia
import os
import random
import speech_recognition as sr

#that's my engine name
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[0].id)
engine.setProperty('voice',voices[0].id)

#function for speaking
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
#this function is only for wishing
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("good morning")
    elif hour >= 12 and hour < 18:
        speak("good afternoon")
    else:
        speak("good evening")

    speak("I am David Please tell me sir how may I help you? ")
    
#I thought to use it first for text input as word
'''
query1 = input("Say some thing:")
query = query1.lower()
print("user said",query1)
'''


if __name__ == "__main__":

    wishMe()
    while True:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Speak:")
            audio = r.listen(source)

        try:
            print("recognising")
            query1 = r.recognize_google(audio)
            query = query1.lower()
            print("user said:",query)
        except sr.UnknownValueError:
            print("Could not understand audio")
            speak("I could not understand!!!")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

        if "hi" or "hello" or "aloha" in query:
            speak("Hi there. How are You? ")
            print("Hi there. How are You?")

        elif "fine" or "good" in query:
            speak("good to hear about it")

        elif "exit" in query:
            speak("Sir,I am exiting now bye")
            print("Sir,I am exiting now bye!!!")
            exit()

        elif "youtube" in query:
            webbrowser.open("youtube.com")
            speak("youtube is opened for you Sir")

        elif "google" in query:
            webbrowser.open("google.com")
            speak("google is opened for you Sir")

        elif "stackoverflow" in query:
            webbrowser.open("stackoverflow.com")
            speak("stackoverflow is opened for you Sir")

        elif "wikipedia" in query:
            speak("Searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "music" in query:
            music_dir = "D:\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[random.randint(1,70)]))

        elif "time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is{strTime}")
            print(f"Time:{strTime}")

        elif "who" in query:
            speak("i am chat bot created by shuvra")
            print("I am chat bot created by Shuvra")

        elif "atom" in query:
            code_path_atom = "C:\\Users\\DELL\\AppData\\Local\\atom\\atom.exe"
            os.startfile(code_path_atom)

        elif "whatsapp" in query:
            code_path_whatsapp = "C:\\Users\\DELL\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(code_path_whatsapp)
            speak("WhatsApp is opened for you Sir")

        else:
            speak("I could not understand!!!")
            print("I could not understand!!!")
