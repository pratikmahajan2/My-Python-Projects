''' 
=====================================================================================================================
Project    - Portable Language Translator - GUI based using tkinter, googletrans and text to speech API
Programmer - Pratik Mahajan
Contact    - pratikmahajan2@gmail.com
Date       - 27 - Jul - 2021

Project Description:
====================
In this project, I will be utilizing tkinter to create a simple GUI where user can type or speak the sentences they 
want to translate to desired supported language.

User will be presented with a window, where source and dstination languages can be selected from the drop-down list
boxes. Once languages are selected, user can type or speak the input sentence. Another box in the window will show 
the translated text upon clicking the translate button.

The GUI has capability to accept input as your speak. Once user selects the input language and clicks on the
microphone button, translator requests user to speak (in the selected input language). It then prints the input 
sentence in the input box. Once user confirms, input will be translated to the desired language and will be
printed in the output box. 

The speaker button reads the text in the input and output box aloud in the langauge selected.

Version Log:
=============================================
27 - Jul - 2021 - Pratik M. - Initial Version
=============================================
=====================================================================================================================
'''
#import functions required from text and voice based translator projects
# from GoogleTranslator_TextBased import translateText
import sys
sys.path.insert(1,"D:\My Projects\Git Repository\GitHub\My-Python-Projects\Translator_Voice Based")
from GoogleTranslator_VoiceBased import *

#import other packages
from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator
import googletrans

#=====================================================================================================================
#Load the list of suppoted languages from the google translator API

validLanguageDict = googletrans.LANGUAGES
validLangValuesList = list(validLanguageDict.values())
validLangKeyList = validLanguageDict.keys()

#=====================================================================================================================
#Function which lets user to select the language from selection drop down

def selectLanguage():
    inputLangBoxSelection = inputLangCombo.get().upper()
    outputLangBoxSelection = outputLangCombo.get().upper()
    inputTextLabel.configure(text=f"Input sentence in {inputLangBoxSelection} language:")
    outputTextLabel.configure(text=f"Converted sentence in {outputLangBoxSelection} language:")
    root.after(10,selectLanguage)

#=====================================================================================================================
#Function which fetches the text from input text box and langauage selection boxes and converts into desired language
#After conversion it displays the converted text in the output text box.

def startTranslation():
    global validLanguageDict
    try:
        tranlatorObj = Translator()
        inputText = inputSentenceTextBox.get(1.0, END)
        inputLanguage = inputLangCombo.get()
        outputLanguage = outputLangCombo.get()

        if inputText:
            for key, value in validLanguageDict.items():
                if value == inputLanguage:
                    inputLangCode = str(key)
                if value == outputLanguage:
                    outputLangCode = str(key)

            translatedText = tranlatorObj.translate(inputText, src=inputLangCode, dest=outputLangCode).text
            outputSentenceTextBox.delete(1.0,END)
            outputSentenceTextBox.insert(END, translatedText)
    except Exception as e:
        # print(e)
        messagebox.showerror("Translator", "Please try again")

#=====================================================================================================================
#Function to read the input or ourput text aloud.

def convertText2Audio(parameter):
    inputText = inputSentenceTextBox.get(1.0, END)
    outputText = outputSentenceTextBox.get(1.0,END)
    inputLanguage = inputLangCombo.get()
    outputLanguage = outputLangCombo.get()

    if inputText or outputText:
        for key, value in validLanguageDict.items():
            if value == inputLanguage:
                inputLangCode = str(key)
            if value == outputLanguage:
                outputLangCode = str(key)
    
    if parameter == "input":
        try:
            textToAudio(inputText, inputLangCode)
        except Exception as e:
            messagebox.showerror("Translator", e)
    elif parameter == "output":
        try:
            textToAudio(outputText, outputLangCode)
        except Exception as e:
            messagebox.showerror("Translator", e)

#=====================================================================================================================
#Function to accept input sentence in terms of audio

def convertAudio2Text():

    inputSentenceTextBox.delete(1.0, END)
    inputLanguage = inputLangCombo.get()

    for key, value in validLanguageDict.items():
        if value == inputLanguage:
            inputLangCode = str(key)
    
    textToAudio(translateText("Please speak the sentence you want to convert", "en", inputLangCode),inputLangCode)
    
    text = audioToText()
    
    inputSentenceTextBox.insert(END, text)

#=====================================================================================================================
#GUI Design

root = Tk()
root.title('Language Translator')
root.geometry("990x420")

inputLangLabel = ttk.Label(root, text = "Please select 'FROM' language:", background="light blue")
inputLangLabel.place(x=50, y=50)

inputLangCombo = ttk.Combobox(root, values=validLangValuesList, state='r')
inputLangCombo.place(x=50,y=70)
inputLangCombo.set("english")

inputTextLabel = ttk.Label(root, text="Input sentence in english language:", background="light blue")
inputTextLabel.place(x=50, y=100)

inputFrame = Frame(root, bg="black", bd=5)
inputFrame.place(x=50, y=130, width=440, height=210)

inputSentenceTextBox = Text(inputFrame, font="Helvetica", bg="white", relief=GROOVE, wrap=WORD)
inputSentenceTextBox.place(x=0, y=0, width=430, height=200)

outputLangLabel = ttk.Label(root, text = "Please select 'TO' language:", background="light blue")
outputLangLabel.place(x=500, y=50)

outputLangCombo = ttk.Combobox(root, values=validLangValuesList, state='r')
outputLangCombo.place(x=500,y=70)
outputLangCombo.set("english")

outputTextLabel = ttk.Label(root, text="Converted sentence in English language:", background="light blue")
outputTextLabel.place(x=500, y=100)

outputFrame = Frame(root, bg="black", bd=5)
outputFrame.place(x=500, y=130, width=440, height=210)

outputSentenceTextBox = Text(outputFrame, font="Helvetica", bg="white", relief=GROOVE, wrap=WORD)
outputSentenceTextBox.place(x=0, y=0, width=430, height=200)

translateActionButton = Button(root, text="Translate", cursor="hand2", bd=5, command=startTranslation)
translateActionButton.place(x=462, y=348)

speaker = PhotoImage(file = r"D:\My Projects\Git Repository\GitHub\My-Python-Projects\Translator_Tkinter GUI Based\speaker.png")
microphone = PhotoImage(file = r"D:\My Projects\Git Repository\GitHub\My-Python-Projects\Translator_Tkinter GUI Based\mic.png")

listenInput = Button(root, image=microphone, cursor="hand2", bd=5, command=convertAudio2Text)
listenInput.place(x=50, y=348)

convertInputToAudio = Button(root, image=speaker, cursor="hand2", bd=5, command=lambda: convertText2Audio("input"))
convertInputToAudio.place(x=114, y=348)

convertOutputToAudio = Button(root, image=speaker, cursor="hand2", bd=5, command=lambda: convertText2Audio("output"))
convertOutputToAudio.place(x=892, y=348)

contactLabel = ttk.Label(root, text = "Created by Pratik Mahajan. pratikmahajan2@gmail.com", background="light blue")
contactLabel.place(x=10, y=403)
#=====================================================================================================================
selectLanguage()
#=====================================================================================================================
root.configure(bg="light blue")
root.mainloop()