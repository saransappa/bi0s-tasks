def chopsticks(a,b,n,arr):
	count=0
	for i in range(n):
		if (a+b)>arr[i] and (a-b)<arr[i]:
			count+=1
	return count

t=int(input())
while t>0:
	a=int(input())
	b=int(input())
	r=int(input())
	n=int(input())
	arr=[]
	for j in range(n):
		arr.append(int(input()))
	k=chopsticks(a,b,n,arr)
	print(k)
	if k>r:
		print("Natsu")
	else:
		print("Grey")
	t-=1