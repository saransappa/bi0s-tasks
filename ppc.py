def pal(k):
	m=list(k)
	n=list(k)
	n.reverse()
	if m!=n:
		print("NOT PALINDROME")
	else:
		print("PALINDROME")

print("Please enter the no.of words you want to enter :  ",end='')
n=int(input())
a=[]
for i in range(n):
	a.append(input())
i=1
while i<=(len(a)-2):
	k=a[i-1]+a[i]+a[i+1]
	pal(k)
	i+=1