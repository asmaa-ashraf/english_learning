from tkinter import  *
window=Tk()
window.title("hi dear friend")
window.configure(bg='gold')
lbl=Label(window,text='type your name')
lbl.grid(column=0,row=0)
lbl1=Label(window,text='')
lbl1.grid(column=0,row=2)
window.geometry('10x10')
def clicked():
  s=txt.get()
  lbl1.configure(text='hello!'+s)
btn = Button(window, text="Click Me", bg="orange", fg="red",command=clicked)
btn.grid(column=0,row=1)
txt=Entry(window,width=10)
txt.grid(column=1,row=0)
window.mainloop()

