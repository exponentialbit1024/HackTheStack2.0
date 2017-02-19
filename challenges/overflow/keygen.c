#include<time.h>
#include<stdlib.h>
#include<stdio.h>

int main(int argc, char** argv)
{
	srand(time(0));
	if (argc < 2)
		return -1;
	int chars = atoi(argv[1]);
	for (int i = 0; i < chars; i++)
	{
		char suffix = rand() % 32;
		char prefix = rand() % 4 + 1;
		printf("%x", suffix + (prefix << 5));
	}
	printf("\n");
	return 0;
}
