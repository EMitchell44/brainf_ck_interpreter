# brainf_ck_interpreter
## A Brainfuck interpreter written in Python

This is my first dive into any esoteric language as well as writing interpreters of any kind. Brainfuck was designed in 1993 by Urban
Müller (to make a German ü sound, pronounce oo and ee simultaneously) with the goal of writing the smallest compiler possible. Müller's original compiler had a size of only 296 bytes; since then, he's managed to write a compiler less than 200 bytes in size. In a heart-wrenching betrayal of the revered Brainfuck tradition, the files on this interpreter add up to 3,128 bytes, not including dependencies. It would seem I have some catching up to do if I ever want to be a real hacker.

### Brainfuck 101
Brainfuck consists only of an array of memory cells (each containing one byte), an instruction pointer (which points to the next instruction to be executed), a data pointer (which points to a memory cell), and eight simple instructions:

  ```>``` : Increment the data pointer.  
  ```<``` : Decrement the data pointer.  
  ```+``` : Increment the byte at the data pointer.  
  ```-``` : Decrement the byte at the data pointer.  
  ```,``` : Accept one byte of input, storing its value in the cell at the data pointer. This is usually done by getting the byte value of one ASCII character.  
  ```.``` : Output the byte at the data pointer as a character by its ASCII value.  
  ```[``` : Skip to the matching ```]``` instruction if the byte at the data pointer is zero.  
  ```]``` : Go back to the matching ```[``` instruction if the byte at the data pointer is not zero.  

All other characters are ignored. These eight instructions are enough to make the language Turing complete; theoretically, Brainfuck can be used to compute any function, given enough memory.

### Using This Interpreter
Though most Brainfuck compilers and interpreters start with an array of 30,000 cells, this interpreter creates cells on the fly as needed.

To use, start by creating a Brainfuck interpreter object:


```
bf = Brainfuck()
```
___
From there, brainfuck can be exectued using the ```main()``` function, used like ```bf.main("code goes here")```. It returns the output of the Brainfuck code.

Input:
```
print(bf.main("++++++++[->+++++++++<]>.<++++++[->+++++<]>-.+++++++..+++.<+++++++[->----------<]>+++.<+++[->----<]>.<+++++[->+++++++++++<]>.<++++++[->++++<]>.+++.------.--------.<++++++++[->--------<]>---."))
```

Output:  
```
Hello, World!
```
___

The ```show_cells()``` function automatically prints the current byte value in each cell.

Input:
```
bf.show_cells()
```

Output:  
```
[0x00] [0x21]
```
___
### It's dangerous to go alone! Take this.
[https://www.ascii-code.com/](https://www.ascii-code.com/)
