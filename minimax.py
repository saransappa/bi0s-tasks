def minimax():
	a=[]
	min=0
	max=0
	for i in range(5):
		a.append(int(input()))
	a.sort()
	for i in range(4):
		min=min+a[i]
	for i in range(1,5):
		max=max+a[i]
	print(min)
	print(max)
	return

minimax()