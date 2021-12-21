#simple grammer rules
#this,it,he,she+is+adjective
#a,an before single 
#you,we,they,those+are,I+am
#identifying subject
class Grammer:
	def __init__(self,nouns=[]):
		self.nouns=nouns
		self.vowels=['a','i','e','o','u']
		self.pronounis=['he','she','it','this']
		self.pronounare=['those','we','they','you']
	def be(self,subject):
		if subject in self.pronounis:
			return 'is'
		elif subject in self.pronounare:
			return 'are'
		elif subject=='i':
			return 'am'
	def a_an(self,word):
		if word.endswith('s'):
			return None
		for w in self.vowels:
			if word.startswith(w):
				return 'an'
		return 'a'
n=['nice','happy']
g=Grammer(n)
print(g.be('i'))
print(g.a_an('ear'))
		
		