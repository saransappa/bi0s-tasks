g=lambda x : 1 if x%4==0 and x%100!=0 and x%400!=0 else 0
if g(int(input()))==1:
	print("Yes")
else:
	print("No")
