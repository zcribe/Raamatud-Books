#lang sicp

(define (percent x y)(* (/ x y) 100))

(define (square x)
  (* x x))

(define (sqrt x) 
  (sqrt-iter 1.0 2.0 x)) 
  
(define (improve guess x)
  (average guess (/ x guess)))

(define (average x y)
  (/ (+ x y) 2))

 (define (good-enough? guess oldguess) 
   (< (abs (- guess oldguess)) 
      (* guess 0.001))) 

 (define (sqrt-iter guess oldguess x) 
   (if (good-enough? guess oldguess) 
       guess 
       (sqrt-iter (improve guess x) guess 
                  x)))

(sqrt-iter 6 8 10)

;;; The core problem with standard good-enough is the arbitrary quality standard. It does not
;;; account for the size of the number. Thus creating needlessy wasteful or impercise numbers.