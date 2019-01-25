def jumble():
	t=int(input())
	for i in range(t):
		a=[]
		b=[]
		s=input()
		s=s.replace(" ", "")
		k=len(s)
		i=0
		while i<k:
			if i%2==0:
				a.append(s[i])
			else:
				b.append(s[i])
			i+=1
		b.reverse()
		for i in range(int(k/2)):
			print(a[i],end='')
			print(b[i],end='')
		print('\n')
	return
jumble()