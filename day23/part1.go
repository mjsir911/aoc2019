package main;

import (
	"time"
	"fmt"
)

func main() {
	n := newRouter()
	n.start()

	for (!n.idle()) { time.Sleep(time.Millisecond) }
	fmt.Println(n.nat.y)
}
