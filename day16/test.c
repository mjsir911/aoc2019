#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char s[650 * 10000];

void phase(int k) {
	char runsum = 0;
	for (int i=sizeof(s)/sizeof(s[0]); i > k; i--) {
		runsum += s[i];
		runsum %= 10;
		s[i] = runsum;
	}
}

void repeat(char *buf, int len, int amount) {
	for (int i=1; i < amount; i++) {
		for (int j=0; j < len; j++) {
			buf[(i*len)+j] = buf[j];
		}
	}
}

int main(int argc, char *argv[]) {
	char inp[650 + 1];
	char offset_s[7 + 1];
	fgets(inp, sizeof(inp), stdin);
	strncpy(offset_s, inp, 7);
	size_t offset = atol(offset_s);

	for (int i=0; i < 650; i++) {
		s[i] = inp[i] - '0'; // atoc basically
	}

	repeat(s, 650, 10000);
	for (int i=0; i < 100; i++) {
		phase(offset - 1);
	}
	for (int i=0; i < 8; i++) {
		printf("%i", s[offset+i]);
	}
	printf("\n");
}
