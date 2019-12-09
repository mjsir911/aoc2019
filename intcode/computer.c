#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#ifdef TRACE
	#define trace eprintf
#else
	#define trace(...)
#endif

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
			trace(" %d ", v);
			return v;
		case 0:
			trace(" *%d(=%d) ", v, r[v]);
			return r[v];
	}
}

#define lenof(l) sizeof(l) / sizeof(l[0])
void computer(int *r, FILE *input) {
	int *p = r;
	int op;
	trace("pc: %ld\n", (p) - r);
	trace("op: %d\n", *p);
	while ((op = *(p++))) {
		int pmode_t[8] = {0};
		int *pmode = pmode_t;
		for (int i=0; i < 8; i++) {
			pmode[i] = (op / (int) pow(10, (i + 2))) % 10;
		}
		switch (op % 100) {
			case 1: {
				trace("*%ld = ", (p) - r);
				int val1 = getval(r, *(p++), &pmode);
				trace("+");
				int val2 = getval(r, *(p++), &pmode);
				trace("\n");
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
				trace("*%d = input()(", *p);
				int status = getline(&in, &n, input);
				if (status == -1) {
					eprintf("expecting input!\n");
					exit(1);
				}
				trace("=%d)\n", atoi(in));

				r[*(p++)] = atoi(in);
				if (in) free(in);
				break;
			}
			case 4: {
				trace("output(");
				printf("%d\n", getval(r, *(p++), &pmode));
				trace(")\n");
				break;
			}
			case 5: {
				trace("if ");
				int cond = getval(r, *(p++), &pmode);
				trace("? jump");
				int *loc = r + getval(r, *(p++), &pmode);
				trace("\n");
				trace("loc: %ld\n", loc - r);
				if (cond!=0) {
					p = loc;
				}
				break;
			}
			case 6: {
				int cond = getval(r, *(p++), &pmode);
				int *loc = r + getval(r, *(p++), &pmode);
				if (cond==0) {
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
				eprintf("Unknown op!: %d\n", op);
				exit(0);
			}
		}
		trace("pc: %ld\n", (p) - r);
		trace("op: %d\n", *p);
	}
}


int main(int argc, char *argv[]) {
	int reel[10000] = {
		#ifdef INTPROG
			INTPROG
		#else
			#include "prog.int"
		#endif
	};
	computer(reel, stdin);
	trace("exiting\n");
	return 0;
}
