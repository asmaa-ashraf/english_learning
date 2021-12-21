from tkinter import Menu
from tkinter import *
window =Tk()

menu = Menu(window)

menu.add_command(label='File')

window.config(menu=menu)
menu.add_cascade(label='file',menu='newItem')
window.mainloop()
