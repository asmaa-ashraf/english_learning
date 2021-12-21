import numpy as np
def similarity(x,y,c):
	return np.exp(-c*np.sum(np.power((x-y),2)))

def similarityToAll(x,yM,c):
	xM=np.tile(x,[np.size(yM,axis=0),1])
	sqDiff=np.power(xM-yM,2)
	ssDiff=np.sum(sqDiff,axis=1)
	return np.exp(-c*ssDiff)
def model1(testCase,cat1,cat2,c):
	c1s=np.sum(similarityToAll(testCase,cat1,c))
	c2s=np.sum(similarityToAll(testCase,cat2,c))
	return c1s/(c1s+c2s)
	
def model2(testCase,cat1,cat2,c):
	c1s=similarity(testCase,np.average(cat1,axis=0),c)
	c2s=similarity(testCase,np.average(cat2,axis=0),c)
	return c1s/(c1s+c)
x1=[1,1]
x2=[1,0]
x3=[1,3]
c=1000
print(similarity(x1,x2,c))