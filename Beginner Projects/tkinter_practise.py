from tkinter import *

root = Tk()
root.title("First GUI")

e=Entry(root,width=50)
e.grid(row=0,column=0,columnspan=2,padx=20,pady=20)
# e.insert(0,"Enter Your Name")

def myClick():
    myLabel = Label(root, text = f"Hello {e.get()}!")
    myText = e.get()
    myLabel.grid()
    e.delete(0,END)
    e.insert(0,myText)
    

myButton= Button(root,text="Click Me!",command=myClick)
buttonExit = Button(root,text="Exit",command=e.quit)
myButton.grid(row=1, column=0)
buttonExit.grid(row=1, column=1)

root.mainloop()