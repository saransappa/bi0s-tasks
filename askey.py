def askey():
	s1=input()
	s2=input()
	sum1=0
	sum2=0
	for i in s1:
		k=ord(i)
		sum1+=k
	for i in s2:
		k=ord(i)
		sum2+=k

	if sum1==sum2:
		print("They are equal.")
	else:
		print("They are not equal.")
	return 

askey()