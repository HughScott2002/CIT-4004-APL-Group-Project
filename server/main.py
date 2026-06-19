from flask import Flask, request, jsonify
from typesnake.symbol_table import *
from typesnake.parser_1 import parser
from typesnake.semantic_analyzer import semantic_analyzer
from typesnake.code_generator import generate_code
from flask_cors import CORS

# TODO: Add arithmetic operations to the language (Done)
# TODO: Make sure you can assign a variable to another variable (Done)
# TODO: Add conditionals to the language (DONE)
# TODO: Add scope and binding to the language (Done)
# TODO: Add params and args to the language (Done)
# TODO: Finish the code generator (Done)
# TODO: Finish the server backend (Done)


app = Flask(__name__)
allowed_origins = [
    "https://apl-cit-4004-web-ui.vercel.app",
    "https://apl-web-ui.vercel.app",
]
CORS(app, origins=allowed_origins)


@app.route("/generate_code", methods=["POST"])
def parse_code():
    global_symbol_table = SymbolTable()
    input_code = request.json.get("code")
    print(input_code)
    # Parse the input code
    try:
        ast = parser.parse(input_code)
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
    compiled_python_code = generate_code(ast)

    # Return the transpiled Python code — caller runs it, not us
    response = {"python_code": compiled_python_code}
    return jsonify(response)


@app.route("/test", methods=["GET"])
def test():
    return jsonify({"message": "Hello, World!"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
