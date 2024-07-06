import pyttsx3

engine = pyttsx3.init()

engine.setProperty('rate', 150)
engine.setProperty('volume', 1)

def say(text):
    engine.say(text)
    engine.runAndWait()