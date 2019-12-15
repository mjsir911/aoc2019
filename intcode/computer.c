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
void computer(long *r, FILE *input, FILE *output) {
	int relative_base = 0;
	long *p = r;
	long op;
	trace("%03ld: ", (p) - r);
	// trace("op: %ld\n", *p);
	while ((op = *(p++))) {
		int pmode_t[8] = {0};
		int *pmode = pmode_t;
		for (int i=0; i < 8; i++) {
			pmode[i] = (op / (int) pow(10, (i + 2))) % 10;
		}
		switch (op % 100) {
			case 1: {
				long val1 = getval(r, *(p++), *(pmode++), relative_base);
				trace(" + ");
				long val2 = getval(r, *(p++), *(pmode++), relative_base);
				trace(" → ");
				*getpos(r, *(p++), *(pmode++), relative_base) = val1 + val2;
				trace("\n");
				break;
			}
			case 2: {
				long val1 = getval(r, *(p++), *(pmode++), relative_base);
				trace(" × ");
				long val2 = getval(r, *(p++), *(pmode++), relative_base);
				trace(" → ");
				*getpos(r, *(p++), *(pmode++), relative_base) = val1 * val2;
				trace("\n");
				break;
			}
			case 3: {
				char *in = NULL;
				size_t n = 0;
				trace("input()(");
				ssize_t status = getline(&in, &n, input);
				if (status == -1) {
					eprintf("expecting input!\n");
					exit(1);
				}
				trace("=%ld) → ", atol(in));
				*getpos(r, *(p++), *(pmode++), relative_base) = atoi(in);
				trace("\n");

				if (in) free(in);
				break;
			}
			case 4: {
				trace("output(");
				fprintf(output, "%ld", getval(r, *(p++), *(pmode++), relative_base));
				trace("): ");
				printf("\n");
				break;
			}
			case 5: {
				trace("if ");
				long cond = getval(r, *(p++), *(pmode++), relative_base);
				trace("≠0 ? goto ");
				long *loc = r + getval(r, *(p++), *(pmode++), relative_base);
				trace("\n");
				if (cond!=0) {
					p = loc;
				}
				break;
			}
			case 6: {
				trace("if ");
				long cond = getval(r, *(p++), *(pmode++), relative_base);
				trace("=0 ? goto ");
				long *loc = r + getval(r, *(p++), *(pmode++), relative_base);
				trace("\n");
				if (cond==0) {
					p = loc;
				}
				break;
			}
			case 7: {
				long val1 = getval(r, *(p++), *(pmode++), relative_base);
				trace(" < ");
				long val2 = getval(r, *(p++), *(pmode++), relative_base);
				trace(" → ");
				*getpos(r, *(p++), *(pmode++), relative_base) = val1 < val2;
				trace("\n");
				break;
			}
			case 8: {
				long val1 = getval(r, *(p++), *(pmode++), relative_base);
				trace("=");
				long val2 = getval(r, *(p++), *(pmode++), relative_base);
				trace(" → ");
				*getpos(r, *(p++), *(pmode++), relative_base) = val1 == val2;
				trace("\n");
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
		trace("%03ld: ", (p) - r);
		// trace("op: %ld\n", *p);
	}
}


// stringizing
#define xstr(s) str(s)
#define str(s) #s

int main(int argc, char *argv[]) {
	long reel[10000] = {
		#ifdef INTPROG
			INTPROG
		#else
			#include "my.in"
		#endif
	};
	#ifdef INPUT
	char tmp[] = xstr(INPUT);
	FILE *in = fmemopen(tmp, sizeof(tmp), "r");
	#else
	FILE *in = stdin;
	#endif
	computer(reel, in, stdout);
	trace("exiting\n");
	return 0;
}
