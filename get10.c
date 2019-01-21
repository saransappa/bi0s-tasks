#include <stdio.h>
void Toget(int n)
{
	float sum=0;
	for(int i=0;i<n;i++)
	{
		int temp=0;
		scanf("%d",&temp);
		sum+=temp;
	}
	float avg=sum/n;
	if(avg>=9.5)
	{
		printf("0\n");
	}
	else
	{
		int count=0;
		while(1)
		{
			sum+=10;
			n++;
			avg=sum/n;
			count++;
			if(avg>=9.5)
			{
				printf("%d\n",count);
				return;
			}
		}
		
	}
}
int main()
{
	int n;
	scanf("%d",&n);
	Toget(n);
	return 0;
}