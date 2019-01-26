import ast
def record():
	d=ast.literal_eval(input())
	a=[]
	for i in d.values():
		a.append(i)
	a.sort()
	a.reverse()
	m=len(a)
	i=0
	for k,v in d.items():
		d[k]=a[i]
		i+=1
	print(d)
	return

record()
