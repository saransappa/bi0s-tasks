def decrypt():
	#key is 13
	s=input()
	k=len(s)
	for i in range(k-1):
		a=s[i]
		b=ord(a)
		if b!=32:
			if i%2!=0:
				print(s[i],end='')
			else:
				
				b-=13
				if b<65 and ord(a)>=65 and ord(a)<=90:
					m=65-b
					b=97-m+1
				elif b<97 and ord(a)>=97 and ord(a)<=122:
					m=97-b
					b=122-m+1
				j=(str)(chr(b))
				print(j,end='')
		else:
			print(" ",end='')
			i-=1			
	print(s[k-1])
	print()		
	#print(s)
	return

decrypt()