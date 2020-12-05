import webbrowser
import pyttsx3
import os
from youtube_search import YoutubeSearch  # pip install youtube_search
import speedtest  # pip install speedtest-cli
import wikipedia
import subprocess
import speech_recognition as sr
# import datetime
import random

##############################################################################################################################################
##############################################################################################################################################


def speak(audio):
    engine = pyttsx3.init()
    #voices = engine.getProperty('voices')
    engine.setProperty(
        'voice', "HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Speech\\Voices\\Tokens\\TTS_MS_EN-US_ZIRA_11.0")
    engine.say(audio)
    engine.runAndWait()

##############################################################################################################################################
##############################################################################################################################################


def ai_assist():

    if ('play' in a) or ('listen' in a) or ('music' in a):
        try: 
        # extracting and storing search results in dictionary
            if ('play' in a):
                results = a.replace("play", "")
                results = YoutubeSearch(results, max_results=1).to_dict()
            elif ('listen' in a) or ('music' in a):
                speak('Enter the name of song you want to play: ')
                print('Taking Input: ')
                music = input()
                results = YoutubeSearch(music, max_results=1).to_dict()
            x = results[0]  # storing 1st dictionary of results from array
            url = 'https://www.youtube.com/watch?v='
            webbrowser.open_new_tab(url+x['id'])   # acessing id in x
        except:
            speak("Unable to play, Please check your connection and try again...")

    elif (('open' in a) or ('launch' in a)) and ('youtube' in a):
        url = 'https://www.youtube.com/'
        webbrowser.open_new_tab(url)

    # elif (('open' in a) or ('launch' in a)) and ('telegram' in a):
    #     url = 'https://web.telegram.org/#/login'
    #     webbrowser.open_new_tab(url)

    elif (('open' in a) or ('launch' in a)) and (('insta' in a) or ('instagram' in a)):
        url = 'https://www.instagram.com/'
        webbrowser.open_new_tab(url)

    elif (('open' in a) or ('launch' in a)) and (('fb' in a) or ('facebook' in a)):
        url = 'https://www.facebook.com/'
        webbrowser.open_new_tab(url)

    elif (('open' in a) or ('launch' in a)) and ('linkedin' in a):
        url = 'https://www.linkedin.com/login'
        webbrowser.open_new_tab(url)

    elif (('open' in a) or ('launch' in a)) and (('word' in a) or ('ms word' in a)):
        os.system('start winword')
        speak('Launching word')

    elif (('open' in a) or ('launch' in a)) and (('excel' in a) or ('ms excel' in a)):
        os.system('start excel')
        speak('Launching excel')

    elif (('open' in a) or ('launch' in a)) and (('ppt' in a) or ('ms powerpoint' in a) or ('powerpoint' in a)):
        os.system('start powerpnt')
        speak('Launching powerpoint')

    elif (('open' in a) or ('launch' in a)) and (('outlook' in a) or ('ms outlook' in a)):
        os.system('start outlook')
        speak('Launching outlook')

    elif (('open' in a) or ('launch' in a)) and (('onenote' in a) or ('ms onenote' in a)):
        os.system('start onenote')
        speak('Launching onenote')

    elif (('open' in a) or ('launch' in a)) and (('access' in a) or ('ms access' in a)):
        os.system('start MSACCESS')
        speak('Launching ms access')

    elif (('open' in a) or ('launch' in a)) and ('skype' in a):
        os.system('start skype')
        speak('Launching skype')

    elif ('shutdown' in a) or ('turnoff' in a):
        speak('Ok Sure thing. Bye Bye')
        # 1 here refers the seconds to force apps close and shutdown
        os.system("shutdown /s /t 1")
        exit()

    elif (('speed' in a) or ('speedtest' in a) or ('speed test' in a)) and (('internet' in a) or ('net' in a) or ('connection' in a) or ('speedtest' in a) or ('speed test' in a)):
        try:
            threads = None
            s = speedtest.Speedtest()
            speak('Performing speed test for you')
            s.get_best_server()
            down = (s.download(threads=threads))/1024000
            up = (s.upload(threads=threads))/1024000
            speak('Here are the results')
            print("Download: " + str(int(down)) + " Mbps")
            print("Upload: " + str(int(up)) + " Mbps")
        except:
            speak('Unable to perform speedtest, make sure you are connected to a network')

    elif (('open' in a) or ('launch' in a)) and ('paint' in a):
        speak('Launching paint')
        os.system('start mspaint')

    elif (('open' in a) or ('launch' in a)) and (('chrome' in a) or ('google chrome' in a)):
        speak('Launching chrome')
        os.system('start chrome')

    elif (('open' in a) or ('launch' in a)) and (('edge' in a) or ('microsoft edge' in a)):
        speak('Launching microsoft edge')
        os.system('start msedge')

    elif (('open' in a) or ('launch' in a)) and (('visual studio code' in a) or ('vs code' in a) or ('code' in a)):
        speak('Launching vs code')
        os.system('start code')

    elif (('open' in a) or ('launch' in a)) and (('visual studio community' in a) or ('vs community' in a) or ('community' in a)):
        speak('Launching vs community')
        os.system('start devenv')

    elif (('open' in a) or ('launch' in a)) and ('steam' in a):
        speak('Launching steam')
        os.system('start steam://open/console')

    elif (('open' in a) or ('launch' in a)) and ('discord' in a):
        speak('Launching discord')
        os.system('start discord://open/console')

    elif ('exit' in a) or ('quit' in a) or ('terminate' in a) or ('close' in a) or ('bye' in a) or ('nothing' in a) or ('nope' in a) or ('no' in a):
        speak('Sure thing. Have a great Day...')
        exit()

    elif (('open' in a) or ('launch' in a)) and ('task manager' in a):
        speak('Launching task manager')
        os.system('start taskmgr')

    #######################################################################################
    ###############                      Windows apps                      ###############

    elif (('open' in a) or ('launch' in a)) and ('mail' in a):
        speak('Launching mail')

        subprocess.Popen(
            'explorer.exe shell:appsFolder\\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.mail')

    elif (('open' in a) or ('launch' in a)) and ('camera' in a):
        speak('Launching camera')
        subprocess.Popen(
            'explorer.exe shell:appsFolder\\explorer.exe shell:appsFolder\\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.mail!App')

    elif (('open' in a) or ('launch' in a)) and (('whatsapp' in a) or ('what apps' in a) or ('whats app' in a)):
        speak('Launching whatsapp desktop')
        subprocess.Popen(
            'explorer.exe shell:appsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!WhatsAppDesktop')

    elif (('open' in a) or ('launch' in a)) and ('telegram' in a):
        speak('Launching telegram desktop')
        subprocess.Popen(
            'explorer.exe shell:appsFolder\\TelegramMessengerLLP.TelegramDesktop_t4vj0pshhgkwm!Telegram.TelegramDesktop.Store')

    elif (('open' in a) or ('launch' in a)) and ('your phone' in a):
        speak('Launching your phone')
        subprocess.Popen(
            'explorer.exe shell:appsFolder\\Microsoft.YourPhone_8wekyb3d8bbwe!App')

    elif (('open' in a) or ('launch' in a)) and (('whiteboard' in a) or ('white board' in a)):
        speak('Launching whiteboard')
        subprocess.Popen(
            'explorer.exe shell:appsFolder\\Microsoft.Whiteboard_8wekyb3d8bbwe!Whiteboard')

    elif (('open' in a) or ('launch' in a)) and (('store' in a) or ('microsoft store' in a)):
        speak('Launching microsoft store')
        subprocess.Popen(
            'explorer.exe shell:appsFolder\\Microsoft.WindowsStore_8wekyb3d8bbwe!App')

    #######################################################################################

    else:
        speak('Inappropriate Command!!')


##############################################################################################################################################
##############################################################################################################################################

def speechCommand():
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        # r.pause_threshold = 1
        # r.energy_threshold = 1500
        audio = r.listen(source)
           
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("say anything else please")
        return "None"
    return query

##############################################################################################################################################
##############################################################################################################################################

def taskill():

    if ('chrome' in a):
        speak('terminating chrome')
        os.system('taskkill /F /IM chrome.exe')

    elif ('word' in a) or ('ms word' in a):
        speak('terminating word')
        os.system('taskkill /F /IM  winword.exe')

    elif ('excel' in a) or ('ms excel' in a):
        speak('terminating excel')
        os.system('taskkill /F /IM  excel.exe')

    elif ('ppt' in a) or ('ms powerpoint' in a) or ('powerpoint' in a):
        speak('terminating powerpoint')
        os.system('taskkill /F /IM  powerpnt.exe')

    elif ('outlook' in a) or ('ms outlook' in a):
        speak('terminating outlook')
        os.system('taskkill /F /IM  outlook.exe')

    elif ('onenote' in a) or ('ms onenote' in a):
        speak('terminating onenote')
        os.system('taskkill /F /IM  onenote.exe')

    elif ('access' in a) or ('ms access' in a):
        speak('terminating ms access')
        os.system('taskkill /F /IM  MSACCESS.exe')

    elif ('skype' in a):
        speak('terminating skype')
        os.system('taskkill /F /IM  skype.exe')

    elif ('visual studio community' in a) or ('vs community' in a) or ('community' in a):
        speak('terminating vs community')
        os.system('taskkill /F /IM  devenv.exe')

    elif ('visual studio code' in a) or ('vs code' in a) or ('code' in a):
        speak('terminating vs code')
        os.system('taskkill /F /IM  code.exe')

    elif ('whatsapp desktop' in a or 'whatsapp' in a):
        speak('terminating whatsapp desktop')
        os.system('taskkill /F /IM  whatsapp.exe')

    elif ('telegram desktop' in a):
        speak('terminating telegram desktop')
        os.system('taskkill /F /IM telegram.exe')

    elif ('discord' in a):
        speak('terminating discord')
        os.system('taskkill /F /IM  discord.exe')


##############################################################################################################################################
##############################################################################################################################################

def wikiSearch(a):

    if ('tell me about' in a):
        results = a.replace("tell me about", "")
    elif ('wikipedia' in a):
        results = a.replace("wikipedia", "")
    elif ('who is' in a):
        results = a.replace("who is", "")

    speak('Searching about     ' + results)

    wikiReply = wikipedia.summary(results, sentences=2)

    print("According to wikipedia, " + wikiReply)
    speak('According to wikipedia,' + wikiReply)

##############################################################################################################################################
##############################################################################################################################################


if __name__ == "__main__":

    os.system('cls')

    speak('Hey! How are you? ')
    # print('taking input....')
    
    while True:

        print('taking input....')
        a = speechCommand()
        a = a.lower()

        if ('don\'t' in a) or ('do not' in a) or ('don\'t want to' in a) or ('dont' in a):
            speak('Sure, i won\'t do that...')
            speak("Anything else you want me to do?")

        elif ('kill' in a):
            taskill()
            speak("Anything else you want me to do?")

        elif ("tell me about" in a) or ("wikipedia" in a) or ("who is" in a):
            wikiSearch(a)
            speak("Anything else you want me to do?")

        elif('fine' in a) and ('about you' in a) or ('how are you' in a):
            reply1 = "I am fine too..."
            reply2 = "Just lazinG around with internet"
            reply3 = "Enjoying the day"
            vars = [reply1, reply2, reply3]
            speak(random.sample(vars, 1))
            speak('How may I help you?')

        elif ('fine' in a):
            speak('as expected...')
            speak('How may I help you?')

        else:
            ai_assist()
            speak("........Anything else you want me to do?")
