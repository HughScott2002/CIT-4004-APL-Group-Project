from symbol_table import *
from parser_1 import parser
from semantic_analyzer import semantic_analyzer
from code_generator import generate_code

# TODO: Add arithmetic operations to the language (Done)
# TODO: Make sure you can assign a variable to another variable (Done)
# TODO: Add conditionals to the language (DONE)
# TODO: Add scope and binding to the language
# TODO: Add params and args to the language
# TODO: Add function return types to the language
# TODO: Add arrays and lists to the language
# TODO: Finish the code generator
# TODO: Create custom errors for the language


def main():
    # Get the source code
    from sourcecode import data as longdata
    from shortsourcecode import data as shortdata

    # Create a global symbol table
    global_symbol_table = SymbolTable()

    print("*" * 50)
    print("Parsing the source code:")
    ast = parser.parse(longdata)
    print(ast)
    print("*" * 50)

    # Semantic Analysis
    print("*" * 50)
    print("Performing Semantic Analysis:")
    semantic_analyzer(ast, global_symbol_table)
    # print(ast)
    print("*" * 50)

    # # Code Generation
    # print("*" * 50)
    # print("Generating Python code:")
    # python_code = generate_code(ast)
    # print(python_code)
    # print("*" * 50)


if __name__ == "__main__":
    main()
