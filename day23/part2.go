package main;

import (
	"time"
	"fmt"
)

func main() {
	n := newRouter()
	n.start()

	seen := make(map[int]struct{})
	for {
		for (!n.idle()) { time.Sleep(time.Millisecond) }
		time.Sleep(time.Millisecond * 5)

		_, ok := seen[n.nat.y]
		if ok {
			fmt.Println(n.nat.y)
			break
		}
		seen[n.nat.y] = struct{}{}
		n.resume()
	}
}
