import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import pyjokes
import sys
import datetime
from datetime import date
import webbrowser

listener = sr.Recognizer()
engine = pyttsx3.init()


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
            if 'ivan' in command:
                command = command.replace('ivan', '')
                print(command)
    except:
        pass

    return command


def run_ivan():
    talk('what should i do?')
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'tell me about' in command:
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 1)
        talk('i found this from Wikipedia that ' + info)
        print('i found this from Wikipedia that ' + info)
    elif 'what is' in command:
        person = command.replace('what is', '')
        info = wikipedia.summary(person, 1)
        talk('i found this from Wikipedia that ' + info)
        print('i found this from Wikipedia that ' + info)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk('i found this from Wikipedia that ' + info)
        print('i found this from Wikipedia that ' + info)
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
        today = date.today()
        todate = today.strftime("%B /%d /%Y")
        talk('today\'s date is ' + todate)
    elif 'who are you' in command:
        talk('I am ivan, a virtual AI assistant made by Raunak Manna on 11th February 2021. i can do various work '
             'like searching and showing with just few commands')
    elif 'who made you' in command:
        talk('I am ivan, a virtual AI assistant made by Raunak Manna on 11th February 2021. i can do various work '
             'like searching and showing with just few commands')
    elif 'what can you do' in command:
        talk('I am ivan, a virtual AI assistant made by Raunak Manna on 11th February 2021. i can do various work '
             'like searching and showing with just few commands')
    elif 'How are you' in command:
        talk('I am fine, thank you')
    elif 'what\'s going on?' in command:
        talk('I am fine, thank you')
    elif 'search' in command:
        search1 = command.replace('search', '')
        new = 2
        try:
            from googlesearch import search
        except ImportError:
            print("No module named 'google' found")

        # to search
        query = search1

        for j in search(query, tld="co.in", num=1, stop=1, pause=2):
            k = j

        url = j
        talk('opening...')
        webbrowser.open(url, new=new)
    else:
        talk('i am sorry, i didn\'t get that. can you please repeat it again or you can ask with a different name.')


talk('i am ivan, your virtual A I assistant.')
while True:
    run_ivan()
