#!/usr/bin/env -S csi -q
(require-extension srfi-1)

; read from input
(define (read-from-stdin)
	(let ([line (read-line)])
		(if (eof-object? line) ; the test is fine
				'()
				(cons line (read-from-stdin)))))
; have big list from input
(define input 
		; create a pair for each line of input
		(map (lambda (l) (map string->symbol (string-split l ")"))) (read-from-stdin) ))

; (display input)
; (display "\n")
(define (list->graph t root)
	(cons root (map (lambda (n) (list->graph t (cadr n))) (filter (lambda (n) (equal? (car n) root)) t))))

(define orbits (list->graph input 'COM))

(define ((compose f g) x) (f (g x)))
(define (sum l)
	(reduce + 0 l))

(define (part1 t) ; returns cons of all connects & # of nodes within
	(let [(r (map part1 (cdr t)))]
		(cons
			(+ (sum (map cdr r)) (sum (map car r)) (length r)) ; # of all connections
			(+ (sum (map cdr r)) (length r))))) ; # of nodes within

(display (car (part1 orbits))) ; only get # of all connections


