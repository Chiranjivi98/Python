import speech_recognition as sr

r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Anything:")
    audio = r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("You said:{}".format(text))
    except:
        print("Sorry could not recognize what you said")

#py -3 -m pipwin install pyaudio=>install these on your cmd
# py -3 -m pip install pipwin
