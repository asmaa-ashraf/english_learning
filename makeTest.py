from tkinter import *
import random
window=Tk()
class MakeTest:
	window=''
	def __init__(self,win,dic,grammer=''):
		global window
		window=win
		self.window=win
		self.dictionary=dic
		self.grammer=grammer
		self.mr={}
		self.row=0
		chec=Button(window,text='check',command=self.check)
		chec.grid(column=10,row=20)
		self.scorelabel=Label(self.window,text='score')
		self.scorelabel.grid(column=0,row=0)
		self.row=1

	def missingletter(self,repeat):
		row=self.row
		ans=[]
		lis=list(self.dictionary)
		lf=LabelFrame(window,text='1-complete the missing letter:')
		lf.grid(column=0,row=row)
		mentry=[]
		answer={}
		for i in range(repeat):
			x=random.randint(0,len(lis)-1)	
			row=row+1
			word=lis[x]
			r=random.randint(0,len(word)-1)
			missing=word[r]
			ans.append(missing)
			mEntry=Entry(lf,width=1)
			mentry.append(mEntry)
			rest=word.split(missing)
			if r==0:
				mEntry.grid(column=1,row=row)
				restLabel=Label(lf,text=rest[1])
				restLabel.grid(column=2,row=row)
			elif r==len(word)-1:
				restLabel=Label(lf,text=rest[0])
				restLabel.grid(column=1,row=row)
				mEntry.grid(column=2,row=row)
			else:
				rl1=Label(lf,text=rest[0])
				rl1.grid(column=1,row=row)
				mEntry.grid(column=2,row=row)
				rl2=Label(lf,text=rest[1])
				rl2.grid(column=3,row=row)
			lf1=Label(lf,text=str(i+1)+")")
			lf1.grid(column=0,row=row)
			answer[ans[i]]=mentry[i]
		self.mr= answer
		self.row=row
	def rearrange(self):
		print('')
		#add code
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
		x=''
		for i in missingletter:
			if missingletter[i].get()==i:
				score=score+1
			self.scorelabel.configure(text=score)
		return score
			
dic={'fish':'swim','bird':'fly'}
tst=MakeTest(window,dic)
tst.missingletter(4)

window.mainloop()