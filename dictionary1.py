from tkinter import *
window=Tk()
file=open('file.txt')
lbl1=Label(text='write a word')
col,r=0,1

lbl1.grid(column=col,row=r)
word=Entry(window,width=10)
col=1
window.configure(bg='light blue')
word.grid(column=col,row=r)
lbl2=Label(text='write the definition or add path')
col=0
r=r+1
lbl2.grid(column=col,row=r)
definition=Entry(window,width=10)
col=1
definition.grid(column=col,row=r)
dictionary={}
def click():
	global word,definition,dictionary,r
	x,y =word.get(),definition.get()
	dictionary[x]=y
	l1=Label(text=x)
	word.delete(0,END)
	definition.delete(0,END)

	r=r+1
	col=0
	l1.grid(column=col,row=r)
	l2=Label(text=dictionary[x])
	
	col=1
	l2.grid(column=col,row=r)
	r=r+1
	print('hi')
btn=Button(text ='Add Word',command=click)
r=r+3
btn.grid(column=col,row=r)
r=r+1
col=0
l=Label(text='file')
l.grid(column=0,row=r)
r=r+1
def save():
	dict={'f':'g'}
	t=''
	global dictionary
	f=open('file.txt','r')
	file=f.read()
	f=open('file.txt','w')
	for i in dictionary:
		t=t+i+':'+dictionary[i]+'\n'
		l.configure(text=t)
		
	f.write(file+t)
	f.close()
btn1=Button(text='save',command=save)

btn1.grid(column=col,row=r)
window.mainloop()