import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
from datetime import date
import wikipedia
import pyjokes
import sys
import pyowm

owm = pyowm.OWM('856efd6e8ff237af0134c0ecedf704dc')

listener = sr.Recognizer()
engine = pyttsx3.init()


def intro():
    engine.say('I am Jarvis, you Virtual ai assistant.')
    engine.say('What can i do for You?')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)

    except:
        pass
    return command


def run_jarvis():

    command = take_command()
    print(command)
    if 'play ' in command:
        song = command.replace('play ', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is ' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)
        print(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
        print(pyjokes.get_joke())
    elif 'shut down' in command:
        talk('as you wish, have a good day!')
        sys.exit()
    elif 'sleep' in command:
        talk('as you wish, have a good day!')
        sys.exit()
    elif 'don\'t disturb now' in command:
        talk('as you wish, have a good day!')
        sys.exit()
    elif 'date' in command:
        today= date.today()
        todate=today.strftime("%B /%d /%Y")
        talk('today\'s date is '+todate)
    elif 'tell me about you' in command:
        talk('I am ')

    else:
        talk('i am sorry, i didn\'t get that. can you please repeat it again or you can ask with a different name.')


while True:
    run_jarvis()
