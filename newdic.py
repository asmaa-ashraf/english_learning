from tkinter import *
from tkinter import Menu
from tkinter import ttk
from tkinter import scrolledtext
class File:
	def __init__(self):
		self.files=[]
		self.file='file.txt'
		with open(self.file,'r') as f:
			s=f.read()
			self.files=s.split(',')
		#	self.files.remove('')
	def check(self,file):
		try :	#check if it is a file 
			with open(file,'r') as f:
				return True
		except:
			return False
	def add(self,file):
		if self.files ==[] or self.files ==[' ']:
			x=False
		else:
			print(self.files)
			x=True
		if self.check(file):
			if file in self.files:
				return 'file already exists'
			self.files.append(file)
			with open(self.file,'a') as f:
				if x:
					f.write(','+file)
				else:
					f.write(file)
				return 'added'
		return 'not a file'
	def remove(self,file):
		x=''
		if file in self.files:
				self.files.remove(file)
				with open(self.file,'w') as f:
						for file in self.files:
							if x=='':
								x=file
							else:
								x=x+','+file
						self.file.write(x)
	def get(self,index=0):
		return self.files[index]
class DicItem:
	def __init__(self,word='',definition='',desc='',no=1.1):
		self.word=word
		self.definition=definition
		self.desc=desc
		self.no=str(no)
		try:
			s=self.no
			us=s.split('.')
			self.unit=us[0]
			self.lesson=us[1]
		except:
			self.unit=1
			self.lesson=1
		
	def set_word(self,word):
		self.word=word
	def set_definition(self,definition):
		self.definition=definition
	def set_desc(self,desc):
		self.desc=desc
	def get_word(self):
		return self.word
	def set_lessonNo(self,no):
		self.lesson=no
	def get_lessonNo(self):
		
		return self.lesson
	def set_unitNo(self,no):
		self.unit=no
	def get_unitNo(self):
		
		return self.unit
	
	def get_definition(self):
		return self.definition
	def get_desc(self):
		return self.desc
	def remove_newline(self,s):
		if s.endswith('\n'):
			x=s.split('\n')
			return x[0]
		return s			
	def from_line(self,line,sep=' : '):
		line=self.remove_newline(line)
		if sep in line:
			s=line.split(sep)
			self.word=s[0]
			if len(s)>1:
				self.definition=s[1]
				if len(s)>2:
					self.desc=s[2]
					if len(s)>3:
						self.no=s[3]
	def write(self,sep=' : '):
		x=self.word+sep+self.definition+sep+self.desc+sep+self.no
		return x
	def write_line(self,word,definition,desc,no,sep=' : '):
		x=word+sep+definition+sep+desc+sep+str(no)
		return x
##############################
class Dictionary:
	def __init__(self,dic=[]):
		self.dictionary=dic
	def add(self,item):
		self.dictionary.append(item)
	def remove(self,item):
		self.dictionary.remove(item)
	def search(self,word):
		for d in self.dictionary:
			if d.get_word()==word:
				return d
		return None
	def write(self):
		dic =self.dictionary
		a=''
		for i in range(len(dic)):
			a=a+dic[i].write()+'\n'
		
		return a
	def read(self,file):
		x=[]
		
		with open(file,'r') as f:
			x=f.readlines()
		for line in x:
			dicitem=DicItem()
			dicitem.from_line(line)
			self.add(dicitem)
	def get(self):
		return self.dictionary
	
win=Tk()
win.configure(bg='light blue')
dicwin=Frame(win,bg='lightblue')
dicwin.grid(column=0,row=0)
menu = Menu(win)
dic_menu=Menu(menu)
dic_menu.add_command(label='Dictionary')
dic_menu.add_command(label='Grammar')

dic_menu.add_command(label='Test')
def quit():
	win.quit()
	win.destroy()
	exit()
dicwin.grid_rowconfigure(2,weight=1)
dicwin.grid_rowconfigure(4,weight=1)
dicwin.grid_rowconfigure(5,weight=1)
dicwin.grid_rowconfigure(6,weight=1)
dicwin.grid_rowconfigure(7,weight=1)
dicwin.grid_rowconfigure(8,weight=1)
dicwin.grid_columnconfigure(0,weight=1)
dicwin.grid_columnconfigure(1,weight=1)
dicwin.grid_columnconfigure(2,weight=1)
dicwin.grid_columnconfigure(3,weight=1)
#win.grid_rowconfigure(3,weight=1)
dic_menu.add_command(label='Exit',command=quit)
menu.add_cascade(label='Menu',menu=dic_menu)
win.config(menu=menu)
header=Label(dicwin,bg='white',text='Dictionary',bd=4)
header.grid(column=1,row=0,columnspan=2)
dic=Dictionary()
f=File()
file=f.get()
dic.read(file)
dif=dic.get()
var1 =IntVar()
var2 =IntVar()
unitl=Label(dicwin,text='unit:',bg='pink')
unitl.grid(row=1,column =0)
units=Spinbox(dicwin,width=8, textvariable=var1)
ulist=[]
llist=[]
for item in dif:
	ulist.append(item.unit)
	llist.append(item.lesson)
units['values']=ulist
units.grid(row=1,column=1)

lessonl=Label(dicwin,text='lesson:',bg='pink')
lessonl.grid(row=1,column =2)
lessons=Spinbox(dicwin,width=8, textvariable=var2)
lessons.grid(row=1,column=3)
lessons['values']=llist
photo=Label(dicwin,text='word',bg='white',height=10,width=10)
photo.grid(column=1,row=2,ipadx=10,ipady=10,columnspan=2)
w=Label(dicwin,text='meaning',bg='#FF0',font=('helvetica',12))
w.grid(column=1,row=3,columnspan=2)
x=w['text']
p=LabelFrame(dicwin,text='Write the word many times to save it:',bg='#dFF',fg='purple')
p.grid(column=0,row=4,columnspan=4)
writer=Text(p,width=15,height=1)
checking=Text(p,width=15,height=1,state='disable')
score=Label(p,text='score',width=10,bg='#5FF')
writer.grid(column=1,row=6,columnspan=2)
well=Label(p,text='checking',width=8,bg='#dFF')
well.grid(column=0,row=7)
well1=Label(p,text='Write:',width=8,bg='#dFF')
well1.grid(column=0,row=6)
checking.grid(column=1,row=7,columnspan=2)
score.grid(column=3,row=4,columnspan=1)

def practice():
	if pract['text']=='hide the word':
		pract['text']='show the word'
		w.configure(text='                ')
	else:
		pract['text']='hide the word'
		w.configure(text=dif[d].get_word())
pract=Button(p,text='hide the word',command=practice,bg='#ddf')
pract.grid(column=0,row=8,columnspan=1)
sc=0
cc=0

d=0
defin=''
def check():
	global sc,cc
	checking.tag_configure('r',foreground='green')
	checking.tag_configure('w',foreground='red')
	wr=writer.get(1.0,'end')
	wrl=wr.split('\n')
	x=dif[d].get_word()
	writer.delete(1.0,'end')
	checking['state']='normal'
	checking.delete(1.0,'end')
	oc=0
	for l in wrl:
		if l !=' ' and l!='' and l!='  ':
			for i in range(len(l)):
				if i<len(x):
					if l[i]==x[i]:
						checking.insert('end',l[i],'r')
					else:
						checking.insert('end',l[i],'w')
						oc=1
				
				else:checking.insert('end',l[i],'w')
			if oc==0:
				sc=sc+1
				
			cc=cc+1
	score.configure(text='score:'+str(sc)+'/'+str(cc))
				
check1=ttk.Button(p,text='check',command=check)
check1.grid(column=1,row=8,columnspan=2)	
def image():
	sc=0
	cc=0
	if len(dif)>0:
		defin=dif[d].get_definition()
		if defin.endswith('.png'):
			i=PhotoImage(file=defin)
			photo.configure(image=i,height=400,width=400)
			photo.image=i
		else:
			photo.image=''
			photo.configure(text=defin)			
		w.configure(text=dif[d].get_word())	
		var1.set(dif[d].unit)
		var2.set(dif[d].lesson)
	else:
		w.configure(text='Dictionary is empty.')
image()
def back():
	global d,photo
	global previous
	
	if d>=1:
		d=d-1
	else :
		d=len(dif)-1
	image()
def jump():
	global d,photo,defin
	global next

	if d<len(dif)-1:
		d=d+1
	else:
		d=0
	image()
next=ttk.Button(dicwin,text='next',command=jump)
next.grid(column=3,row=2)
previous=ttk.Button(dicwin,text='previous',command=back)
previous.grid(column=0,row=2)
win.mainloop()