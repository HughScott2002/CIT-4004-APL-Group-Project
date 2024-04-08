from flask import Flask, request, jsonify
from symbol_table import *
from parser_1 import parser
from semantic_analyzer import semantic_analyzer
from code_generator import generate_code
import io, sys

# TODO: Add arithmetic operations to the language (Done)
# TODO: Make sure you can assign a variable to another variable (Done)
# TODO: Add conditionals to the language (DONE)
# TODO: Add scope and binding to the language (Done)
# TODO: Add params and args to the language (Done)
# TODO: Finish the code generator (Fix the symbol table and the expression generator)
# TODO: Finish the server backend
# TODO: Create custom errors for the language
# TODO: Add function return types to the language (Made room for it)
# TODO: Add arrays and lists to the language

app = Flask(__name__)
allowed_origins = ["https://apl-web-ui.vercel.app", "*"]

CORS(app, origins=allowed_origins)

@app.route("/generate_code", methods=["POST"])
def parse_code():
    global_symbol_table = SymbolTable()
    input_code = request.json.get("code")
    print(input_code)

    # Parse the input code
    try:
        ast = parser.parse(input_code)
    # ast = parser.parse(input_code)
    except Exception as e:
        response = {"error": str(e)}
        return jsonify(response)

    try:
        # Perform Semantic Analysis
        semantic_analyzer(ast, global_symbol_table)
    except Exception as e:
        response = {"error": str(e)}
        return jsonify(response)
    # Generate Python code
    python_code = generate_code(ast)

    output = io.StringIO()
    sys.stdout = output
    exec(python_code)
    sys.stdout = sys.__stdout__
    printed_output = output.getvalue()
    response = {"python_code": printed_output}
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)
# def main():
#     # Get the source code
#     from sourcecode import data as longdata
#     from shortsourcecode import data as shortdata

#     # Create a global symbol table
#     global_symbol_table = SymbolTable()
#     # print("*" * 50)
#     # print("Parsing the source code:")
#     ast = parser.parse(longdata)
#     # print(ast)
#     # print("*" * 50)

#     # Semantic Analysis
#     # print("*" * 50)
#     # print("Performing Semantic Analysis:")
#     # function_scope = new_scope(global_symbol_table)
#     semantic_analyzer(ast, global_symbol_table)
#     # computed_symbols = global_symbol_table.get_all_symbols()

#     # function_symbols = function_scope.get_all_symbols()
#     # function_scope_symbols = function_scope.get_all_symbols()
#     # print(function_scope.get_all_symbols()["_A"].value)
#     # print(computed_symbols["_A"].value)
#     # print(computed_symbols)
#     # print(function_symbols)

#     # var = computed_symbols["_Inside_Attempt"]
#     # print(f"Name: {var.name}")
#     # global_symbol_table.print_child_scopes()
#     # inside_attempt_symbol = "_Inside_Attempt"
#     # insert_symbol = global_symbol_table.insert(
#     #     VariableSymbol(inside_attempt_symbol, "bool", True, True)
#     # )
#     # variable_symbol = computed_symbols[inside_attempt_symbol]
#     # print("Variable Symbol: ", variable_symbol, type(variable_symbol))
#     # print(f"Name: {variable_symbol.name}")
#     # print(f"Type: {variable_symbol.type}")
#     # print(f"Value: {variable_symbol.value}")
#     # print(f"Is Locked: {variable_symbol.is_locked}")
#     # print(ast)
#     # print("*" * 50)

#     # # Code Generation
#     # print("*" * 50)
#     # print("Generating Python code:")
#     python_code = generate_code(ast)
#     print(python_code)
#     # print("*" * 50)


# if __name__ == "__main__":
#     main()
