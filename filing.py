class Filing:
	def __init__(self,file):
		self.file=file
	def write(self,item):
		w=open(self.file,'r')
		x=w.read()
		w=open(self.file,'w')
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
			
			
			
				
			
			
			
x=Filing('new.txt')
d={'hi':'hello','good':'luck','how':'are','you':'dear'}
x.d_write(d)
print(x.to_list())