#!/usr/bin/env -S csi -q
(require-extension srfi-1)

(load "part1.scm")

(define (graph-find t k)
	(if (equal? k (car t))
		(list k)
		(let [(r (filter (compose not null?)(map (lambda (n) (graph-find n k)) (cdr t))))]
			(if (null? r)
				r
				(cons (car t) (car r))))))


(define (diff l1 l2)
	(if (equal? (car l1) (car l2))
		(cons (car l1) (diff (cdr l1) (cdr l2)))
		'()))

(define (graph-get t k)
	(if (equal? (car t) (car k))
		(if (null? (cdr k))
			t
			(graph-get (assoc (cadr k) (cdr t)) (cdr k)))))

(define neighborhood-path (diff (graph-find orbits 'YOU) (graph-find orbits 'SAN)))
(define neighborhood (graph-get orbits neighborhood-path))
(display "\n")
(display (+ -4
            (length (graph-find neighborhood 'YOU))
            (length (graph-find neighborhood 'SAN))))
