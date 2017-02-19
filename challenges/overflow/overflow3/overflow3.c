#include "../get_pwd.h"
#include<stdio.h>
#include<stdlib.h>

int main()
{
	int ret = system("./exploit");
	if (ret == 4096)
		printf("Password is: %s\n", get_pwd("bufofa3"));
	return 0;
}
