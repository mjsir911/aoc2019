#include <stdio.h>
#include <math.h>
#include <stdlib.h>

void print_reel(size_t n, int reel[n]) {
	printf("[");
	for (int *i = reel; i < reel + n; i++) {
		printf("%d, ", *i);
	}
	printf("]\n");
}

int getval(int *r, int v, int **mode) {
	switch (*((*mode)++)) {
		case 1:
			fprintf(stderr, " %d ", v);
			return v;
		case 0:
			fprintf(stderr, " *%d(=%d) ", v, r[v]);
			return r[v];
	}
}

#define lenof(l) sizeof(l) / sizeof(l[0])
void computer(int *r, FILE *input) {
	int *p = r;
	int op;
	fprintf(stderr, "pc: %ld\n", (p) - r);
	fprintf(stderr, "op: %d\n", *p);
	while ((op = *(p++))) {
		int pmode_t[8] = {0};
		int *pmode = pmode_t;
		for (int i=0; i < 8; i++) {
			pmode[i] = (op / (int) pow(10, (i + 2))) % 10;
		}
		switch (op % 100) {
			case 1: {
				fprintf(stderr, "*%ld = ", (p) - r);
				int val1 = getval(r, *(p++), &pmode);
				fprintf(stderr, "+");
				int val2 = getval(r, *(p++), &pmode);
				fprintf(stderr, "\n");
				r[*(p++)] = val1 + val2;
				break;
			}
			case 2: {
				int val1 = getval(r, *(p++), &pmode);
				int val2 = getval(r, *(p++), &pmode);
				r[*(p++)] = val1 * val2;
				break;
			}
			case 3: {
				char *in = NULL;
				size_t n = 0;
				fprintf(stderr, "input: ");
				int status = getline(&in, &n, input);
				if (status == -1) {
					fprintf(stderr, "expecting input!\n");
					exit(1);
				}

				r[*(p++)] = atoi(in);
				if (in) free(in);
				break;
			}
			case 4: {
				printf("%d\n", getval(r, *(p++), &pmode));
				break;
			}
			case 5: {
				fprintf(stderr, "if ");
				int cond = getval(r, *(p++), &pmode);
				fprintf(stderr, "? jump");
				int *loc = r + getval(r, *(p++), &pmode);
				fprintf(stderr, "\n");
				fprintf(stderr, "loc: %ld\n", loc - r);
				if (cond) {
					p = loc;
				}
				break;
			}
			case 6: {
				int cond = getval(r, *(p++), &pmode);
				int *loc = r + getval(r, *(p++), &pmode);
				if (! cond) {
					p = loc;
				}
				break;
			}
			case 7: {
				int val1 = getval(r, *(p++), &pmode);
				int val2 = getval(r, *(p++), &pmode);
				r[*(p++)] = val1 < val2;
				break;
			}
			case 8: {
				int val1 = getval(r, *(p++), &pmode);
				int val2 = getval(r, *(p++), &pmode);
				r[*(p++)] = val1 == val2;
				break;
			}
			case 99: {
				return;
				break;
			}
			default: {
				fprintf(stderr, "Unknown op!: %d\n", op);
				exit(0);
			}
		}
		fprintf(stderr, "pc: %ld\n", (p) - r);
		fprintf(stderr, "op: %d\n", *p);
	}
}


int main(int argc, char *argv[]) {
	int reel[] = {
		#include "prog.int"
	};
	computer(reel, stdin);
}
