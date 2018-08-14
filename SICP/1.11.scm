#lang sicp


;;; f(n) = n if n<3 and f(n) = f(n - 1) + 2f(n - 2) + 3f(n - 3) if n> 3

;;; Recursive

(define (f n)(cond ((< n 3) n)
                   (else (> n 3) (+ (f(- n 1))
                               (* 2 (f(- n 2)))
                               (* 3 (f(- n 3)))))
                   ))

;;; Iterative
(define (g n)(cond ((< n 3) n)
                   (else (> n 3)(3))))


(define (h n) 
  (define (iter a b c count) 
    (if (= count 0) 
        a 
        (iter b c (+ c (* 2 b) (* 3 a)) (- count 1)))) 
  (iter 0 1 2 n)) 

(define (j n) (fi n 0 1 2)) 
  
(define (fi i a b c) 
  (cond ((< i 0) i) 
        ((= i 0) a) 
        (else (fi (- i 1) b c (+ c (* 2 b) (* 3 a)))))) 


(f 4)



