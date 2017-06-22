from tkinter import *
from random import randint
randomNumber = randint(1,6)
def throw():
    text.delete(0.0, END)
    text.insert(END, str(randomNumber))
    if randomNumber % 2 == 0:
        print("You threw an even number.")
    else:
        print("You threw an odd number")
window = Tk()
text = Text(window, width=1, height=1)
button = Button(window, text="Press to throw the die", command=throw)
text.pack()
button.pack()
window.mainloop()
