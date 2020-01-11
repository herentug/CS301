def trim(L,o):
	n=len(L)
	L2=[L[0]]
	last=L[0]
	for i in range(1,n):
		if(L[i]>last*(1+o)):
			L2.append(L[i])
			last=L[i]

	return L2





