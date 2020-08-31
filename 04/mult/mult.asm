// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.


//init storage to 0
@0
    D = A
@R2
    M = D

//add R0 to R2, R1 times
(LOOP)
    //reduce counter by 1
    @R1
        M = M-1
        D = M
    //end loop if counter <0
    @END
        D;JLT

    //add R0 to R2
    @R0
        D = M
    @R2
        M = M + D

    //loop back
    @LOOP
        0;JMP

(END)
    @END
        0;JMP