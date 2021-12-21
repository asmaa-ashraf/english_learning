from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import PhotoImage
class Filing:
	def __init__(self,file):
		self.file=file
	def write(self,item):
		w=open(self.file,'r')
		x=w.read()
		w=open(self.file,'w')
		if x.endswith('\n'):
			w.write(x+item)
		else:
			w.write(x+'\n'+item)
		w.close()
	def d_write(self,d):
		cont=''
		for i in d:
			cont=cont+i+' : '+d[i]+'\n'
		self.write(cont)
	def to_list(self,type='list'):
		x=open(self.file,'r')
		dic=x.readlines()
		x.close()
		words=[]
		definitions=[]
		dictionary={}
		list=[]
		for m in dic:
			r=m.split(' : ')
			if len(r)>1:
				words.append(r[0])
				e=r[1].split('\n')
				definitions.append(e[0])
				dictionary[r[0]]=e[0]
				list.append(r[0])
				list.append(e[0])
			
		if type=='words':
			return words
		elif type=='definitions':
			return definitions
		elif type=='dictionary':
			return dictionary
		else:
			return list
          ###############
window=Tk()
tab_control=ttk.Notebook(window)
tab1=Frame(tab_control)
tab2=Frame(tab_control)
tab_control.add(tab1,text='Add new words')
tab_control.add(tab2,text='Display Words')
lbl1=Label(tab1,text='write a word')
col,r=0,1
lbl1.grid(column=col,row=r,padx=2,pady=10)
wordtext=Entry(tab1,width=10)
col=1
window.configure(bg='light blue')
wordtext.grid(column=col,row=r)
lbl2=Label(tab1,text='write the definition or add path',padx=2,pady=10)
col=0
r=r+1
pic=''
def ask():
	global pic,definition
	pic=filedialog.askopenfilename()
	picture=PhotoImage(file=pic)
	definition1.configure(image=picture)
	definition1.image=picture
lbl2.grid(column=col,row=r)
col=col+1
dfn=Entry(tab1,width=10)
dfn.grid(column=col,row=r)
r=r+1
definition1=Button(tab1,text='choose photo',command=ask)
col=1
definition1.grid(column=col,row=r)
r=r+1
i=PhotoImage(file=pic)
dictionary={}
def click():
	global wordtext,pic,dictionary,r,dfn
	x,y =wordtext.get(),pic
	
	if dfn.get() !='':
		y= dfn.get()
		l2=Label(tab1,text=y,height=10,width=10)
	elif y.endswith('.png'):
		image=PhotoImage(file=y)
		l2=Label(tab1,image=image)
		l2.image=image
	dictionary[x]=y
	l1=Label(tab1,text=x)
	wordtext.delete(0,END)
	r=r+1
	col=0
	l1.grid(column=col,row=r)
	col=1
	l2.grid(column=col,row=r)
	r=r+1
	btn1.grid(column=col,row=r)
btn=Button(tab1,text ='Add Word',command=click)
r=r+3
btn.grid(column=col,row=r)
r=r+1
col=0
l=Label(tab1,text='file')
l.grid(column=0,row=r)
r=r+1
def save():
	t=''
	global dictionary
	f=Filing('new.txt')
	f.d_write(dictionary)
	
	for i in dictionary:
		t=t+i+':'+dictionary[i]+'\n'
		l.configure(text=t)
btn1=Button(tab1,text='save',command=save)
btn1.grid(column=0,row=r)
#########display tab widgets######
d=0
file=Filing('new.txt')
dif=file.to_list('definitions')
word=file.to_list('words')
def back():
	global d,photo
	global pre
	pre.configure(bg='pink')
	dif=file.to_list('definitions')
	word=file.to_list('words')
	if len(dif)>0:
		if d>=1:
			d=d-1
		else :
			d=len(dif)-1
			
		if dif[d].endswith('.png'):
			i=PhotoImage(file=dif[d])
			photo.configure(image=i,height=500,width=500)
			photo.image=i
		else:
			photo.image=''
		#	photo.configure(text=dif[d])			
		w.configure(text=word[d])	
	else:
		w.configure(text='Dictionary is empty.')
def jump():
	global d,photo
	global next
	dif=file.to_list('definitions')
	word=file.to_list('words')
	dic=dif
	next.configure(bg='pink')
	list=[c in dic]	
	if d<len(dic)-1:
		d=d+1
	else:
		d=0
	t=Label(tab2)
	if dic[d].endswith('.png'):
		i=PhotoImage(file=dic[d])
		photo.configure(image=i,height=500,width=500)
		photo.image=i
		if t!='':
			t=''
	else:
		photo.image=''
		#photo.configure(text=dic[d])
		t.configure(text=dif[d])
		t.grid(column=2,row=r-2)
	w.configure(text=word[d])
next=Button(tab2,text='Next',bg='pink',command=jump)
r=r+1
c=0
photo=Label(tab2)
dic=dif

if dic[c].endswith('.png'):
	x=PhotoImage(file=dic[c])
	photo.configure(image=x)
	photo.image=x
else:
	photo.configure(text=dic[c])
next.grid(column=0,row=r)
photo.grid(column=2,row=r)
w=Label(tab2,text=c)
w.grid(column=2,row=r+1)	
pre=Button(tab2,text='Previous',bg='pink',command=back)
pre.grid(column=3,row=r)
r=r+2
edit=Button(tab2,text='Edit this word').grid(column=2,row=r)
tab_control.pack(expand=1,fill='both')
window.mainloop()
			