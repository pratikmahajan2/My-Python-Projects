''' 
=====================================================================================================================
Project    - Portable Language Translator - Voice based using googletrans and text to speech API
Programmer - Pratik Mahajan
Contact    - pratikmahajan2@gmail.com
Date       - 25 - Jul - 2021

Project Description:
====================
In this project, I will be utilizing googletrans API to perform audio translation from source language to desired
language. 
User will be prompted to enter a source language first. The program validates the source language against supported
language pool. If valid, user will then be asked to enter "TO" language, which will again be validated. If valid, 
user will be able to speak in source language, which will then be translated and announced in desired language.  

Version Log:
=============================================
25 - Jul - 2021 - Pratik M. - Initial Version
=============================================
=====================================================================================================================
'''
#import packages required
import os
from googletrans import Translator
import googletrans
from datetime import datetime
import speech_recognition as sr
from gtts import gTTS
import playsound
#====================================================================================================================
#fetch dictionary of supported language from googletrans
masterLanguageDict = googletrans.LANGUAGES
# print(masterLanguageDict)
#====================================================================================================================
#Function to drive the main logic of the code
def mainDriver():

    displayMessages()
    fromLanguage, fromLangCode = userChoice("from")
    # print(fromLanguage)
    toLanguage, toLangCode = userChoice("to")
    # print(toLanguage)

    initiateTranslation(fromLanguage, fromLangCode, toLanguage, toLangCode)

#====================================================================================================================
#Function to initiate the translator

def initiateTranslation(fromLanguage, fromLangCode, toLanguage, toLangCode):

    inputText = translateText(f"Hello! Thank you for using translator. Please speak in {fromLanguage}", "en", fromLangCode)
    textToAudio(inputText, fromLangCode)

    inputText = translateText(audioToText(), fromLangCode, toLangCode)
    textToAudio(inputText, toLangCode)

    inputText = translateText(f"Your sentence is converted in {toLanguage}", "en", fromLangCode)
    textToAudio(inputText, fromLangCode)

#====================================================================================================================
#Funtion to print greet messages
def displayMessages():

    msg1 = "Welcome to the portable language translator"
    msg2 = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    message = msg1.upper() + "       " + msg2
    length = len(message)

    print('*'*length)
    print(message)
    print('*'*length)

#====================================================================================================================
#Function to accept "FROM" and "TO" languages
def userChoice(language):
    
    print("")
    while True:
        choice = input(f"Enter the {language} language: ").lower()
        langCode = validateLanguage(choice)
        if langCode:
            return choice, langCode

        else:
            print("Error! Not a valid language. Please retry")
        
#====================================================================================================================
#Function to determine the entered language is part of supported language pool

def validateLanguage(choice):

    lanCode = ''
    for key, value in masterLanguageDict.items():
        if value == choice:
            lanCode = key
    return lanCode 

#====================================================================================================================
#Function to perform tranlation

def translateText(inputText, fromLang, toLang):

    try:
        translatorObj = Translator()
        tranlatedText = translatorObj.translate(inputText, src=fromLang, dest=toLang).text
        # print(tranlatedText)
    except Exception as e:
        print("Exception: " + str(e))
    else:
        # print(f"Text in {fromLang} is: " + str(inputText))
        # print(f"Text in {toLang} is: " + tranlatedText)
        return tranlatedText

#====================================================================================================================
#Function to convert audio into text

def audioToText():
    
    srObj = sr.Recognizer()
    with sr.Microphone() as source:
        srObj.adjust_for_ambient_noise(source, duration=0.2)
        inputAudio = srObj.listen(source)
        convertedText = ""

        try:
            convertedText = srObj.recognize_google(inputAudio)
            # print(convertedText)
        except Exception as e:
            print("Exception " + str(e))
    
    return convertedText

#====================================================================================================================
# Function to convert text to audio

def textToAudio(inputText,toLang):

    textToSpeechObj = gTTS(text=inputText,lang=toLang)
    fileName = "tempVoiceRecorder.mp3"
    textToSpeechObj.save(fileName)

    playsound.playsound(fileName)
    os.remove(fileName)

#====================================================================================================================
#Program entry point
if __name__  == "__main__":
    mainDriver()
#====================================================================================================================