# Function to generate Python code from the AST
# It takes a variable indent_level to keep track of the indentation level
def generate_code(ast, indent_level=0):
    generated_code = ""
    for node in ast:
        if node[0] == "declaration":
            generated_code += generate_declaration(node, indent_level)
        elif node[0] == "assignment":
            generated_code += generate_assignment(node, indent_level)
        elif node[0] == "abstract_function_declaration":
            generated_code += handle_abstract_function_declaration(node, indent_level)
        elif node[0] == "print_statement":
            generated_code += generate_print_statement(node, indent_level)
        elif node[0] == "attempt_findout_block":
            generated_code += handle_attempt_findout_block(node, indent_level)
        elif node[0] == "abstract_call":
            generated_code += handle_abstract_call(node, indent_level)
        elif node[0] == "conditionals":
            generated_code += handle_conditionals(node, indent_level)
        else:
            raise ValueError(f"Unknown node type: {node[0]}")

    return generated_code


# Dictionary to store the results of the variables in the code
# It adds a new level for each indentation level then stores the variable name and its value
results = {}


# Generates a declaration statement
def generate_declaration(node, indent_level):
    indent = "    " * indent_level
    if len(node) == 4:
        var_type, var_name = node[2], node[3]
        return f"{indent}{var_name} = None\n"
    elif len(node) == 5:
        var_type, var_name, value = node[2], node[3], node[4]
        if var_type == "string":
            return f"{indent}{var_name} = '{value}'\n"
        if isinstance(value, tuple):
            # value = handle_expression(value,  indent_level)
            value = conditional_switcher(value)
            # Clear all indentation levels except 0 (global scope)
            for level in list(results.keys()):
                if level != 0 and level != indent_level:
                    results.pop(level)
            if indent_level not in results:
                results[indent_level] = {}
            results[indent_level][var_name] = value
            # print(results)
            return f"{indent}{var_name} = {value}\n"
        elif (
            isinstance(value, str)
            | isinstance(value, int)
            | isinstance(value, float)
            | isinstance(value, bool)
        ):
            # Clear all indentation levels except 0 (global scope)
            for level in list(results.keys()):
                if level != 0 and level != indent_level:
                    results.pop(level)
            if indent_level not in results:
                results[indent_level] = {}
            results[indent_level][var_name] = value
            return f"{indent}{var_name} = {value}\n"
        return f"{indent}{var_name} = {value}\n"
    else:
        raise ValueError("Invalid declaration")


# Generates an assignment statement
def generate_assignment(node, indent_level):
    # if indent_level > 0:
    #     # print(node)
    indent = "    " * indent_level
    var_name, value = node[1], node[3]
    if isinstance(value, tuple):
        values = conditional_switcher(value)
        return f"{indent}{var_name} = {values}\n"
    elif (
        isinstance(value, str)
        | isinstance(value, int)
        | isinstance(value, float)
        | isinstance(value, bool)
    ):
        # Clear all indentation levels except 0 (global scope)
        # This is done so that you can access a variable of the same name inside another scope
        for level in list(results.keys()):
            if level != 0 and level != indent_level:
                results.pop(level)
        if indent_level not in results:
            results[indent_level] = {}
        results[indent_level][var_name] = value
        return f"{indent}{var_name} = {value}\n"
    return f"{indent}{var_name} = {value}\n"


# Generates a print statement
def generate_print_statement(node, indent_level):
    indent = "    " * indent_level
    if len(node) == 2:
        # print(node[1][0])
        if node[1][0] == "_":
            return f"{indent}print({node[1]})\n"
        elif node[1][0] != "_":
            return f"{indent}print('{node[1]}')\n"
        # if node[1] in computed_symbols:
        #     return f"print({computed_symbols[node[1]].value})\n"
        else:
            raise ValueError("Invalid print statement")
    elif len(node) == 3:
        if node[1][0] == "_" and node[2][0] == "_":
            return f"{indent}print({node[1]}, {node[2]})\n"
        elif node[1][0] != "_" and node[2][0] != "_":
            return f"{indent}print('{node[1]}','{node[2]}')\n"
        elif node[1][0] != "_" and node[2][0] == "_":
            return f"{indent}print('{node[1]}', {node[2]})\n"
        elif node[1][0] == "_" and node[2][0] != "_":
            return f"{indent}print({node[1]}, '{node[2]}')\n"
        else:
            raise ValueError("Invalid print statement")
    else:
        raise ValueError("Invalid print statement")


# Generates an try-except block
def handle_attempt_findout_block(node, indent_level):
    indent = "    " * indent_level
    attempt_block, findout_block = node[1], node[2]
    generated_code = f"{indent}try:\n"
    generated_code += handle_attempt_block(attempt_block, indent_level + 1)
    exception_var = get_python_error_token(findout_block[1])
    generated_code += f"{indent}except {exception_var} as e:\n"
    generated_code += handle_findout_block(findout_block, indent_level + 1)
    return generated_code


# Generates the code for the try block
def handle_attempt_block(node, indent_level):
    indent = "    " * indent_level
    attempt_block = node[1]
    generated_code = ""
    for statement in attempt_block:
        generated_code += generate_code([statement], indent_level) + "\n"
    return f"{generated_code}"


# Generates the code for the except block
def handle_findout_block(node, indent_level):
    indent = "    " * indent_level
    findout_block = node[2]
    generated_code = ""
    for statement in findout_block:
        generated_code += generate_code([statement], indent_level) + "\n"
    return f"{indent}{generated_code}"


# Generates the function declaration
def handle_abstract_function_declaration(node, indent_level):
    indent = "    " * indent_level
    function_name = node[1]
    parameters = node[2]
    function_body = node[3]
    generated_code = f"def {function_name}("
    if parameters[0] == None:
        generated_code += "):\n"
        for statement in function_body:
            generated_code += generate_code([statement], indent_level + 1)
        return f"{indent}{generated_code}"
    else:
        for param in parameters:
            # print(param[2])
            generated_code += f"{param[2]}, "
        generated_code = generated_code[:-2]  # Remove the last comma and space
        generated_code += "):\n"
        for statement in function_body:
            generated_code += generate_code([statement], indent_level + 1)
        # return ""
        # print(generated_code)
        return f"{indent}{generated_code}"


# Generates the code for the abstract function call
def handle_abstract_call(node, indent_level):
    indent = "    " * indent_level
    function_name = node[1]
    arguments = node[2]
    generated_code = f"{function_name}("
    if arguments[0] != None:
        for arg in arguments:
            if arg[0] == "argument_declaration":
                value = conditional_switcher(arg[1])
                generated_code += f"{value}, "
                generated_code = generated_code[:-1]

            else:
                generated_code += f"{arg}, "
                generated_code = generated_code[:-2]
    generated_code += ")\n"
    return f"{indent}{generated_code}"


# Generates the code for the conditional statements
def handle_conditionals(node, indent_level):
    if node[1][0] == "if":
        return helper_handle_if([node[1]], indent_level)
    elif node[1][0] == "if_elif":
        return handle_if_elif(node[1], indent_level)
    elif node[1][0] == "if_else":
        return handle_if_else(node[1], indent_level)
    elif node[1][0] == "if_elif_else":
        return handle_if_elif_else(node[1], indent_level)
    elif node[1][0] == "aslongas_statement":
        return handle_aslongas(node[1], indent_level)
    elif node[1][0] == "for_loop":
        return handle_for_loop(node[1], indent_level)
    else:
        raise ValueError("Invalid conditional")


# Generates the code for the while loop
def helper_handle_if(node, indent_level):
    indent = "    " * indent_level
    if node[0][0] == "if":
        value = conditional_switcher(node[0][1])
        generated_code = f"{indent}if {value}:\n"
        for statement in node[0][2]:
            generated_code += generate_code([statement], indent_level + 1)
        return generated_code
    else:
        raise ValueError("Invalid conditional block")


# Generates the code for the elif block
def handle_if_elif(node, indent_level):
    indent = "    " * indent_level
    ifstatement = node[1]
    generated_code = ""
    generated_code += helper_handle_if([ifstatement], indent_level)
    generated_code += helper_handle_elif(node[2], indent_level)
    return generated_code


# Generates the code for the elif block
def helper_handle_elif(node, indent_level):
    indent = "    " * indent_level
    value = conditional_switcher(node[1])
    generated_code = f"{indent}elif {value}:\n"
    for statement in node[2]:
        generated_code += generate_code([statement], indent_level + 1)
    return generated_code


# Generates the code for the else block
def handle_if_else(node, indent_level):
    ifstatement = node[1]
    generated_code = ""
    generated_code += helper_handle_if([ifstatement], indent_level)
    generated_code += helper_handle_else(node[2], indent_level)
    return generated_code


# Helper to generate the code for the else block
def helper_handle_else(node, indent_level):
    indent = "    " * indent_level

    generated_code = f"{indent}else:\n"
    for statement in node[1]:
        generated_code += generate_code([statement], indent_level + 1)
    return generated_code


# Generates the code for the if-elif-else block
def handle_if_elif_else(node, indent_level):
    indent = "    " * indent_level
    ifstatement = node[1]
    generated_code = ""
    generated_code += helper_handle_if([ifstatement], indent_level)
    generated_code += helper_handle_elif(node[2], indent_level)
    generated_code += helper_handle_else(node[3], indent_level)
    return generated_code


# Switcher for the conditional statements
# It evaluates expressions and returns the result to be compiled
def conditional_switcher(node):
    generated_code = ""
    if (
        isinstance(node, int)
        or isinstance(node, float)
        or isinstance(node, bool)
        or isinstance(node, str)
    ):
        return str(node)
    if node[0] == "not_equal":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} != {right_operand}"
    elif node[0] == "less_than":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} < {right_operand}"
    elif node[0] == "greater_than":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} > {right_operand}"
        # generated_code += f"{node[1]} > {node[2]}"
    elif node[0] == "less_than_or_equal":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} <= {right_operand}"
        # generated_code += f"{node[1]} <= {node[2]}"
    elif node[0] == "greater_than_or_equal":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        # generated_code += f"{node[1]} >= {node[2]}"
        generated_code += f"{left_operand} >= {right_operand}"
    elif node[0] == "equivalent":
        # generated_code += f"{node[1]} == {node[2]}"
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} == {right_operand}"
    elif node[0] == "bitwise_and":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} & {right_operand}"
    elif node[0] == "bitwise_or":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} | {right_operand}"
    elif node[0] == "bitwise_xor":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} ^ {right_operand}"
    elif node[0] == "shift_left":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} << {right_operand}"
    elif node[0] == "shift_right":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} >> {right_operand}"
    elif node[0] == "not":
        operand = conditional_switcher(node[1])
        generated_code += f"not {operand}"
    elif node[0] == "add":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        return f"{left_operand} + {right_operand}"
    elif node[0] == "sub":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        return f"{left_operand} -  {right_operand}"
    elif node[0] == "mul":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        return f"{left_operand} * {right_operand}"
    elif node[0] == "div":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        return f"{left_operand} / {right_operand}"
    elif node[0] == "power":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        return f"{left_operand} ** {right_operand}"
    return generated_code


# Generates the code for the while loop
def handle_aslongas(node, indent_level):
    indent = "    " * indent_level
    length = len(node[1])
    aslongas = node[2]
    generated_code = ""
    if isinstance(node[1], tuple):
        value = conditional_switcher(node[1])
        generated_code += f"while {value}:\n"
        for statement in aslongas:
            generated_code += generate_code([statement], indent_level + 1)
        return generated_code
    generated_code += f"while {node[1]}:\n"
    for statement in aslongas:
        generated_code += generate_code([statement], indent_level + 1)
    return generated_code


# Generates the code for the for loop
def handle_for_loop(node, indent_level):
    indent = "    " * indent_level
    for_loop_type = node[1]
    id = node[2]
    generated_code = ""
    if for_loop_type == "range":
        generated_code += f"for {id} in range("
        for i in range(len(node[3])):
            generated_code += f"{node[3][i][1]}, "
        generated_code = generated_code[:-2]  # Remove the last comma and space
        generated_code += "):\n"
        for statement in node[4]:
            generated_code += generate_code([statement], indent_level + 1)
        return generated_code
    elif for_loop_type == "in":
        generated_code += f"for {id} in '{node[3]}':\n"
        for statement in node[4]:
            generated_code += generate_code([statement], indent_level + 1)
        return generated_code

    return generated_code


# Dictionary that maps the error token to the corresponding Python error token
def get_python_error_token(reserved_word):
    tokens = {
        "exception": "Exception",
        "stoptteration": "StopIteration",
        "arithmeticerror": "ArithmeticError",
        "floatingpointerror": "FloatingPointError",
        "overflowerror": "OverflowError",
        "zerodivisionerror": "ZeroDivisionError",
        "assertionerror": "AssertionError",
        "attributeerror": "AttributeError",
        "buffererror": "BufferError",
        "eoferror": "EOFError",
        "importerror": "ImportError",
        "modulenotfounderror": "ModuleNotFoundError",
        "lookuperror": "LookupError",
        "indexerror": "IndexError",
        "keyerror": "KeyError",
        "memoryerror": "MemoryError",
        "nameerror": "NameError",
        "unboundlocalerror": "UnboundLocalError",
        "oserror": "OSError",
        "blockingioerror": "BlockingIOError",
        "childprocesserror": "ChildProcessError",
        "connectionerror": "ConnectionError",
        "brokenpipeerror": "BrokenPipeError",
        "connectionabortederror": "ConnectionAbortedError",
        "connectionrefusederror": "ConnectionRefusedError",
        "connectionreseterror": "ConnectionResetError",
        "fileexistserror": "FileExistsError",
        "filenotfounderror": "FileNotFoundError",
        "interruptederror": "InterruptedError",
        "isadirectoryerror": "IsADirectoryError",
        "notadirectoryerror": "NotADirectoryError",
        "permissionerror": "PermissionError",
        "processlookuperror": "ProcessLookupError",
        "timeouterror": "TimeoutError",
        "referenceerror": "ReferenceError",
        "runtimeerror": "RuntimeError",
        "syntaxerror": "SyntaxError",
        "indentationerror": "IndentationError",
        "taberror": "TabError",
        "systemerror": "SystemError",
        "typeerror": "TypeError",
        "valueerror": "ValueError",
        "unicodeerror": "UnicodeError",
        "unicodeencodeerror": "UnicodeEncodeError",
        "unicodedecodeerror": "UnicodeDecodeError",
        "unicodetranslateerror": "UnicodeTranslateError",
        "warning": "Warning",
        "userwarning": "UserWarning",
        "deprecationwarning": "DeprecationWarning",
        "pendingdeprecationwarning": "PendingDeprecationWarning",
        "syntaxwarning": "SyntaxWarning",
        "runtimewarning": "RuntimeWarning",
        "futurewarning": "FutureWarning",
        "importwarning": "ImportWarning",
        "unicodewarning": "UnicodeWarning",
        "byteswarning": "BytesWarning",
        "resourcewarning": "ResourceWarning",
        "keyboardinterrupt": "KeyboardInterrupt",
    }

    return tokens.get(reserved_word.lower(), None)
