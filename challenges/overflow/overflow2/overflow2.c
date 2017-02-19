#include "../get_pwd.h"
#include<time.h>
#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	char correctPassword[10];
	char inputPassword[10];
	for (int i = 0; i < 9; i++)
		correctPassword[i] = (char)(rand() % 256);
	correctPassword[9] = '\0';
	scanf("%s", inputPassword);
	if (!strcmp(inputPassword, correctPassword))
		printf("The password is: %s\n", get_pwd("bufofa2"));
}
