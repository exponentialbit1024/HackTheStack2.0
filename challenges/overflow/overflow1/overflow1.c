#include<stdio.h>
#include<string.h>
#include "../get_pwd.h"

int main()
{
	char lock[7] = "CLOSED";
	char buffer[10];
	scanf("%s", buffer);
	if(strcmp(lock, "CLOSED"))
		printf("Password is: %s\n", get_pwd("bufofa1"));
	return 0;
}
