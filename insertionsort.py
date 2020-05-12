def insertion(L):
	for i in range(1,len(L)):
		item_to_insert=L[i]
		j=i-1
		while j>=0 and L[j]>item_to_insert:
			L[j+1]=L[j]
			j-=1
		L[j+1]=item_to_insert

print("in dev branch)