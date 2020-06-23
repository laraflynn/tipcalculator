# Author: Lara Flynn
# Created: June 19 2020
# Last Updated: June 22 2020

import tkinter
from tkinter import Entry, Frame, Button, Label, StringVar, END
 
# get the numbers from input
def retrieveEntry():
    bill = 0
    percent = 0
    
    try:
        bill = float(my_entry1.get())
    except ValueError:
        resultLabel.config(text = "Please enter a number for both inputs.")
    
    try:
        percent = float(my_entry2.get())
    except ValueError:
        resultLabel.config(text = "Please enter a number for both inputs.")
    
    # valid input, go on
    if type(bill) == float and type(percent) == float:
        tip = bill * (percent / 100)
        total = bill + tip
        returnEntry(tip, total)
 
# show the resulting tip and total
def returnEntry(tip, total):
    str1 = "Your tip is " + str('{:.2f}'.format(tip)) + "."
    str2 = "Your total is " + str('{:.2f}'.format(total)) + "."
    resultLabel.config(text = str1 + "\n" + str2)
    # delete inputs when done calculating
    my_entry1.delete(0, END)
    my_entry2.delete(0, END)

# the main GUI
root = tkinter.Tk()
root.geometry("300x200")
root.title("Tip Calculator")

# use to format everything nicely
frame = Frame(root)
frame.pack()
 
# create a fresh label to show output
resultLabel = Label(root, text = "")
resultLabel.pack()

# inform and get first input
text1 = StringVar()
text1.set("How much was the bill?")
text1Dir = Label(frame, textvariable = text1, height = 1)
text1Dir.pack()

my_entry1 = Entry(frame, width = 20)
my_entry1.pack(padx = 5, pady = 5)

# inform and get second input
text2 = StringVar()
text2.set("How much, in percent, do you plan to tip?")
text2Dir = Label(frame, textvariable = text2, height = 1)
text2Dir.pack()
 
my_entry2 = Entry(frame, width = 10)
my_entry2.pack(padx = 5, pady = 5)

# button to submit
Button = Button(frame, text = "Calculate", command = retrieveEntry)
Button.pack(padx = 5, pady = 5)
 
root.mainloop()