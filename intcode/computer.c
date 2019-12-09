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

long *getpos(long *r, long v, int mode, int rel_offset) {
	switch (mode) {
		case 0:
			trace("*%ld", v);
			return r+v;
		case 2:
			trace("*(rb(=%d)%+ld)", rel_offset, v);
			return r + rel_offset + v;
		default:
			return NULL;
	}
}

long getval(long *r, long v, int mode, int rel_offset) {
	switch (mode) {
		case 1: {
			trace("%ld", v);
			return v;
		}
		case 2:
		case 0: {
			long val = *getpos(r, v, mode, rel_offset);
			trace("(=%ld)", val);
			return val;
		}
		default:
			return 0;
	}
}


#define lenof(l) sizeof(l) / sizeof(l[0])
void computer(long *r, FILE *input) {
	int relative_base = 0;
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
				long val1 = getval(r, *(p++), *(pmode++), relative_base);
				trace("+");
				long val2 = getval(r, *(p++), *(pmode++), relative_base);
				trace("\n");
				*getpos(r, *(p++), *(pmode++), relative_base) = val1 + val2;
				break;
			}
			case 2: {
				long val1 = getval(r, *(p++), *(pmode++), relative_base);
				long val2 = getval(r, *(p++), *(pmode++), relative_base);
				*getpos(r, *(p++), *(pmode++), relative_base) = val1 * val2;
				break;
			}
			case 3: {
				char *in = NULL;
				size_t n = 0;
				trace("*%ld = input()(", *p);
				ssize_t status = getline(&in, &n, input);
				if (status == -1) {
					eprintf("expecting input!\n");
					exit(1);
				}
				trace("=%ld)\n", atol(in));

				*getpos(r, *(p++), *(pmode++), relative_base) = atoi(in);
				if (in) free(in);
				break;
			}
			case 4: {
				trace("output(");
				printf("%ld\n", getval(r, *(p++), *(pmode++), relative_base));
				trace(")\n");
				break;
			}
			case 5: {
				trace("if ");
				long cond = getval(r, *(p++), *(pmode++), relative_base);
				trace("? jump");
				long *loc = r + getval(r, *(p++), *(pmode++), relative_base);
				trace("\n");
				trace("loc: %ld\n", loc - r);
				if (cond!=0) {
					p = loc;
				}
				break;
			}
			case 6: {
				long cond = getval(r, *(p++), *(pmode++), relative_base);
				long *loc = r + getval(r, *(p++), *(pmode++), relative_base);
				if (cond==0) {
					p = loc;
				}
				break;
			}
			case 7: {
				long val1 = getval(r, *(p++), *(pmode++), relative_base);
				long val2 = getval(r, *(p++), *(pmode++), relative_base);
				*getpos(r, *(p++), *(pmode++), relative_base) = val1 < val2;
				break;
			}
			case 8: {
				long val1 = getval(r, *(p++), *(pmode++), relative_base);
				long val2 = getval(r, *(p++), *(pmode++), relative_base);
				*getpos(r, *(p++), *(pmode++), relative_base) = val1 == val2;
				break;
			}
			case 9: {
				trace("relative_base += ");
				relative_base += getval(r, *(p++), *(pmode++), relative_base);
				trace("\n");
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
