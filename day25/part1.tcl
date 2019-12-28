#!/usr/bin/env tclsh
set fd [open "| ./doit.sh" w+]
fconfigure $fd -buffering line


proc opposite {dir} {
	switch $dir {
		north {
			return south
		}
		south { 
			return north
		}
		east {
			return west
		}
		west {
			return east
		}
	}
}

proc addcord {scoord dir} {
	array set coord "$scoord"
	switch $dir {
		north {
			incr coord(y)
		}
		south {
			incr coord(y) -1
		}
		east {
			incr coord(x)
		}
		west {
			incr coord(x) -1
		}
	}
	return [array get coord]
}



proc goto {fd dir pos} {
	array set coord [addcord $pos $dir]
	puts $fd $dir
	while {[string equal [set roomName [gets $fd]] ""]} {}
	puts "$roomName, $coord(x), $coord(y)"
	if {[string match "*Pressure-Sensitive Floor*" $roomName]} {
		while {![string equal [gets $fd] "Command?"]} { }
		return
	}

	set i 0
	while {![string equal [set line [gets $fd]] "Doors here lead:"]} {}
	while {[string match "- *" [set line [gets $fd]]]} {
		set directions($i) [string replace $line 0 1];
		incr i
	}
	while {![string equal [gets $fd] "Command?"]} { }

	for { set j 0 }  { $j < [array size directions] }  { incr j } {
		if {![string equal [opposite $dir] $directions($j)]} {
			goto $fd $directions($j) [array get coord]
		}
  }
	puts $fd [opposite $dir]
	while {![string equal [gets $fd] "Command?"]} { }
}

while {![string equal [gets $fd] "Command?"]} { }

goto $fd west "x 0 y 0"
