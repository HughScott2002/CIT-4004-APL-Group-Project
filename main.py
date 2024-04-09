from symbol_table import *
from parser_1 import parser
from semantic_analyzer import semantic_analyzer
from code_generator import generate_code


def main():
    # Get the source code
    from sourcecode import data as longdata
    from shortsourcecode import data as shortdata

    # Create a global symbol table
    global_symbol_table = SymbolTable()
    print("*" * 50)
    print("Parsing the source code:")
    # Parse the long data
    ast = parser.parse(shortdata)  # Change this to longdata to test all the features
    print(ast)
    print("*" * 50)

    # Semantic Analysis
    print("*" * 50)
    print("Performing Semantic Analysis:")
    semantic_analyzer(ast, global_symbol_table)
    print("*" * 50)

    # Code Generation/Complier
    print("*" * 50)
    print("Generating Python code:")
    python_code = generate_code(ast)
    exec(python_code)
    print("*" * 50)


if __name__ == "__main__":
    main()
