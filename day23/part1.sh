function nic() {
	(echo $1; while true; do
		if ! timeout 0.1 cat $1; then
			echo -1
		fi
	done) | ./computer | while read -r dest; do
		read -r x
		read -r y
		echo "$1: ($x, $y) → $dest" >&2
		(echo $x; echo $y) > $dest
	done
}
for i in $(seq 0 49); do
	mkfifo $i 2> /dev/null
	nic $i 4<my.in &
done

sleep 100
