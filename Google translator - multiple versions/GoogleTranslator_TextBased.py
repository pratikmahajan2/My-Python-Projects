''' 
=====================================================================================================================
Project    - Portable Language Translator - Text based using googletrans API
Programmer - Pratik Mahajan
Contact    - pratikmahajan2@gmail.com
Date       - 25 - Jul - 2021

Project Description:
====================
In this project, I will be utilizing googletrans API to perform text translation from source language to desired
language. 
User will be prompted to enter a source language first. The program validates the source language against supported
language pool. If valid, user will then be asked to enter "TO" language, which will again be validated. If valid, 
user will be able to type in the text in source language, which will then be converted and deisplayed in desired
language.  

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
#====================================================================================================================
#fetch dictionary of supported language from googletrans
masterLanguageDict = googletrans.LANGUAGES
# print(masterLanguageDict)
#====================================================================================================================
#Function to drive the main logic of the code
def mainDriver():

    displayMessages()
    fromLangCode = userChoice("from")
    # print(fromLangCode)
    toLangCode = userChoice("to")
    # print(toLangCode)
    translateText(fromLangCode, toLangCode)

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
            return langCode

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

def translateText(fromLang, toLang):

    inputText = input("Please enter the text you want to translate: ")
    
    try:
        translatorObj = Translator()
        tranlatedText = translatorObj.translate(inputText, src=fromLang, dest=toLang).text
        print(tranlatedText)
    except Exception as e:
        print("Exception: " + str(e))
    else:
        print(f"Text in {fromLang} is: " + str(inputText))
        print(f"Text in {toLang} is: " + tranlatedText)

#====================================================================================================================

if __name__  == "__main__":
    mainDriver()
#====================================================================================================================