import speech_recognition as sr
import os
import time
import subprocess

#vocie command
def listen_micro():
    #micro on
    microfone = sr.Recognizer()

    #micron using
    with sr.Microphone() as source:
        #reduce ambient noise
        microfone.adjust_for_ambient_noise(source)
        print("Diga alguma coisa: ")
        audio = microfone.listen(source)
    try:
        # write commands
        text = microfone.recognize_google(audio, language='pt-BR')
        if "navegador" in text:
            os.system("start Chrome.exe")
        if "calculadora" in text:
            os.system("start calc.exe")
        if "YouTube" in text:
            # os.system('taskkill /im chrome.exe')
            os.system('start chrome "https://www.youtube.com/watch?v=OPf0YbXqDm0&ab_channel=MarkRonsonVEVO" --kiosk')
            time.sleep(1)
        if "jogos" in text:
            jogos = r"C:\Program Files (x86)\Origin\Origin.exe"
            subprocess.check_call([jogos, '--kiosk'])
        print("Você disse: " + text)

    # miss understand sound error
    except sr.UnkownValueError:
        print("Não entendi")

    return text

while 2 > 1:
    listen_micro()
