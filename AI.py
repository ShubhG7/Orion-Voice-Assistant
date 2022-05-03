import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import random
import os
import smtplib

#passwordFile = 'C:\\Users\\shubh\\OneDrive\\Documents\\Shubh Gupta\\Python\\passwordFile.txt'
chromePath = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning.")
    elif hour>=12 and hour <18:
        speak("Good Afternoon.") 
    else:
        speak("Good Evening.")
    speak("Hi I'm Orion, How may I help you?")


def sendEmail(to, content):
    # passwordFile = 'C:\\Users\\shubh\\OneDrive\\Documents\\Shubh Gupta\\Python\\passwordFile.txt'
    # os.listdir(passwordFile)
    # dotFile = open("passwordFile.txt")
    # pw= dotFile.read()
    with open("passwordFile.txt") as dotFile:
        pw = dotFile.read()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # server.login('shubhguptarm7@gmail.com', open('passwordFile.txt', 'r').readlines())
    server.login('shubhguptarm7@gmail.com', pw)
    server.sendmail('shubhguptarm7@gmail.com', to, content)
    server.close()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say Something.") 
        r.pause_threshold = 1
        audio = r.listen(source)

        
    try: 
         print("...")
         statement = r.recognize_google(audio, language = 'en-in')
         print("You said:", statement)

    except Exception as e:
        #print(e)
        print("Didn't quite get that")
        return "none"
    return statement

if __name__ == "__main__":
    wishMe()
    while True:
        statement = takeCommand().lower()
        
        if 'wikipedia' in statement:
            speak('Searching Wiki.')
            statement = statement.replace("wikipedia", "")
            result = wikipedia.summary(statement, sentences=2)
            speak('Here is what i found')
            print(result)
            speak(result)

        elif 'open youtube' in statement:
            webbrowser.get(chromePath).open("youtube.com")

        elif 'open google' in statement:

            webbrowser.get(chromePath).open("Google.com")
        elif 'open stackoverflow' in statement:
            webbrowser.get(chromePath).open("stackoverflow.com")

        elif 'play music' in statement:
            music_dir = 'C:\\Users\\shubh\\OneDrive\\Documents\\Shubh Gupta\\MusicDir'
            songs = os.listdir(music_dir)
            print("Do you want me to choose a song for you?")
            speak('Do you want me to choose a song for you?')
            ans= takeCommand().lower()
            if 'yes' in ans:
                n = random.randint(0, len(songs)-1)
                os.startfile(os.path.join(music_dir, songs[n]))
            else:
                os.startflile(os.path.join(music_dir, songs[0]))

        elif 'the time' in statement:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            speak('The time right now is', time)

        elif 'open visual studio' in statement:
            vsCode_path = "C:\\Users\\shubh\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vsCode_path)

        elif 'open rocket league' in statement:
            rocketLeague_path = "C:\\Users\\shubh\\OneDrive\\Documents\\Shubh Gupta\\Games\\Rocket League"
            os.startfile(rocketLeague_path)
        
        elif 'send email to papa' in statement:
            try: 
                speak('What should I send?')
                print("What should I Send?")
                content = takeCommand()
                to = "guptankgupta@gmail.com"
                sendEmail(to, content)
                speak('Ive sent the email')
            
            except Exception as e:
                print(e)
                speak("Sorry, I couldn't send the email")
            



        

       

