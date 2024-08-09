import speech_recognition as sr
import webbrowser
import pyttsx3
recognizer = sr.Recognizer()
engine = pyttsx3.init()
import musicLibrary
import requests

newsapi = "3ecc6450bcd447c38551b653337d17db"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
    if "open google" in c.lower():
        speak("Opening Google Sir")
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        speak("Opening Youtube Sir")
        webbrowser.open("https://www.youtube.com")
    elif "open Linkedin" in c.lower():
        speak("Opening Linkedin Sir")
        webbrowser.open("https://www.linkedin.com")
    elif "play" in c.lower():
        song = c.lower()[5:].strip()
        link = musicLibrary.music[song]
        speak("Yes Maharaj Playing the song ")
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            #parse The Json Response
            data = r.json()
            #extract the articles
            articles = data.get('articles',[])
            #print headlines
            for article in articles:
                print(article['title'])
                speak(article['title'])
    else:
        #Let Openai handle the request
        pass
if __name__=="__main__":
    speak("Initializing Victoria")
    while True:
        #listen for the wake word hoosier
        #obtain audio from the microphone
        r = sr.Recognizer()
        print("Recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout=2,phrase_time_limit=2)
            word = r.recognize_google(audio)
            if(word.lower()=="victoria"):
                 speak("Yes Sunny Maharaj")
                #Listen for Command
                 with sr.Microphone() as source:
                    print("Victoria Active...")
                    audio = r.listen(source, timeout=2,phrase_time_limit=2)
                    command = r.recognize_google(audio)
                    processCommand(command)
                
        except Exception as e:
            print("Error; {0}".format(e))
