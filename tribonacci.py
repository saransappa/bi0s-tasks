def div(n):
	div=0
	i=1;
	while(i<=n):
		if(n%i==0):
			div+=1
		i+=1

	return div
def func(n):
	a=0
	b=0
	c=1
	while True:
		d=a+b+c
		k=div(d)
		if(k>n):
			print(d)
			break
		a=b
		b=c
		c=d
	return
	
t=int(input())
while t>0 :
	n=int(input())
	func(n)
	t-=1