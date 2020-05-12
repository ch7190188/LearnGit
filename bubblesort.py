def bubblesort(L):
	for i in range(1,len(L)):
		for j in range(len(L)-i):
			if L[j]>L[j+1]:
				L[j],L[j+1]=L[j+1],L[j]
a=[82,4,5,3,45,3,44]
bubblesort(a)
print(a)



