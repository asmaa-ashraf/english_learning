from tkinter import *
from tkinter import Menu
from tkinter import ttk
from tkinter import scrolledtext
import random
import dict
class MakeTest:
	def __init__(self,win,dic,grammer=''):
		self.window=win
		self.dictionary=dic
		self.grammer=grammer
		self.mr={}
		self.rearran={}
		self.row=0
		self.lis=[]
		for i in self.dictionary:
			self.lis.append(i.get_word())
		chec=ttk.Button(self.window,text='check',command=self.check)
		chec.grid(column=0,row=20,sticky="e")
		self.scorelabel=Label(self.window,text='score:00',bg="#fef")
		self.scorelabel.grid(column=0,row=0,sticky="w")
		self.row=1
	def missingletter(self,repeat):
		row=self.row
		ans=[]	
		lf=LabelFrame(self.window,text='1-complete the missing letter:',bg='#eff')
		lf.grid(column=0,row=row)
		mentry=[]
		answer={}
		xlist=[]
		for i in range(repeat):
			x=random.randint(0,len(self.lis)-1)		
			while x in xlist and i>0:
				x=random.randint(0,len(self.lis)-1)	
			xlist.append(x)
			row=row+1
			word=self.lis[x]
			r=random.randint(0,len(word)-1)
			missing=word[r]
			ans.append(missing)
			mEntry=Entry(lf,width=1)
			mentry.append(mEntry)
			rest=word.split(missing)
			if r==0:
				mEntry.grid(column=1,row=row)
				restLabel=Label(lf,text=rest[1],bg='#eff')
				restLabel.grid(column=2,row=row)
			elif r==len(word)-1:
				restLabel=Label(lf,text=rest[0],bg='#eff')
				restLabel.grid(column=1,row=row)
				mEntry.grid(column=2,row=row)
			else:
				rl1=Label(lf,text=rest[0],bg='#eff')
				rl1.grid(column=1,row=row)
				mEntry.grid(column=2,row=row)
				rl2=Label(lf,text=rest[1],bg='#eff')
				rl2.grid(column=3,row=row)
			lf1=Label(lf,text=str(i+1)+")",bg='#eff')
			lf1.grid(column=0,row=row)
			answer[ans[i]]=mentry[i]
		self.mr= answer
		self.row=row
	def rearrange(self,repeat=4):
		row=self.row
		ans=[]
		sil=[]
		answer=[]
		xlist=[]
		rf=LabelFrame(self.window,text='2-Rearrange the letters to make the word:',bg='#eff')
		rf.grid(column=0,row=row)
		for i in range(repeat):
			x=random.randint(0,len(self.lis)-1)	
			
			while x in xlist and i>0:
				x=random.randint(0,len(self.lis)-1)	
			xlist.append(x)
			row=row+1
			word=self.lis[x]
			ans.append(word)
			vessel=list(word)
			vessel.sort()
			sil.append(vessel)		
			col=1
			la=''
			for  v in range(len(vessel)):
				if v <len(vessel)-1:
					la=la+vessel[v]+'-'
				else: la=la+vessel[v]
			la1=Label(rf,text=str(i+1)+')',bg='#eff')
			la1.grid(row=i,column=0)
			la2=Label(rf,text=la,bg='#efa')
			la2.grid(row=i,column=1)
			answer.append(Entry(rf,width=15))
			answer[i].grid(row=i,column=2)	
			self.rearran[ans[i]]=answer[i]
	def missingword(self):
		print('')
		#add code
	def writeword(self):
		print('')
		#add code
	def punctuate(self):
		print('')
		#add code
	def connect(self):
		print('')
		#add code
	def choose(self):
		global scorelabel
		print('')
		#cooooode
	def check(self):
	#	global scorelabel
		missingletter=self.mr
		score=0
		x=len(missingletter)+len(self.rearran)
		for i in missingletter:
			if missingletter[i].get()==i:
				score=score+1
		for a in self.rearran:
			if self.rearran[a].get()==a:
				score=score+1			
		self.scorelabel.configure(text="score :"+str(score)+'/'+str(x))
		return score	
dic=dict.Dictionary()
f=dict.File()
file=f.get()
dic.read(file)
dif=dic.get()
win=Tk()
win.configure(bg='#eff')
menu = Menu(win)
dic_menu=Menu(menu)
dicwin=Frame(win,bg='lightblue')
dic_menu.add_command(label='Dictionary',command=dicwin.tkraise)
testwin=Frame(win,bg='#aff',height=500)
dic_menu.add_command(label='Test',command=testwin.tkraise)
dics=Frame(win)
dic_menu.add_command(label='settings',command=dics.tkraise)
def quit():
	win.quit()
	win.destroy()
	exit()

testwin.grid(column=0,row=0)
def placeholder(parent,background='white'):
	place=Label(parent,width=50,height=50,bg=background)
	place.grid(column=0,row=0,columnspan=40,rowspan=40)
placeholder(testwin)
win.grid_rowconfigure(0,weight=2)
win.grid_columnconfigure(0,weight=2)
testwin.grid_rowconfigure(2,weight=1)
testwin.grid_rowconfigure(3,weight=1)
dic_menu.add_command(label='Exit',command=quit)
menu.add_cascade(label='Menu',menu=dic_menu)
win.config(menu=menu)
header=Label(testwin,bg='light blue',text='Tests Page',bd=4)
header.grid(column=3,row=0,columnspan=3)
f=Label(testwin,text='from lesson:',bg='pink')
f.grid(row=1,column =0)
Label(testwin,text='unit:',bg='pink').grid(row=1,column =2)
var1 =IntVar()
var2 =IntVar()
ulist=[]
llist=[]
for item in dif:
	ulist.append(item.unit)
	llist.append(item.lesson)
units=Spinbox(testwin,width=2,textvariable=var1)
units.grid(row=1,column=3)
units['values']=ulist
lessons=Spinbox(testwin,width=2,textvariable=var2)
lessons.grid(row=1,column=1)
t=Label(testwin,text='to',bg='pink')
t.grid(row=1,column =4)
units1=Spinbox(testwin,width=2)
units1.grid(row=1,column=5)
units1['values']=llist
lessons1=Spinbox(testwin,width=2)
lessons1.grid(row=1,column=6)
lessons['values']=llist
lessons1['values']=llist
placeholder(dics)
def new():
	t=MakeTest(master,dif)
	t.missingletter(4)
	t.rearrange()
new=Button(testwin,text='New Test',command=new)
new.grid(row=1,column=7)
master=LabelFrame(testwin,text='Test',bg='white')
master.grid(column=0,row=2,columnspan=10)

dicwin.grid(column=0,row=0)
placeholder(dicwin)
header=Label(dicwin,bg='white',text='Dictionary',bd=4)
header.grid(column=1,row=0,columnspan=2)
dic=dict.Dictionary()
f=dict.File()
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
dic=dict.Dictionary()
f=dict.File()
file=f.get()
dic.read(file)
dif=dic.get()

dics.grid(column=0,row=0)
master=LabelFrame(dics,text='Dictionary Settings',fg='purple',bg='light blue')
master.grid(column=0,row=0)
addf=LabelFrame(master,text='add',bg='light blue')
addf.grid(column=0,row=0,columnspan=13)
wordf=LabelFrame(addf,text='New Word',bg='light blue')
wordf.grid(column=0,row=3,columnspan=13)
addl=Label(addf,text='To add a new dictonary file \nIt should be organized in word : definiton pairs ',bg='pink',fg='green').grid(column=0,row=0)
add_dic=ttk.Button(addf,text='Add a new dictionary')
add_dic.grid(column=0,row=1)
unitl=Label(wordf,text='Unit No:',bg='pink')
unitl.grid(row=0,column =0,columnspan=2,sticky='W')
units=Spinbox(wordf,width=4,values=(1,2,3))
units.grid(row=0,column=1,columnspan=2,sticky='W')
lessonl=Label(wordf,text='lesson No:',bg='pink')
lessonl.grid(row=0,column =2,columnspan=2,sticky='W')
lessons=Spinbox(wordf,width=4,values=(1,2,3))
lessons.grid(row=0,column=3,columnspan=2)
types=['','adverb','adjective','conjunction','interjection','noun','pronoun','preposition','verb']
addword=Entry(wordf,width=10)
addword.grid(column=1,row=2)

al=Label(wordf,text='word',bg='pink',fg='green')
al.grid(column=1,row=1)
dl=Label(wordf,text=':',bg='pink',fg='green')
dl.grid(column=2,row=1)
dfl=Label(wordf,text='Meaning',bg='pink',fg='green')
dfl.grid(column=3,row=1)
dsc=Label(wordf,text='desc',bg='pink',fg='green')
dsc.grid(column=4,row=1)
dots=Label(wordf,text=':',width=1,bg='pink',fg='green').grid(column=2,row=2)
adddefinition=Entry(wordf,width=10)
adddefinition.grid(column=3,row=2)
add_description=ttk.Combobox(wordf,width=6,values=types)
def edit():
	worde=LabelFrame(master,text='Edit Word',bg='light blue')
	worde.grid(column=0,row=5,columnspan=5)
	unitl2=Label(worde,text='Unit No:',bg='pink')
	unitl2.grid(row=0,column =0,columnspan=2,sticky='W')
	units2=Spinbox(worde,width=4,values=(1,2,3))
	units2.grid(row=0,column=1,columnspan=2,sticky='W')
	lessonl1=Label(worde,text='lesson No:',bg='pink')
	lessonl1.grid(row=0,column =2,columnspan=2,sticky='E')
	lessons1=Spinbox(worde,width=4,values=(1,2,3))
	lessons1.grid(row=0,column=3,columnspan=2)
	addword1=Entry(worde,width=10)
	addword1.grid(column=1,row=1,columnspan=2)
	al1=Label(worde,text='word',bg='pink',fg='green')
	al1.grid(column=0,row=1)
	dfl1=Label(worde,text='Meaning',bg='pink',fg='green')
	dfl1.grid(column=0,row=2)
	dsc1=Label(worde,text='desc',bg='pink',fg='green')
	dsc1.grid(column=0,row=3)
	adddefinition1=Entry(worde,width=10)
	adddefinition1.grid(column=1,row=2,columnspan=2)
	add_description=ttk.Combobox(worde,width=6)
	add_description.grid(column=1,row=3)
	delete_word['state']='disable'
#############
wordf.grid(column=0,row=3,columnspan=13)
def add():
	global file
	word=addword.get() #The word 
	definition=adddefinition.get()    #the defintion
	desc=add_description.get()   #the description
	ls=str(lessons.get())
	us=str(units.get())
	no=us+'.'+ls #the lesson and unit numbers
	dicitem=DicItem(word,definition,desc,no)
	
	result=dic.add(dicitem)
	Label(wordf,text=result,bg='#faf',width=30).grid(column=0,row=3,columnspan=6)
	with open(file,'a') as f:
			z='\n'+dicitem.write()
			f.write(z)	
add_word=ttk.Button(wordf,text='Add',command=add)
add_word.grid(column=0,row=2,pady=5,padx=5,ipadx=0)
add_description.grid(row=2,column=4)

found=dict.DicItem()
def search():
	f=File()
	file=f.get()
	dic.read(file)
	x=dic.search(wordentry.get())
	if x!=None:
		searchresult.configure(text=x.write())
				
	else:
		searchresult.configure(text='The word is not found.')
def delete():
	f=dict.File()
	file=f.get()
	dic1=dict.Dictionary()
	dic1.read(file)
	x=dic1.search(wordentry.get())
	if x!=None:
		dic1.remove(x)
		searchresult.configure(text='The word has been deleted')
		
		with open(file,'w') as f :
			f.write(dic.write())
	else:
		searchresult.configure(text='That word is not in the dictionary.')
	
search=ttk.Button(master,text='search for a word',command=search)
search.grid(column=0,row=4,padx=10,pady=10)
wordentry=Entry(master,width=15)
wordentry.grid(column=1,row=4,columnspan=2,padx=10,pady=10)
searchresult=Label(master,bg='light blue')
searchresult.grid(row=5,columnspan=4)
delete_word=ttk.Button(master,text='delete',command =delete)
delete_word.grid(column=2,row=6,padx=10,pady=10)
edit=ttk.Button(master,text='edit',command=edit)
edit.grid(column=1,row=6,padx=10,pady=10)
win.mainloop()