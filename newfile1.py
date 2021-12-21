class File:
	def __init__(self):
		self.files=[]
		self.file='file.txt'
		with open(self.file,'r') as f:
			s=f.read()
			self.files=s.split(',')
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
dic=Dictionary()
dic.read(file)
z=dic.search('two')
if z!=None:
	dic.remove(z)