
def plus(l,number):
	li=l
	n=len(li)
	for i in range(0,n):
		li[i]+=number
	return li

def mergeLists(li1,li2):
	x1=0
	x2=0
	ret=[]
	n1=len(li1)
	n2=len(li2)
	while(x1!=n1+1 and x2!=n2+1):
		if(x1==n1):
			ret = [*ret, *li2[x2:n2]]
			break
		if(x2==n2):
			ret = [*ret, *li1[x1:n1]]
			break

		if(li1[x1]<=li2[x2]):
			ret.append(li1[x1])
			x1+=1
		else:
			ret.append(li2[x2])
			x2+=1
	return ret

def removeEach(li,t):
	n=len(li)
	ret=[]
	for i in li:
		if(i>t):
			ret.append(i)	
	li=ret

def subset(li,t):
	n=len(li)
	L=[[]]*(n+1)
	L[0]=[0]
	for i in range(1,n+1):
		L[i]=mergeLists(L[i-1].copy(),plus(L[i-1].copy(),li[i-1]))
		removeEach(L[i],t)
	return max(L[n])

