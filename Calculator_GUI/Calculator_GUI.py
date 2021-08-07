''' 
=====================================================================================================================
Project    - Python Calculator - GUI based
Programmer - Pratik Mahajan
Contact    - pratikmahajan2@gmail.com
Date       - 05 - Aug - 2021

Project Description:
====================
In this project, I will be utilizing tkinter to create a GUI based claculator.

A simple GUI will be presented to the user. User can click on the number and sign buttons to input the calculation
parameters. At the end, it would show the result.

Version Log:
=============================================
05 - Aug - 2021 - Pratik M. - Initial Version
=============================================
=====================================================================================================================
'''
#import packages
from tkinter import *
from tkinter import ttk, messagebox

root = Tk()
root.title('Python Calculator')
# root.geometry("270x400")
global expHist
operation=Entry(root,width=35,borderwidth=5)
operation.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def click_num(num):
    currentNum = operation.get()
    operation.delete(0,END)
    operation.insert(0,str(currentNum)+str(num))

def clearField():
    operation.delete(0,END)

def calculate():
    try:
        expression = operation.get()
        result = eval(expression)
        operation.delete(0,END)
        operation.insert(0,str(result))
    except Exception as e:
        messagebox.showerror("Calculator", f"Error: {str(e)}")

button_1 = Button(root, text="1",padx=40,pady=20,command=lambda: click_num(1))
button_1.grid(row=4,column=0)
button_2 = Button(root, text="2",padx=40,pady=20,command=lambda: click_num(2))
button_2.grid(row=4,column=1)
button_3 = Button(root, text="3",padx=40,pady=20,command=lambda: click_num(3))
button_3.grid(row=4,column=2)
button_4 = Button(root, text="4",padx=40,pady=20,command=lambda: click_num(4))
button_4.grid(row=3,column=0)
button_5 = Button(root, text="5",padx=40,pady=20,command=lambda: click_num(5))
button_5.grid(row=3,column=1)
button_6 = Button(root, text="6",padx=40,pady=20,command=lambda: click_num(6))
button_6.grid(row=3,column=2)
button_7 = Button(root, text="7",padx=40,pady=20,command=lambda: click_num(7))
button_7.grid(row=2,column=0)
button_8 = Button(root, text="8",padx=40,pady=20,command=lambda: click_num(8))
button_8.grid(row=2,column=1)
button_9 = Button(root, text="9",padx=40,pady=20,command=lambda: click_num(9))
button_9.grid(row=2,column=2)
button_0 = Button(root, text="0",padx=40,pady=20,command=lambda: click_num(0))
button_0.grid(row=5,column=0)
button_plus = Button(root, text="+",padx=39,pady=20,command=lambda: click_num('+'))
button_plus.grid(row=5,column=1)
button_minus = Button(root, text="-",padx=41,pady=20,command=lambda: click_num('-'))
button_minus.grid(row=5,column=2)
button_multiply = Button(root, text="*",padx=40,pady=20,command=lambda: click_num('*'))
button_multiply.grid(row=6,column=0)
button_division = Button(root, text="/",padx=40,pady=20,command=lambda: click_num('/'))
button_division.grid(row=6,column=1)
button_clear = Button(root, text="C",padx=40,pady=20,command=clearField)
button_clear.grid(row=6,column=2)
button_equal = Button(root, text="=",padx=135,pady=20,command=calculate)
button_equal.grid(row=7,column=0,columnspan=3)

root.configure(bg="light blue")
root.mainloop()