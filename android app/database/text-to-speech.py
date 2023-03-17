import pyttsx3
engine= pyttsx3.init()
while True:
    txt = input('What do you want me to say?')
    if txt != '':
        engine.say(txt)
        engine.runAndWait()
    else:
        break
