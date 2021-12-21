from tkinter import *
t=Tk()
f=Frame(t,width=500,height=500,bg='#eee')
f1=Frame(t,width=500,height=500,bg='#eee')
f2=Frame(t,width=500,height=500,bg='#eee')
def go():
	f2.tkraise()
	f2.configure(bg="#567")
def go1():
	f1.tkraise()
	f2.configure(bg="#567")
def go2():
	f.tkraise()
	f.configure(bg="#567")
f.grid(column=0,row=0)
f1.grid(column=0,row=0)	
f2.grid(column=0,row=0)
fb=Button(f,text='go to f2',command=go)
fb.grid(column=0,row=0)
fb=Button(f1,text='go to f',command=go2)
fb.grid(column=0,row=0)
fb=Button(f2,text='go to f1',command=go1)
fb.grid(column=0,row=0)
t.mainloop()