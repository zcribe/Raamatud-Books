// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@R2
M=0
@R1
D=M
@counter
M=D

(Loop)
@R1 // Neg, Pos kontroll
D=M
@Negative
D;JLT
@Endless
D;JEQ


@R0 // Liitmis Loop
D=M
@R2
M=M+D
@counter
M=M-1
D=M
@Loop // Loop jump kui pole 0
D;JGT
@Endless
D;JEQ

(Negative)
@R0 // Lahutamise Loop
D=M
@R2
M=M-D
@counter
M=M+1
D=M
@Loop // Loop jump kui pole 0
D;JLT
@Endless
D;JEQ


@Endless
(Endless)
0;JMP