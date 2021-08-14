import time
from os import system

myList = []

def acceptItems():
    item = ''
    while item != 'q':
        item = input("Enter the item or press 'q' once done: ")
        if item != 'q':
            try:
                item = int(item)
            except Exception as e:
                print("wrong item inserted: " + str(e))
                # break
            else:
                myList.append(item)
    
def show_list(myList):
    system('cls')
    for item in myList:
        print(item,'X'*item)

def bubbleSort(myList):
    for i in range(len(myList)):
        for j in range(1, len(myList)-i):
    
            if myList[j-1] > myList[j] and j < len(myList):
                temp = myList[j-1]
                myList[j-1] = myList[j]
                myList[j] = temp
            time.sleep(.1)
            show_list(myList)

acceptItems()
bubbleSort(myList)

