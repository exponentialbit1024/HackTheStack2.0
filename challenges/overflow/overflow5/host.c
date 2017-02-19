#include<stdio.h>

//char shellcode[] = "\xeb\x1a\x31\xc0\x31\xdb\x31\xd2\x40\xc1\xe0\x02\x59\x43\x42\xc1\xe2\x03\x4a\xcd\x80\x31\xc0\x40\x31\xdb\xcd\x80\xe8\xe1\xff\xff\xffplease??";
void hack()
{
	char shellcode[100];
	scanf("%s", shellcode);
	int(*ret)();
	ret = (int(*)())shellcode;
	ret();
}

int main()
{
	hack();
	return 0;
}
