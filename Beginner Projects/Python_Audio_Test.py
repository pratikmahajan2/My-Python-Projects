import os
import time
import googletrans
import playsound
import speech_recognition as sr
from gtts import gTTS
from googletrans import Translator
languageDict = googletrans.LANGUAGES
# print(languageDict)

def getSrcLang(languageDict):
    src_key = ""
    while True:
        src_lang = input("Please enter the source language: ")
        print(src_lang)
        for key, value in languageDict.items():
            # print(value)
            if value == src_lang:
                src_key = key
                # print(src_key)
                return src_key
        if src_key == "":
            print("Invalid Language")

def getToLang(languageDict):  
    to_key = ""      
    while True:
        to_lang = input("Please enter the destination language: ")
        for key, value in languageDict.items():
            if value == to_lang:
                to_key = key
                # print(to_key)
                return to_key
        if to_key == "":
            print("Invalid language")
    
    # return (src_key, to_key)
        



def speak(text,to_lang):
    tts = gTTS(text=text, lang=to_lang)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.2)
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception: " + str(e))
    return said    

fromLang = getSrcLang(languageDict)
destLang = getToLang(languageDict)
# speak("Hello. What is your name")
translator = Translator()
intro = translator.translate("please Say something",src="en",dest=fromLang).text
print(intro)
speak(intro,destLang)

text1 = get_audio()
# translator = Translator()
newText = translator.translate(text1,src=fromLang,dest=destLang).text
print(newText)
speak(newText,destLang)
