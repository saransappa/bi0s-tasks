#include <stdio.h>
#include <string.h>
int main()
{	
	int n;
	int sum=0;
	scanf("%d",&n);
	char str1[15];
	char str2[15];
	char str3[15];
	char str4[15];
	scanf("%s",str1);
	scanf("%s",str2);
	scanf("%s",str3);
	scanf("%s",str4);
	int marks[n];
	for(int i=0;i<n;i++)
	{
		scanf("%d",&marks[i]);
	}
	char para[100];
	fgets(para,100,stdin);
	for(int i=0;i<n;i++)
	{
		char str[15];
		if(i==0)
		{
			for(int l=0;l<strlen(str1);l++)
			{str[l]=str1[l];}
		}
		else if(i==1)
		{
			for(int l=0;l<strlen(str2);l++)
			{str[l]=str2[l];}
		}
		else if(i==2)
		{
			for(int l=0;l<strlen(str3);l++)
			{str[l]=str3[l];}
		}
		else
		{
			for(int l=0;l<strlen(str4);l++)
			{str[l]=str4[l];}
		}
		char *p;
		p=strstr(para,str);
		if(p)
		{
			sum+=marks[i];
		}
	}
	printf("%d\n",sum);
	return 0;
}