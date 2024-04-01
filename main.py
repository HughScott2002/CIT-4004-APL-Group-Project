import ply.yacc as yacc
from lexer import tokens

from parser_1 import parser
from semantics import semantic_analyzer
from code_generator import generate_code


def main():
    # Get the source code
    from sourcecode import data as longdata
    from shortsourcecode import data as shortdata

    # Lexing
    # print(tokens)

    # Parsing
    # parser = yacc.yacc()
    print("*" * 50)
    print("Parsing the source code:")
    ast = parser.parse(shortdata)
    print(ast)

    # # Semantic Analysis
    print("*" * 50)
    print("*" * 50)
    print("Performing Semantic Analysis:")
    semantic_analyzer(ast)
    print("*" * 50)

    # # Code Generation
    # code_generator = CodeGenerator()
    print("*" * 50)
    print("Generating Python code:")
    python_code = generate_code(ast)
    print(python_code)
    print("*" * 50)


if __name__ == "__main__":
    main()
