import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import time
import random
import pywhatkit
from requests import get
import wikipedia
import webbrowser
import smtplib
import sys
import pyjokes

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)



# ------------ speech 2 audio -------------
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


# ----------- convert voice into text ------------ 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 0.7
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print("The Query is : " + str(query))

    except Exception as e:
        speak("can't hear properly..")
        return "none"
    return query

# -----------   WISH  ------------

def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("hi iam Mrs.Minion, how can i help you")



    
# ------------- SENDING MAIL --------------


def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password')
    server.sendmail('your email id',to,content)
    server.close()


if __name__ == "__main__":
    wish()
    while True:
    
        query = takecommand().lower()

# ---------- AI LOGIC BUILDING FOR TASKS--------------

        if "open Notepad" in query:
            npath = ("C:\\Program Files\\Notepad++\\system32\\notepad.exe")
            os.startfile(npath)


        elif "open netflix" in query:
            webbrowser.open("https://www.netflix.com/in/Login")


            
        elif "who is god" in query:
            speak("i was created by NITHIN, so he is my god")



        elif "what's your name" in query:
            speak("My name is MINI1.1")



        elif "in which year you was born" in query:
            speak("i was born in the year 2020 december 12")



        elif "open flipkart" in query:
            speak("opening flipkart")
            webbrowser.open("www.flipkart.com")



        elif "open amazon" in query:
            speak("opening amazon")
            webbrowser.open("www.amazon.com")



        elif "where will you live" in query:
            speak("i will live in air where ever you want")



        elif "who are you" in query:
            speak("iam nithin's personal assistant")



        elif "how are you" in query:
            speak("I am fine sir! what about you sir?")



        elif "do you love me" in query:
            speak("No! i'm already in love")



        elif "who is nani" in query:
            speak("He is my BOSS")



        elif "open command prompt" in query:
            speak("opening cmd")
            os.system("start cmd")

            

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret,img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()


        
        elif "play music" in query:
            music_dir = "C:\\Users\\DELL\\OneDrive\\Desktop\\music"
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir,rd))




        elif "ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"your IP adress is {ip}")




        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)



        elif "open youtube" in query:
            speak("opening youtube")
            webbrowser.open("www.youtube.com")



        elif "open facebook" in query:
            speak("opening facebook")
            webbrowser.open("www.facebook.com")



        elif "open sathyabama website" in query:
            speak("opening sathyabama website")
            webbrowser.open("www.sathyabama.ac.in")


        elif "open lms sathyabama" in query:
            webbrowser.open("https://sathyabama.cognibot.in//")



        elif "open google maps" in query:
            speak("opening google maps")
            webbrowser.open("https://www.google.com/maps?cid=7579651550580939191")


        
        elif "open google" in query:
            speak("sir, what should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")



        elif "open stack overflow" in query:
            speak("opening stackover flow")
            webbrowser.open("www.stackovetflow.com")



        elif "open whatsapp" in query:
            speak("opening whatsapp")
            webbrowser.open("web.whatsapp.com")



        elif "open mail" in query:
            speak("opening mail")
            webbrowser.open("www.gmail.com")


        elif "wake up siri" in query:
            speak("i am already up")


        elif "open drive" in query:
            speak("opening drive")
            webbrowser.open("https://drive.google.com/drive/my-drive")



        elif "hello mini" in query:
            speak("hello sir, how may i help you")



        elif "play joke" in query:
            speak(pyjokes.get_joke())


        elif "play on youtube" in query:
            song = query.replace("play","")
            speak('playing' + song)
            pywhatkit.playonyt(song)


        elif "activate how to command" in query:
            speak("How to command is activated, please tell me what to do...")
            how = takecommand()
            max_results = 1
            how_to = search_wikihow(how, max_results)
            assert len(how_to) == 1
            how_to[0].print()
            speak(how_to[0].summary)




        elif "you can sleep now" in query:
            speak("ok sir, bye. If you have any need call me i will be there for you always")
            sys.exit()


        elif "no thanks" in query:
            speak("thanks for using me, have a good day.")
            sys.exit()






























