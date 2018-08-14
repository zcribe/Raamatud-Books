#lang sicp
(define (square x)(* x x))
(define (square-sum x y z)
  (cond
   ((and (> x y)(> z y)) (+ (square x)(square z)))
   ((and (> y x)(> z x)) (+ (square x)(square z)))
   ((and (> x z)(> y z)) (+ (square x)(square y)))
  ))

(square-sum 1 2 3)