
#define PWDS 1

#include<string.h>
#include<stdio.h>
#include<stdlib.h>



const char* get_pwd(const char* key)
{
	FILE* fp = fopen("/var/www/app/app/challengePassKeys", "r");
	if (!fp)
		return "DEAD";
	char line[40];
	while(fgets(line, sizeof(line), fp))
	{
		char format[50];
		sprintf(format, "%s=%%s", key);
		char* pass = (char*) malloc(20);
		sscanf(line, format, pass);
		if (strlen(pass))
			return pass;
	}
}
