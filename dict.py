class File:
	def __init__(self):
		self.files=[]
		self.file='file.txt'
		with open(self.file,'r') as f:
			s=f.read()
			self.files=s.split(',')
			#self.files.remove('')
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
class MakeTest:
	def __init__(self,win,dic,grammer=''):
		self.window=win
		self.dictionary=dic
		self.grammer=grammer
		self.mr={}
		self.row=0
		chec=ttk.Button(self.window,text='check',command=self.check)
		chec.grid(column=10,row=20)
		self.scorelabel=Label(self.window,text='score')
		self.scorelabel.grid(column=0,row=0)
		self.row=1

	def missingletter(self,repeat):
		row=self.row
		ans=[]
		for i in dictionary:
			lis[i]=self.dictionary[i].get_word()
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
	