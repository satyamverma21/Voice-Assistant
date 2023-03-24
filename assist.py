
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia as wiki 
import smtplib
import webbrowser
from fnmatch import fnmatch


engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice' , voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour < 12 :
        speak("Good morning!!")
        
    elif hour>=12 and hour < 18 : 
        speak("good Afternoon!!")
        
    else:
        speak("Good evening!!")
        
    speak("I am Albus Dumbuldore  ... Help is always be given at hogwards who deserves it.  what do you want,,,")

         
         
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source : 
        print('listening....')
        r.pause_threshold =  1
        audio = r.listen(source)
        
    try : 
        print('Recognising...')
        query = r.recognize_google(audio , language='en-in')  
        print(f"user said :-> {query} ")      
    except Exception as e : 
        print("Say that again please ...")
        return 'none'
    return query
    
    
def sendEmail(to , content):
    server = smtplib.SMTP('smntp.mail.com' , 587)
    server.ehlo()
    server.starttls()
    server.login('emial'  , 'pass')
    server.sendmail("my email" , to   , content )
    server.close()

    
        
if __name__ == '__main__':
    # wishMe()
    # takeCommand()
    
    while True : 
        query = takeCommand().lower()
        
        if fnmatch(query , '*wiki*'):
            speak(" Seaching on wikipedia - ")
            query = query.replace("wiki","-")
            query = query.replace("-pedia","")
            print("wiki --> ",  speak)
            results = wiki.summary(query , sentences = 2 )
            
            speak("thats what i found : ")
            speak(results)
            
        elif 'open youtube' in query : 
            webbrowser.open("youtube.com")
            
        elif "open google" in query : 
            webbrowser.open("youtube.com")
            
        elif 'play music' in  query :
            '''
            
            code to play music
            
            '''
            
        elif 'time' in  query :
            '''
            
            code to time
            
            '''
        
        elif ' code' in  query :
            '''
            
            code to code
            
            '''
        elif ' emai' in  query :
            '''
            use try except 
            code to email 
            
            takecommand 
            sendemial(to  ,  contant)
            print(email send)
            
            '''
        
            
        else :
            print("nope..")
















