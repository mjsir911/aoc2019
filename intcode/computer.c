#include <stdio.h>
#include <math.h>
#include <stdlib.h>

#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#ifdef TRACE
	#define trace eprintf
#else
	#define trace(...)
#endif

void print_reel(size_t n, long reel[n]) {
	printf("[");
	for (long *i = reel; i < reel + n; i++) {
		printf("%ld, ", *i);
	}
	printf("]\n");
}

long getval(long *r, long v, int **mode) {
	switch (*((*mode)++)) {
		case 1:
			trace(" %ld ", v);
			return v;
		case 0:
			trace(" *%ld(=%ld) ", v, r[v]);
			return r[v];
	}
}

#define lenof(l) sizeof(l) / sizeof(l[0])
void computer(long *r, FILE *input) {
	long *p = r;
	long op;
	trace("pc: %ld\n", (p) - r);
	trace("op: %ld\n", *p);
	while ((op = *(p++))) {
		int pmode_t[8] = {0};
		int *pmode = pmode_t;
		for (int i=0; i < 8; i++) {
			pmode[i] = (op / (int) pow(10, (i + 2))) % 10;
		}
		switch (op % 100) {
			case 1: {
				trace("*%ld = ", (p) - r);
				long val1 = getval(r, *(p++), &pmode);
				trace("+");
				long val2 = getval(r, *(p++), &pmode);
				trace("\n");
				r[*(p++)] = val1 + val2;
				break;
			}
			case 2: {
				long val1 = getval(r, *(p++), &pmode);
				long val2 = getval(r, *(p++), &pmode);
				r[*(p++)] = val1 * val2;
				break;
			}
			case 3: {
				char *in = NULL;
				size_t n = 0;
				trace("*%ld = input()(", *p);
				long status = getline(&in, &n, input);
				if (status == -1) {
					eprintf("expecting input!\n");
					exit(1);
				}
				trace("=%ld)\n", atol(in));

				r[*(p++)] = atoi(in);
				if (in) free(in);
				break;
			}
			case 4: {
				trace("output(");
				printf("%ld\n", getval(r, *(p++), &pmode));
				trace(")\n");
				break;
			}
			case 5: {
				trace("if ");
				long cond = getval(r, *(p++), &pmode);
				trace("? jump");
				long *loc = r + getval(r, *(p++), &pmode);
				trace("\n");
				trace("loc: %ld\n", loc - r);
				if (cond!=0) {
					p = loc;
				}
				break;
			}
			case 6: {
				long cond = getval(r, *(p++), &pmode);
				long *loc = r + getval(r, *(p++), &pmode);
				if (cond==0) {
					p = loc;
				}
				break;
			}
			case 7: {
				long val1 = getval(r, *(p++), &pmode);
				long val2 = getval(r, *(p++), &pmode);
				r[*(p++)] = val1 < val2;
				break;
			}
			case 8: {
				long val1 = getval(r, *(p++), &pmode);
				long val2 = getval(r, *(p++), &pmode);
				r[*(p++)] = val1 == val2;
				break;
			}
			case 99: {
				return;
				break;
			}
			default: {
				eprintf("Unknown op!: %ld\n", op);
				exit(0);
			}
		}
		trace("pc: %ld\n", (p) - r);
		trace("op: %ld\n", *p);
	}
}


int main(int argc, char *argv[]) {
	long reel[10000] = {
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
