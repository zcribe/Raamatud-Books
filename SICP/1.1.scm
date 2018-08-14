#lang sicp
10
(+ 5 3 4);;;12
(- 9 1);;;8
(/ 6 2);;;3
(+ (* 2 4) (- 4 6));;;6
(define a 3)
(define b (+ a 1))
(+ a b (* a b));;;19
(= a b);;;#f
(if (and (> b a) (< b (* a b)));;; 4 3 ?7
    b
    a)
(cond ((= a 4) 6);;;#f
      ((= b 4) (+ 6 7 a));;;#t 16
      (else 25))
(+ 2 (if (> b a) b a));;; 9 ! Esimene on if teine on else
(* (cond ((> a b) a) ;;; #f
         ((< a b) b) ;;; #t
         (else -1))
   (+ a 1)) ;;;16