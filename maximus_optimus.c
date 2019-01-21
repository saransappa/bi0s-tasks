#include<stdio.h>

void maximus_optimus() {
	int a[3];
	for(int i=0;i<3;i++)
	{
		scanf("%d",&a[i]);
	}
	int n; 
	scanf("%d",&n);
	int score=0;
	while(n--)
	{
		int k;
		int max=-5000;
		for(int i=0;i<3;i++)
		{
			if(a[i]>max)
			{
				max=a[i];
				k=i;
			}
		}
		if(max>=1)
		{
			score+=max;
			a[k]--;
		}
	}
	printf("%d\n",score);
    return;
}

int main() {
	maximus_optimus();
    return 0;
}