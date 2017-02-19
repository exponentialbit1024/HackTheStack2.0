#include<stdio.h>
#include <string.h>
union {
	char segment[16];
	short encoded[8];
} coder;

int main(int argc, char* argv[])
{
	char* password = argv[1];
	strcpy(coder.segment, password);
	short old = coder.encoded[0] / 2;
	printf("%d ", old);
	for (int i = 1; i < 8; i++)
	{
		printf("%d ", coder.encoded[i] - old);
		old = coder.encoded[i];
	}
	printf("\n");
	return 0;
}
