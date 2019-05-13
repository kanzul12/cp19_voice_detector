import speech_recognition as sr
import webbrowser as wb 

r = sr.Recognizer()

with sr.Microphone() as source: 
    print('say something')
    audio =r.listen(source)
    print('done')
   
try:
    text = r.recognize_google(audio)
    print('google think you said:\n'+text)
            
except Exception as e: 
    print(e)

