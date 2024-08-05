from tkinter import *
from math import pi

screen = Tk()
screen.title("calc_r^2")
screen.geometry("230x70")

def calc():
    r = int(entry_01.get())
    result = r ** 2 * pi
    label_02.config(text = result)
    screen.title("calc_r^2ed")

label_01 = Label(screen, text = "반지름: ")
label_02 = Label(screen, text = "원의 넓이")

entry_01 = Entry(screen)

button_01 = Button(screen, width = 10, command = calc, text = "calc")


label_01.grid(row = 0, column = 0, columnspan = 2)
entry_01.grid(row = 1, column = 0)
button_01.grid(row = 1, column = 1)
label_02.grid(row = 2, column = 0, columnspan = 2)

screen.mainloop()