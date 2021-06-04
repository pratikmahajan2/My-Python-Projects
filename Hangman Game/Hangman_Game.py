#HANGMAN GAME:
# Good old Hangman game, where use has to guess a word in the given attempt. If guessed correct,user 
# wins or the Hangman dies.

# The game is written for my daugter to practice her vocabulary.

# Rules:
# Words will picked randomly from the file. 
# Number of attempts offered to users will be equal to the unique characters in the word.
# Only alphabets are allowed. No special character allowed.

import random
from collections import OrderedDict
import os
import time

def main():
  os.system('cls')
  print("**** WELCOME TO HANGMAN GAME ****")
  print("\n")
  print("     1. Create new world list.")
  print("     2. Add in existing list.")
  print("     3. Play the Game.")
  print("     4. Quit.")
  print("\n")
  
  choice = int(input("Enter Your Choice: "))

  switcher = {
    1 : createNewList,
    2 : addList,
    3 : playGame,
    4 : over
  }
  switcher.get(choice, main)()

def createNewList():
  file = open('Hangman_Words.txt', 'w')
  wordList = []
  while True:
    word = input("Enter the word to add in the list: ")
    if word in wordList:
      print("word is already in the list.")
    else:
      wordList.append(word.lower())
      wordList.append('\n')
    
    choice = input("Want to add more words? (Y/N): ")
    if choice == 'Y' or choice == 'y':
      pass
    else:
      file.writelines(wordList)
      file.close()
      break
  main()

def addList():

  while True:
    
    wordToAdd = input("Please enter the word you want to add in the word list or enter 'q' to exit: ")
    print("\n")
      
    file = open('Hangman_Words.txt', 'r')
    fileText = file.readlines()
    file.close()

    wordList = []

    for items in fileText:
      wordList.append(items.strip())
      # print(items)
  

    if wordToAdd in wordList:
      print(f"{wordToAdd} is already present in the word list. Try another word or enter 'q' to exit.")

    elif wordToAdd.lower() == 'q' :
      break
    
    else:
      wordToAdd = wordToAdd + "\n"
      file = open('Hangman_Words.txt', 'a')
      file.writelines(wordToAdd.lower())
      file.close()

      print("Ward has been added. Want to add more? Enter the word or enter 'q' to exit\n")

  main()

def over():
  exit

def playGame():

  choice = input("Ready to play Hangman ? (Y/N): ")
  if choice == 'Y' or 'y':
    os.system('cls')
    print("Welcome ! Let's play")

    breakLoop = False
    isFirstTime = True

    while breakLoop == False:
      
      # Load the input file and return a random word
      
      word = loadInputFile(isFirstTime)
      isFirstTime = False
      # print(word)

      # identify length of the word ignoring the duplicate characters
      wordLen = checkLength(word)
      # print(wordLen)

      # Show the maximum attempts available to user
      print("The word has {wordLen} unique characters. Thus you have {wordLen} attempts.".format(wordLen = wordLen))

      # Start accepting the options
      startGame(word, wordLen)

      # Take user choice to continue next round
      choice1 = input("Do you want to continue ? (Y/N)")
      if choice1 == 'Y' or choice1 == 'y':
        breakLoop = False
        os.system('cls')
      else:
        breakLoop = True
        print("Bye!!!")
  else:
    print("Bye!!!")
  main()





def loadInputFile(isFirstTime):

  # Open the file in read mode and read the lines
  file = open('Hangman_Words.txt', 'r')
  fileText = file.readlines()
  file.close()

  # Strip the escape characters and create a list of the words
  wordList = []
  for wl in fileText:
    wordList.append(wl.strip())

  if isFirstTime == True:
    print("Here's the word list to be displayed for 5 sec. Get ready!")
    
    for items in wordList:
      print(items)
    
    timeCount = 5

    while timeCount >= 0:
      print("Time Remaining ", timeCount)
      time.sleep(1)
      timeCount -= 1
    os.system('cls')

  # Determine length of the wordList (No. of words) and return a random word form the list 
  noOfWords = len(wordList)
  # print("noOfWords: ", noOfWords)
  return (wordList[random.randint(0, noOfWords-1)])




def checkLength(word):
  deDupeLen = ''.join(OrderedDict.fromkeys(word))
  #print("Dedupe word: ", deDupeLen)
  return len(deDupeLen)




def startGame(word, wordLen):
  wordList = []
  noOfAttempt = wordLen

  # fill the wordlist with '-'
  for i in range(0,len(word)):
    wordList.append('-')

  # Print empty word list
  # print(wordList)

  # Accept user choice until the noOfAttempt = 0
  while noOfAttempt > 0:
    # os.system('cls')
    print(wordList)
    charGuess = input("Guess a character: ").lower()
    

    if charGuess not in wordList:
      if charGuess in word:
        for i in range(0,len(word)):
          if word[i] == charGuess:
            wordList[i] = charGuess
            # print(wordList)
    
      else:
        print(charGuess, " is not present in the word. Try again")
        noOfAttempt  -= 1
        # dummy = input()
    else:
      print("Already guessed ", charGuess)
      # dummy = input()
    
    # os.system('cls')

    if '-' not in wordList:
      print(wordList)
      print("You Won")
      # time.sleep(5)
      break
    else:
      print("No of attempt remaining ", noOfAttempt)
      if noOfAttempt == 0:
        print("You lost")
        print("The word was: ", word, "\n")
        # time.sleep(5)
    # os.system('cls')




if __name__ == main():
  main()