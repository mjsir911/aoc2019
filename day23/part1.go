package main;
import (
	"os/exec";
	"log";
	"fmt";
	"strings";
	"strconv";
	"os";
	"io";
	"bufio";
	"time";
);



type packet struct{x int; y int};
type router [](chan packet);

func (p packet) String() string {
	return fmt.Sprintf("%d\n%d\n", p.x, p.y)
}

func (r router) dispatcher(i int) (out io.Writer) {
	in, out := io.Pipe()
	ins := bufio.NewScanner(in)
	go func() {
		for ins.Scan() {
			dest, err := strconv.Atoi(ins.Text())
			if err != nil { log.Fatal("uhoh") }
			ins.Scan()
			x, err := strconv.Atoi(ins.Text())
			if err != nil { log.Fatal("uhoh") }
			ins.Scan()
			y, err := strconv.Atoi(ins.Text())
			if err != nil { log.Fatal("uhoh") }
			fmt.Printf("%d: (%d, %d) → %d\n", i, x, y, dest)
			if dest == 255 {
				fmt.Printf("\n\n(%d, %d) %s\n\n", x, y, ins.Text());
			} else {
				r[dest] <- packet{x, y}
			}
		}
	}()
	return
}

func (r router) reciever(i int) (in io.Reader) {
	in, w := io.Pipe()
	go func() {
		for {
			select {
			case p, ok := <- r[i]:
				if ok {
					_ = p;
					fmt.Printf("%d ← (%d, %d)\n", i, p.x, p.y);
					fmt.Fprint(w, p.String())
				} else {
					log.Fatal("error!");
				}
			default:
				fmt.Fprint(w, "-1\n")
				time.Sleep(100000)
			}
		}
	}()
	return
}

func nic(r router, id int) {
	cmd := exec.Command("./computer")
	cmd.Stdin = io.MultiReader(
		strings.NewReader(strconv.Itoa(id) + "\n"),
		r.reciever(id),
	)
	cmd.Stdout = r.dispatcher(id)
	// cmd.Stderr = os.Stderr

	file, _ := os.Open("my.in")
	cmd.ExtraFiles = make([]*os.File, 10)
	cmd.ExtraFiles[4 - 3] = file

	go cmd.Run()
}

func main() {
	test := make(router, 50)
	for i := range test {
		test[i] = make(chan packet, 1000);
	}
	for i := range test {
		nic(test, i)
	}
	time.Sleep(time.Second)
}
