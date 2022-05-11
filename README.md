# Turing_Machine

In this assignment, you will create a simple Turing Machine simulation for the algorithm outlined/demonstrated in this video (Links to an external site.) for testing the membership of strings in the language . The program can be implemented in a language of your choosing, but I prefer: Python, C(++/#), Python, FORTRAN, golang, Rust, Haskell, Ruby, Java, scala, or JavaScript. If you submitted Programming Assignment 1 in another language and didn't get an email asking a lot of questions, that language is also OK. The program should:

Accept a string from command line
Place that string into an array, list, or similar data structure
Implement a read/write head as either a pointer or an int that points to the current position of the head in the data structure.
Use variables (boolean is probably easiest) to represent the control unit
Use a loop to step through each timestep of the computation and print out the result of the computation by indicating where the read/write head is located, what the timestep is (i.e., what iteration is the loop on), and updating the values on the tape to show which symbols have been marked off.
You can use whatever bounds checking you like to terminate the program.
At the end of the computation your program should print "ACCEPT" or "REJECT" if the string is in the language or not in the language respectively.
Test cases (these will literally be the ones the program is graded on). Each test case is worth 10 points out of a total 100 points. If you hard code a program that accepts or rejects these specific strings, you will receive a 0/100.

w = 1010#1010 (ACCEPT)
w = 11111#00000 (REJECT)
w = 1001#1001 (ACCEPT)
w = 1010#0101 (REJECT)
w = 000000001#000000001 (ACCEPT)
w = 1#0 (REJECT)
w = 000111#000111 (ACCEPT)
w = 10100101#1010011 (REJECT)
w = # (ACCEPT)
w = 11#000 (REJECT)
