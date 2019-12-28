#!/usr/bin/env tclsh
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
	switch $dir {
		north {
			lset scoord 1 [expr [lindex $scoord 1] + 1]
		}
		south {
			lset scoord 1 [expr [lindex $scoord 1] - 1]
		}
		east {
			lset scoord 0 [expr [lindex $scoord 0] + 1]
		}
		west {
			lset scoord 0 [expr [lindex $scoord 0] - 1]
		}
	}
	return $scoord
}


proc getlist {fd} {
	while {[string match "- *" [set line [gets $fd]]]} {
		lappend l [string replace $line 0 1]
	}
	return $l
}
proc getfloor {fd {dir ""}} {
	if {![string equal $dir ""]} {
		puts $fd $dir
	}
	set items {};
	while {1} {
		set line [gets $fd]
		switch -glob $line {
			"Command?" {
				break
			}
			"*you are ejected back to the checkpoint." {
				break
			}
			"== * ==" {
				set roomName [string range $line 3 [expr [string length $line] - 4]]
			}
			"Doors here lead:" {
				set dirs [getlist $fd]
			}
			"Items here:" {
				set items [getlist $fd]
			}
			"You can't go that way." {
				puts "err"
				exit 1
			}
		}
	}
	list $roomName $dirs $items
}

proc goto {fd body {dir ""} {pos {0 0}}} {
	set coord [addcord $pos $dir]
	lassign [getfloor $fd $dir] roomName directions items
	eval $body
	if {[string equal "Pressure-Sensitive Floor" $roomName]} {
		getfloor $fd ; # on same floor
		return
	}

	foreach direction $directions {
		if {![string equal [opposite $dir] $direction]} {
			goto $fd $body $direction $coord
		}
	}
	puts $fd [opposite $dir]
	while {![string equal [gets $fd] "Command?"]} { }
}

# while {![string equal [gets $fd] "Command?"]} { }


proc intcode {fdname body} {
	set fd [open "| ./doit.sh" w+]
	fconfigure $fd -buffering line
	set $fdname $fd
	eval $body
}

intcode myfd {
	goto $myfd {
		global allItems
		lappend allItems {*}$items
		# puts "$roomName, $items, $coord, $directions"
	}
}
puts $allItems
