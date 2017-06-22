from tkinter import *

def tack():
    print("Tack")
def aj():
    print("Aj, det gör ont!")
window = Tk()
buttonA = Button(window, text="Tryck här!", command=tack)
buttonB = Button(window, text="Tryck inte här!", command=aj)
buttonA.pack()
buttonB.pack()
window.mainloop()
