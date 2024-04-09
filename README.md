### CIT-4004-APL-Group-Project

# Authors:

# Hugh Scott

# Barrington Patterson

# Sharethia McCarthy

# Christina Wilson

## TypeSnake

TypeSnake is a statically-typed, functional programming language inspired by Python and TypeScript. It aims to bring the simplicity and readability of Python while providing the benefits of static typing and modern language features.

## Getting Started

1. **Run locally**: run pip install, then run python main.py

2. **Run as server backend**: run pip install, then run app.py

## Features

- **Static Typing**: TypeSnake uses a powerful type inference system, allowing you to mix dynamic and static code as needed.
- **Block Scope**: Variables in TypeSnake follow block scope rules, ensuring better control over variable lifetimes and preventing accidental name clashes.
- **Modern Syntax**: TypeSnake features a clean and expressive syntax inspired by Python, with additions like type annotations.
- **Functional Programming**: TypeSnake supports first-class functions, lambda expressions, and other functional programming concepts.
- **Exception Handling**: TypeSnake provides a familiar try/except syntax for handling exceptions.

## Test the program in part or as a whole

Use the file structure below for the files mentions

There are 2 files with source code
shortsourcecode has each implemented feature, the file comments out all the implemented parts for you
to test individually.

    for a longer code to run a sample program use the sourcecode.py

    Feel free to add your own✌🏾

Test Tokens: 1. go to the lexer.py file and go to the bottom 2. you will see a comment pointing to the test code

## File Structure

The TypeSnake project has the following file structure:
`(root)/`: This directory contains the main source code of your application. - `app.py`: The server implementation and entry point. - `main.py`: The main file for localing running application. - `lexer.py`: This module handles the lexical analysis of the source code, tokenizing it into a stream of tokens. - `parser_1.py`: This module implements the parser for the language, taking the token stream and building an abstract syntax tree (AST) based on the language's grammar rules. - `semantic_analyzer.py`:This module performs semantic analysis on the AST, ensuring that the code is semantically correct and resolving symbols, types, and other semantic information. - `symbol_table.py`: This module manages the symbol table, which stores information about identifiers, abstracts their types, and their scopes. - `code_generator.py`: This module generates executable code (e.g., bytecode, machine code, or intermediate representation) from the AST and semantic information. - `sourcecode.py`: This module represents the source code of the program being compiled or interpreted. - `requirements.txt`: This file lists the external dependencies required by the project. - `shortsourcecode.py`: This module provides a compact representation of the source code, potentially used for debug purposes or code analysis.

## Resources

- [TypeSnake Documentation](https://docs.google.com/document/d/1HaJzZFqHK1ZdScXy_jM797ikMFCdwXuMlkATgj-Xj2U/edit?usp=sharing)
- [TypeSnake Website](https://apl-web-ui.vercel.app/)
