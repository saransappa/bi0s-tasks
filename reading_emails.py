import re
def emails():
	while True:
		s=input()    #enter 'end' to stop the program.
		if(s=='end'):
			return
		k=re.findall(r'[\w+\.-]+@+[\w+\.-]+',s)
		print(k)
	return


emails()