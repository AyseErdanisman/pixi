"""
from playsound import playsound
from gtts import gTTS
import speech_recognition as sr
import os

def speak(string):
    tts = gTTS(text=string, lang="tr", slow=False)
    file = "answer.mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)
speak("hello")
"""

from playsound import playsound
from gtts import gTTS,gTTSError
import speech_recognition as sr
import os

r  = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""

        try: 
            voice = r.recognize_google(audio, language="tr-TR")
        except sr.UnknownValueError:
            #Mikrofondan gelen sesin anlaşılmaması halinde hata mesajı döndürür.  
            print("Asistan: Anlayamadım")
        except sr.RequestError:
            #Google sunucusu veya internet kesintisi hainde hata mesajı verir.
            print("Asistan: Sistem Çalışmıyor")
        return voice

def playaudio(audio):
    playsound(audio)

def convert_to_audio(text):
    audio = gTTS(text=text, lang='tr', tld='com', slow=False)
    #dil tr olarak belirlense de ingilizce metini de okuyabiliyor
    audio.save("textaud.mp3")
    playaudio("textaud.mp3")

convert_to_audio("olur olur yeriz")
voice = record()
if voice != '':
    print(record)

if 'merhaba' in voice:
    convert_to_audio('merhaba tanıştığıma memnun oldum')
    # bu bloklar devam ettirilierek bir senaryo oluşturulabilir.


