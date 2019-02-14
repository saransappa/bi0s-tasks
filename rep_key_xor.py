def xor(s):
	m=len(s)
	i=0
	n=''
	while i<m:
		p=chr(ord(s[i])^ord('I'))
		n=n+p
		i+=1
		if i>=m:
			break
		q=chr(ord(s[i])^ord('C'))
		n=n+q
		i+=1
		if i>=m:
			break
		r=chr(ord(s[i])^ord('E'))
		n=n+r
		if i>=m:
			break
		i+=1
	return n				

s1="Burning 'em, if you ain't quick and nimble"
s2="I go crazy when I hear a cymbal"
k=xor(s1)
y=k.encode("hex")
l=xor(s2)
z=l.encode("hex")
print y
print len(y)
print z
print len(z) 

