#!/usr/bin/env -S csi -q

(load "shared.scm")

(define (part1 t) ; returns cons of all connects & # of nodes within
	(let [(r (map part1 (cdr t)))]
		(cons
			(+ (sum (map cdr r)) (sum (map car r)) (length r)) ; # of all connections
			(+ (sum (map cdr r)) (length r))))) ; # of nodes within

(display (car (part1 orbits))) ; only get # of all connections


