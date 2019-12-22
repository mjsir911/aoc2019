#!/usr/bin/env -S awk -f
{ printf $1<120?"%c":"%i", $1 }
