
import os
import speech_recognition as sr



r = sr.Recognizer()

with sr.Microphone() as source:
    print("Diga algo: ")
    audio = r.listen(source)
    try:
        texto=r.recognize_google(audio, language='es-ES')
        print("Esto dijiste: {}".format(texto))
        with open("audio.wav","wb") as fichero:
            fichero.write(audio.get_wav_data())
    except:
        print("Lo siento no te entendi")


