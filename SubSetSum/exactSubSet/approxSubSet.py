import trim as tr
from subset import mergeLists,plus,removeEach

def appSubSet(S,t,e):
	n=len(S)
	L=[[]]*(n+1)
	L[0]=[0]
	for i in range(1,n+1):
		L[i]=mergeLists(L[i-1].copy(),plus(L[i-1].copy(),S[i-1]))
		L[i]=tr.trim(L[i],e/(2*n))
		removeEach(L[i],t)
	#print(L)
	return max(L[n])

"""
S=[1,4,5,6,7,8,12,15,18,19,30,31,44,45,46]
e=2
t=10

print(appSubSet(S,t,e))
"""
