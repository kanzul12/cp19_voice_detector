import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    audio=r.listen(source)
try:
    print("transcription: "+r.recognize_google(audio))
except sr.UnknownValueError:
    print("audio unintelligible")
except sr.RequestError as e:
    print("cannot obtain results;{0}".format(e)) 