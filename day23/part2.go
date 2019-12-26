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



type packet struct{x int; y int}
type nic struct {comm chan packet; id int; idle bool}
type router struct {
	network []nic;
	nat packet;
}

func (r *router) route(to int, p packet) {
	// fmt.Printf("(%d, %d) → %d\n", p.x, p.y, to)
	if to == 255 {
		r.nat = p
	} else {
		r.network[to].comm <- p
	}
}

func (r *router) idle() (ret bool) {
	ret = true
	//for i := 1; i < 2; i++ {
	for i := range r.network {
		ret = ret && r.network[i].idle 
	}
		//time.Sleep(time.Millisecond)
	//}
	return
}

func (r router) resume() {
	r.network[0].comm <- r.nat
	time.Sleep(time.Millisecond)
}

func (p packet) String() string {
	return fmt.Sprintf("%d\n%d\n", p.x, p.y)
}

func (n nic) dispatch(r *router) (out io.Writer) {
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
			// fmt.Printf("%d: ", n.id)
			r.route(dest, packet{x, y})
		}
	}()
	return
}

func (n *nic) recieve(r router) (in io.Reader) {
	in, w := io.Pipe()
	go func() {
		for {
			select {
			case p, ok := <- n.comm:
				if ok {
					n.idle = false
					// fmt.Printf("%d ← (%d, %d)\n", n.id, p.x, p.y);
					fmt.Fprint(w, p.String())
					time.Sleep(time.Millisecond * 5)
				} else {
					log.Fatal("error!");
				}
			default:
				fmt.Fprint(w, "-1\n")
				time.Sleep(time.Millisecond) // give it some breathing room
				n.idle = true
			}
		}
	}()
	return
}

func (n *nic) start(r *router) {
	cmd := exec.Command("./computer")
	cmd.Stdin = io.MultiReader(
		strings.NewReader(strconv.Itoa(n.id) + "\n"),
		n.recieve(*r),
	)
	cmd.Stdout = n.dispatch(r)
	// cmd.Stderr = os.Stderr

	file, _ := os.Open("my.in")
	cmd.ExtraFiles = make([]*os.File, 10)
	cmd.ExtraFiles[4 - 3] = file

	go cmd.Run()
}

func main() {
	test := router{make([]nic, 50), packet{0, -1}}
	for i := range test.network {
		test.network[i] = nic{make(chan packet, 1000), i, false};
	}
	for i := range test.network {
		test.network[i].start(&test)
	}

	seen := make(map[int]struct{})
	for {
		for (!test.idle()) { time.Sleep(time.Millisecond) }
		time.Sleep(time.Millisecond * 5)

		_, ok := seen[test.nat.y]
		if ok {
			fmt.Println(test.nat.y)
			break
		}
		seen[test.nat.y] = struct{}{}
		test.resume()
		// if test.idle() {
		// 	break
		// }
	}

	// for (!test.idle()) { time.Sleep(time.Millisecond) }
	// fmt.Println(test.nat);
	// test.network[0].comm <- packet{1151, 22074}
}
