# Custom Python Interpreter

## 🚀 Introduction
I created this custom interpreter to explore language design fundamentals and demonstrate how programming languages work under the hood. This project implements a complete interpreted language with variables, control flow, functions, and more - all built from scratch in Python.

[▶️ Try the live demo](https://interpreter-3e9n.onrender.com) | [📜 Full language specification](#language-features)
This document explains how to use the interpreter, a Python-based tool for executing a custom programming language.

## Getting Started

1. Launch the Interpreter:  
   Navigate to the project directory and run:  
   `python3 shell.py`  
   The prompt `www >` will appear, indicating the interpreter is ready.

2. Enter Commands:  
   Type commands directly into the interactive shell. For example:  
   - `print("Hello, World!")` ? Outputs: `Hello, World!`  
   - `set x =: 5 + 3` ? Outputs: `8`  
   - `walk i =: 1 thru 5 do print(i)` ? Outputs numbers 1 to 5.  

3. To run a file:
  Type: run(filename.www) 

4. Exit the Interpreter:  
   Type `exit` to quit.

## Language Features

* Variables: `set x =: 10`  
* Arithmetic: `+, -, *, /, ^^` (e.g., `5 ^^ 2` for power)  
* and and or:
  www > true and false
  false
  www > true and true  
  true
  www > false or true
  true 
* Logical not:
      www > !(6 == 5)
      true
      www > not(5 == 5)
      false
* Loops:  
        walk i =: 1 thru 5 do print(i)` (for-loop)  
  
        print("For loop (walk)")
        walk i =: 0 thru 10 skip 1 do
          print("For loop: " + i)
        end
  
      www > walk i =: 1 thru 10 skip 2 do "hello"
      [hello, hello, hello, hello, hello]
      
      keep x > 0 do set x =: x - 1` (while-loop)  
      
      print("While loop")
      set counter =: 0
      keep counter < 3 do
        print("Counter: " + counter)
        set counter =: counter + 1
      end
  
      set i =: 0
      set a =: []
      keep i < 10 do;
          set i =: i + 1;
          check i == 4 do continue;
          check i == 8 do break;
          set a =: a + i;
      end
      print(i)
      print(a)
      
      www > keep x < 20 do set x =: x + 2
      [12, 14, 16, 18, 20]


* Conditionals:  

      print("If-else")
      set age =: 20
      check age >= 18 do
          check age == 19 do
              print("AGE = 19")
          otherwise
              print("Adult")
          end
      otherwise
        print("Minor")
      end

      www > check x > 10 do print("x is greater than 10") orif x == 10 do print("x is 10") otherwise print("x is less than 10")
          x is 10
          0


* Functions:
      build greet(text) do
      print("Hello, " + text)
      end
      greet("World")
      build add(a, b) -> a + b

* User input:
      print("User input")
      set name =: input_str("Enter your name: ")
      print("Hello " + name)

* List implementation:
      print("List implementation")
      set lst =: [1, "two", false]
      append(lst, 3)
      print(lst)                       
      print(lst + 4)
      print(lst * [3, 4, 5] )
      print(len(lst))  
      print(lst - 1)  
      print(len(lst)) 
      print(lst -- 1)  

* Text with \quotes\
* Text with \\backslashed\\
* Text \nwith \nnewlines
* Text \twith \ttabs
