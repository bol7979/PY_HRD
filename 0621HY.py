from tkinter import *

screen = Tk()
screen.title("radio_button")
screen.geometry("310x200")

def func():
    print(storage.get())

storage = IntVar() #정수형 라디오 버튼 한 묶음 #문자형: StringVar()
storage_b_01 = Radiobutton(screen, text = "One", value = 1, variable = storage)
storage_b_02 = Radiobutton(screen, text = "Two", value = 2, variable = storage)
storage_b_03 = Radiobutton(screen, text = "Three", value = 3, variable = storage)
b_01 = Button(screen, text = "확인", command = func)

storage_b_01.pack()
storage_b_02.pack()
storage_b_03.pack()
b_01.pack()

screen.mainloop()