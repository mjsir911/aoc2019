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

typedef long mem[10000];
long *getpos(mem m, long v, int mode, int rel_offset) {
	switch (mode) {
		case 0:
			trace("*%ld", v);
			return &m[v];
		case 2:
			trace("*(rb(=%d)%+ld)", rel_offset, v);
			return &m[rel_offset + v];
		default:
			return NULL;
	}
}

long getval(mem m, long v, int mode, int rel_offset) {
	switch (mode) {
		case 1: {
			trace("%ld", v);
			return v;
		}
		case 2:
		case 0: {
			long val = *getpos(m, v, mode, rel_offset);
			trace("(=%ld)", val);
			return val;
		}
		default:
			return 0;
	}
}

typedef struct {
	int pc;
	int sp;
} regs;

typedef FILE *bus;

regs *tick(regs *r, mem m, bus input, bus output) {
	trace("%03d: ", r->pc);
	int op = m[r->pc++];
	int pmode_t[8] = {0};
	int *pmode = pmode_t;
	for (int i=0; i < 8; i++) {
		pmode[i] = (op / (int) pow(10, (i + 2))) % 10;
	}
	switch (op % 100) {
		case 1: {
			long val1 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" + ");
			long val2 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" → ");
			*getpos(m, m[r->pc++], *(pmode++), r->sp) = val1 + val2;
			trace("\n");
			break;
		}
		case 2: {
			long val1 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" × ");
			long val2 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" → ");
			*getpos(m, m[r->pc++], *(pmode++), r->sp) = val1 * val2;
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
			*getpos(m, m[r->pc++], *(pmode++), r->sp) = atoi(in);
			trace("\n");

			if (in) free(in);
			break;
		}
		case 4: {
			trace("output(");
			fprintf(output, "%ld", getval(m, m[r->pc++], *(pmode++), r->sp));
			trace("): ");
			fprintf(output, "\n");
			break;
		}
		case 5: {
			trace("if ");
			long cond = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace("≠0 ? goto ");
			long loc = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace("\n");
			if (cond!=0) {
				r->pc = loc;
			}
			break;
		}
		case 6: {
			trace("if ");
			long cond = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace("=0 ? goto ");
			long loc = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace("\n");
			if (cond==0) {
				r->pc = loc;
			}
			break;
		}
		case 7: {
			long val1 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" < ");
			long val2 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" → ");
			*getpos(m, m[r->pc++], *(pmode++), r->sp) = val1 < val2;
			trace("\n");
			break;
		}
		case 8: {
			long val1 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace("=");
			long val2 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" → ");
			*getpos(m, m[r->pc++], *(pmode++), r->sp) = val1 == val2;
			trace("\n");
			break;
		}
		case 9: {
			trace("r->sp += ");
			r->sp += getval(m, m[r->pc++], *(pmode++), r->sp);
			trace("\n");
			break;
		}
		case 99: {
			break;
		}
		default: {
			eprintf("Unknown op!: %d\n", op);
			exit(0);
		}
	}
	return r;
}

#define lenof(l) sizeof(l) / sizeof(l[0])
void computer(mem m, bus input, bus output) {
	setbuf(input, NULL);
	setbuf(output, NULL);
	regs r = {0, 0};
	// trace("op: %ld\n", *p);
	while ((m[r.pc] % 100) != 99) {
		trace("{.pc=%d, .sp=%d}", r.pc, r.sp);
		tick(&r, m, input, output);
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
