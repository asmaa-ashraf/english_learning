from tkinter import *
from tkinter import ttk
from tkinter import PhotoImage
window=Tk()
tab_control=ttk.Notebook(window)
tab1=Frame(tab_control)
tab2=Frame(tab_control)
tab_control.add(tab1,text='Add new words')
tab_control.add(tab2,text='Display Words')

#file=open('file.txt')
lbl1=Label(tab1,text='write a word')
col,r=0,1

lbl1.grid(column=col,row=r)
word=Entry(tab1,width=10)
col=1
window.configure(bg='light blue')
word.grid(column=col,row=r)
lbl2=Label(tab1,text='write the definition or add path')
col=0
r=r+1
lbl2.grid(column=col,row=r)
definition=Entry(tab1,width=10)
col=1
definition.grid(column=col,row=r)
i=PhotoImage(file='f.png')
#lx=Label(tab2,image=i)
#lx.grid(column=0,row=10)
dictionary={}
def click():
	global word,definition,dictionary,r
	x,y =word.get(),definition.get()
	dictionary[x]=y
	#add try and catch
	image=PhotoImage(file=y)
	l1=Label(tab1,text=x)
	word.delete(0,END)
	definition.delete(0,END)

	r=r+1
	col=0
	l1.grid(column=col,row=r)
	l2=Label(tab1,image=image,height=10,width=10)
	
	col=1
	l2.grid(column=col,row=r)
	r=r+1
	btn1.grid(column=col,row=r)
	print('hi')
btn=Button(tab1,text ='Add Word',command=click)
r=r+3
btn.grid(column=col,row=r)
r=r+1
col=0
l=Label(tab1,text='file')
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
btn1=Button(tab1,text='save',command=save)
btn1.grid(column=0,row=r)
#########display tab widgets######
d=0
list=['fish','play','wash']
dic={'fish':'f.png','play':'play.png','wash':'wash .png'}
def back():
	global d,photo
	global pre
	pre.configure(bg='pink')
	if d>1:
		d=d-1
	else:
		d=len(list)-1
	y=list[d]
	i=PhotoImage(file=dic[y])
	photo.configure(image=i,height=500,width=500)
	w.configure(text=list[d])
	
def jump():
	global d,photo
	global next
	next.configure(bg='pink')
	if d<len(list)-1:
		d=d+1
	else:
		d=0
	y=list[d]
	i=PhotoImage(file=dic[y])
	photo.configure(image=i,height=500,width=500)
	w.configure(text=list[d])
next=Button(tab2,text='Next',bg='pink',command=jump)
r=r+1

x=PhotoImage(file=dic['fish'])
next.grid(column=0,row=r)
photo=Label(tab2,image=x)
photo.grid(column=2,row=r)
w=Label(tab2,text='fish')
w.grid(column=2,row=r+1)


	
pre=Button(tab2,text='Previous',bg='pink',command=back)
pre.grid(column=3,row=r)
tab_control.pack(expand=1,fill='both')
window.mainloop()