#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include<sys/mman.h>
#include <unistd.h>


#define eprintf(...) fprintf(stderr, __VA_ARGS__)
#ifdef TRACE
	#define trace eprintf
#else
	#define trace(...)
#endif

typedef long word;

#define MEM_SIZE 10000
typedef word mem[MEM_SIZE];
word *getpos(mem m, word v, int mode, int rel_offset) {
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

word getval(mem m, word v, int mode, int rel_offset) {
	switch (mode) {
		case 1: {
			trace("%ld", v);
			return v;
		}
		case 2:
		case 0: {
			word val = *getpos(m, v, mode, rel_offset);
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

int tick(regs *r, mem m, bus input, bus output) {
	trace("%03d: ", r->pc);
	int op = m[r->pc++];
	int pmode_t[8] = {0};
	int *pmode = pmode_t;
	for (int i=0; i < 8; i++) {
		pmode[i] = (op / (int) pow(10, (i + 2))) % 10;
	}
	switch (op % 100) {
		case 1: {
			word val1 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" + ");
			word val2 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" → ");
			*getpos(m, m[r->pc++], *(pmode++), r->sp) = val1 + val2;
			trace("\n");
			break;
		}
		case 2: {
			word val1 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" × ");
			word val2 = getval(m, m[r->pc++], *(pmode++), r->sp);
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
			fflush(output);
			trace("\n");
			break;
		}
		case 5: {
			trace("if ");
			word cond = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace("≠0 ? goto ");
			word loc = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace("\n");
			if (cond!=0) {
				r->pc = loc;
			}
			break;
		}
		case 6: {
			trace("if ");
			word cond = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace("=0 ? goto ");
			word loc = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace("\n");
			if (cond==0) {
				r->pc = loc;
			}
			break;
		}
		case 7: {
			word val1 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" < ");
			word val2 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace(" → ");
			*getpos(m, m[r->pc++], *(pmode++), r->sp) = val1 < val2;
			trace("\n");
			break;
		}
		case 8: {
			word val1 = getval(m, m[r->pc++], *(pmode++), r->sp);
			trace("=");
			word val2 = getval(m, m[r->pc++], *(pmode++), r->sp);
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
			trace("halt\n");
			break;
		}
		default: {
			eprintf("Unknown op!: %d\n", op);
			exit(0);
		}
	}
	return op % 100;
}

void computer(mem m, bus input, bus output) {
	setbuf(input, NULL);
	setbuf(output, NULL);
	regs r = {0, 0};
	// trace("op: %ld\n", *p);
	while (tick(&r, m, input, output) != 99) {}
}

size_t get_csv(FILE *in, char *buf) {
	char c;
	int i;
	for (i=0; (c = fgetc(in)) != ',' && c != EOF; i++) {
		buf[i] = c;
	}
	buf[i] = '\0';
	return i;
}


// stringizing
#define xstr(s) str(s)
#define str(s) #s

int main(int argc, char *argv[]) {
	word *prog;
	int prog_in = 3;

	if (fdopen(prog_in, "w+")) {
		ftruncate(prog_in, MEM_SIZE);
		trace("backing with mmap to &4\n");
		prog = mmap(NULL, MEM_SIZE, PROT_READ|PROT_WRITE,MAP_SHARED, prog_in, 0);
	} else {
		trace("backing to allocd\n");
		prog = calloc(MEM_SIZE, sizeof(word));
	}

	int csv_in = 4;
	FILE *csv_fin;
	if ((csv_fin = fdopen(csv_in, "r"))) {
		trace("loading from csv on &4\n");
		char buf[20];
		for (int i = 0; get_csv(csv_fin, buf); i++) {
			prog[i] = atol(buf);
		}
	} else {
		trace("loading from compile time\n");
		word reel[10000] = {
			#ifdef INTPROG
				INTPROG
			#else
				#include "my.in"
			#endif
		};
		prog = reel;
	};

	#ifdef INPUT
	char tmp[] = xstr(INPUT);
	trace("using compile time input: %s\n", tmp);
	FILE *in = fmemopen(tmp, sizeof(tmp), "r");
	#else
	trace("using input from stdin\n");
	FILE *in = stdin;
	#endif
	computer(prog, in, stdout);
	trace("exiting\n");
	return 0;
}
