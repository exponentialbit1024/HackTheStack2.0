#include "../get_pwd.h"

#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int main()
{
	system("rm output"); //don't want you to cheat :)
	system("./host > output");

	FILE* out = fopen("output", "r");
	char output[500];
	fscanf(out, "%s", output);
	if(strcmp("please?", output))
		printf("Whatever happened to asking nicely????\n");
	else
		printf("You're welcome. The password is %s\n", get_pwd("bufofa5"));
	return 0;
}
