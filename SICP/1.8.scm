#lang sicp

(define (square x) (* x x)) 

(define (cuberoot x y)
  (/ (+(/ x (* y y)) (* y y)) 3))