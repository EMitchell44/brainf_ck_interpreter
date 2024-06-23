# brainfuck_interpreter
## A Brainfuck interpreter written in Python

This is my first dive into any esoteric language as well as writing interpreters of any kind. Brainfuck was designed in 1993 by Urban
Müller with the goal of writing the smallest compiler possible. Müller's original compiler had a size of only 296 bytes; since then, he's managed to write a compiler less than 200 bytes in size.

### Brainfuck 101
Brainfuck consists only of an array of memory cells, an instruction pointer (which points to the next instruction to be executed), a data pointer (which points to a memory cell), and eight simple commands:

  ```>``` : increment the data pointer  
  ```<``` : decrement the data pointer  
  ```+``` : increment the byte at the data pointer  
  ```-``` : decrement the byte at the data pointer  
  ```,``` : accept one byte of input, storing its value in the cell at the data pointer. This is usually done by getting the byte value of one ASCII character.  
  ```.``` : output the byte at the data pointer  
  ```[``` : skip to the matching ```]``` instruction if the byte at the data pointer is zero  
  ```]``` : go back to the matching ```[``` instruction if the byte at the data pointer is not zero.  

All other characters are ignored. These eight commands are enough to make the language Turing complete; theoretically, Brainfuck can be used to compute any function, given enough memory.

### Using This Interpreter
Though most Brainfuck compilers and interpreters start with an array of 30,000 cells, this interpreter creates cells on the fly as needed.

To use, start by creating a Brainfuck interpreter object:


```bf = Brainfuck()```

From there, brainfuck can be exectued using the ```main()``` function, used like ```bf.main("code goes here")```.

```
print(bf.main("++++++++[->+++++++++<]>.<++++++[->+++++<]>-.+++++++..+++.<+++++++[->----------<]>+++.<+++[->----<]>.<+++++[->+++++++++++<]>.<++++++[->++++<]>.+++.------.--------.<++++++++[->--------<]>---."))
```

Output:  
```Hello, World!```

The ```show_cells()``` function shows the current byte value in each cell.

```
bf.show_cells()
```

Output:  
```[0x00] [0x21]```
