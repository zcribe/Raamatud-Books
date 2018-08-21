// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.

(INIT)
    @SCREEN // Screen address alias
        D=A
    @PIXEL
        M=D

(MAINLOOP)
    @KBD // Keyboard address alias
        D=M
        
    @BLACK
        D;JNE
    @WHITE // Default
        0;JMP
        
(BLACK)
    @PIXEL // Pixel addition
        D=M
        M=M+1
        A=D
        M=-1
    @KBD // Last screenmap bit
        D=A-D
    @INIT // Reset
        D;JEQ
    @MAINLOOP
        0;JMP
        

(WHITE)
    @PIXEL
        D=M
        M=M+1
        A=D
        M=0
    @KBD
        D=A-D
    @INIT
        D;JEQ
    @MAINLOOP
        0;JMP
        

