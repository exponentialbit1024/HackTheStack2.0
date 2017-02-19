
#include "../get_pwd.h"
#include<stdio.h>
#include<string.h>

char username[16];


void get_name()
{
	char name[16];
	printf("What is your name? ");
	scanf("%s", name);
	strcpy(username, name);
}
void greet()
{
	if (strlen(username))
		printf("Hi %s!\n", username);
	else
	{
		printf("You haven't entered a username yet!\n");
		get_name();
	}
}

void show_password()
{
	greet();
	printf("Your password is: %s\n", get_pwd("bufofa4"));
}


int main()
{
	get_name();
	greet();
	return 0;
}
