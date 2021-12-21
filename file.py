class File:
	def __init__(self):
		
		self.files=[]
		
		self.file='file.txt'
		with open(self.file,'r') as f:
			s=f.read()
			self.files=s.split(',')
			self.files.remove('')
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
c=File()
print(c.add('new.txt'))
print(c.add('dictionary.txt'))