def secret_images():
	p=0
	b=0
	j=0
	n=int(input())
	for i in range(n):
		temp=input()
		str1='.png'
		str2='.bmp'
		str3='.jpeg'
		k=temp.find(str1)
		l=temp.find(str2)
		m=temp.find(str3)
		if k>0:
			p=p+1
		elif l>0:
			b=b+1
		elif m>0:
			j=j+1
	print(p)
	print(b)
	print(j)
	return

secret_images()