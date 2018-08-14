#lang sicp

(define (p) (p))

(define (test x y)
  (if (= x 0)
      0
      y))

(test 0 (p))

;;; Applicative order creates infinite loop.
;;; Normal order returns a 0.
  
