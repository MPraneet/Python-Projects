#Display GUI based Digital clock using Python.
from tkinter import Tk
from tkinter import Label
import time
root = Tk()
root.title("Digital Clock")
def present_time():
    display_time = time.strftime("%I:%M:%S %p \n %D ")
    digi_clock.config(text=display_time)
    digi_clock.after(20,present_time)

digi_clock = Label(root,font=("arial,150"),bg="red",fg="black")
digi_clock.pack(anchor="center")
root.mainloop()
