
import pyttsx3 # pip install pyttsx3

# Automatic recognition of human speech.
import speech_recognition as sr # pip install speechRecognition
import wikipedia  # pip install wikipedia
import datetime
import webbrowser
import os
import smtplib

# init function to get an engine instance for the speech synthesis.
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)

engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)      # say method on the engine that passing input text to be spoken.
    engine.runAndWait()    # run and wait method, it processes the voice commands.

def wishMe():
    '''It is a fuction uses to wish accordingly time'''
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak('Goooooood Morning')

    elif hour>=12 and hour < 18:
        speak('Goooooood Afternoon')

    else:
        speak("Goooooood Evening")

    speak('Hello Sir!, I am Jarvis the bottttt. Speed one terabyte, memory one zetabyte. How may I help you sir?')

def takeCommand():
    '''It takes microphone input from user and returns string output.'''
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")

    except Exception as e:
        # print(e)  # Comment it to not show error name in console
        print('Say that again please...')
        return 'None'
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password-here')
    server.sendmail('youremail@gmail.com',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    # while True:
    if 1:
        query = takeCommand().lower() 
        # .lower() converts the query into lower so that we get errorless results.

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...please wait!')
            query = query.replace('wikipedia',"")
            results = wikipedia.summary(query, sentences = 2)
            speak('Alright')
            speak('According to wikipedia')
            # print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open('youtube.com')

        elif "open google" in query:
            webbrowser.open('google.com')

        elif "open stackoverflow" in query:
            webbrowser.open('stackoverflow.com')

        
        # OR
        # sites = [['youtube','https://www.youtube.com'],['wikipedia','https://www.wikipedia.com'],
        # ['google','https://www.google.com'],['stackoverflow','https://www.stackoverflow.com']]
        
        # for site in sites:
        #     if f"Open {site[0]}".lower() in query:
        #         speak(f"Opening {site[0]} sir...")
        #         webbrowser.open({site[1]})
        
        elif 'play music' in query:
            music_dir = "add your music folder path here"
            songs = os.listdir(music_dir)
            # print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open code' in query:
            codePath = "add your code editor path here"
            os.startfile(codePath)

        elif 'quit' or 'nothing' or 'bye' in query:
            speak('Quiting sir, Thanks for your time.')
            exit()

        elif "send email" in query:
            try:
                speak('What should i say')
                content = takeCommand()
                to = 'youremailhere@gmail.com'
                sendEmail(to, content)
                speak("Email has been sent!")

            except Exception as e:
                # print(e)
                speak('Sorry my friend, I am not able to send this email')
