def generate_code(ast, computed_symbols, indent_level=0):
    generated_code = ""
    for node in ast:
        print(node[0])
        if node[0] == "declaration":
            generated_code += generate_declaration(node, computed_symbols, indent_level)
        elif node[0] == "assignment":
            generated_code += generate_assignment(node, computed_symbols, indent_level)
        elif node[0] == "abstract_function_declaration":
            generated_code += handle_abstract_function_declaration(
                node, computed_symbols, indent_level
            )
        elif node[0] == "print_statement":
            generated_code += generate_print_statement(
                node, computed_symbols, indent_level
            )
        elif node[0] == "attempt_findout_block":
            generated_code += handle_attempt_findout_block(
                node, computed_symbols, indent_level
            )
        elif node[0] == "abstract_call":
            generated_code += handle_abstract_call(node, computed_symbols, indent_level)
        elif node[0] == "conditionals":
            generated_code += handle_conditionals(node, computed_symbols, indent_level)
        else:
            raise ValueError(f"Unknown node type: {node[0]}")

    return generated_code


results = {}
inside_results = {}
# add


# def handle_expression(node, computed_symbols, indent_level):
#     if isinstance(node, int) or isinstance(node, float) or isinstance(node, bool):
#         # table[node] = node
#         # print(table)
#         return node
#     elif isinstance(node, tuple):
#         if node[0] == "add":
#             left_operand = handle_expression(node[1], computed_symbols, indent_level)
#             right_operand = handle_expression(node[2], computed_symbols, indent_level)
#             result = left_operand + right_operand
#             print(left_operand, right_operand, result)
#             return result
#         elif node[0] == "sub":
#             left_operand = handle_expression(node[1], computed_symbols, indent_level)
#             right_operand = handle_expression(node[2], computed_symbols, indent_level)
#             result = left_operand - right_operand
#             print(left_operand, right_operand, result)
#             return result
#         elif node[0] == "mul":
#             left_operand = handle_expression(node[1], computed_symbols, indent_level)
#             right_operand = handle_expression(node[2], computed_symbols, indent_level)
#             result = left_operand * right_operand
#             print(left_operand, right_operand, result)
#             return result
#         elif node[0] == "div":
#             left_operand = handle_expression(node[1], computed_symbols, indent_level)
#             right_operand = handle_expression(node[2], computed_symbols, indent_level)
#             result = left_operand / right_operand
#             print(left_operand, right_operand, result)
#             return result
#         elif node[0] == "power":
#             left_operand = handle_expression(node[1], computed_symbols, indent_level)
#             right_operand = handle_expression(node[2], computed_symbols, indent_level)
#             result = left_operand**right_operand
#             print(left_operand, right_operand, result)
#             return result
#         elif node[0] == "not":
#             operand = handle_expression(node[1], indent_level)
#             if not isinstance(operand, bool):
#                 raise ValueError(f"Expected a boolean, got '{type(operand).__name__}'")
#             result = not operand
#             print(operand, result)
#             return result
#         elif node[0] == "equivalent":
#             left_operand = handle_expression(node[1], computed_symbols, indent_level)
#             right_operand = handle_expression(node[2], computed_symbols, indent_level)
#             result = left_operand == right_operand
#             print(left_operand, right_operand, result)
#             return result
#         elif node[0] == "greater_than":
#             left_operand = handle_expression(node[1], computed_symbols, indent_level)
#             right_operand = handle_expression(node[2], computed_symbols, indent_level)
#             result = left_operand > right_operand
#             print(left_operand, right_operand, result)
#             return result
#         elif node[0] == "less_than":
#             left_operand = handle_expression(node[1], computed_symbols, indent_level)
#             right_operand = handle_expression(node[2], computed_symbols, indent_level)
#             result = left_operand < right_operand
#             print(left_operand, right_operand, result)
#             return result
#         elif node[0] == "not_equal":
#             left_operand = handle_expression(node[1], computed_symbols, indent_level)
#             right_operand = handle_expression(node[2], computed_symbols, indent_level)
#             result = left_operand != right_operand
#             print(left_operand, right_operand, result)
#             return result
#         elif node[0] == "less_than_or_equal":
#             left_operand = handle_expression(node[1], computed_symbols, indent_level)
#             right_operand = handle_expression(node[2], computed_symbols, indent_level)
#             result = left_operand <= right_operand
#             print(left_operand, right_operand, result)
#             return result
#         elif node[0] == "greater_than_or_equal":
#             left_operand = handle_expression(node[1], computed_symbols, indent_level)
#             right_operand = handle_expression(node[2], computed_symbols, indent_level)
#             result = left_operand >= right_operand
#             print(left_operand, right_operand, result)
#             return result
#     elif isinstance(node, str):
#         if 0 in results and node in results[0]:
#             value = results[0][node]
#             return value
#         # Check if the variable is in the current scope
#         elif indent_level in results and node in results[indent_level]:
#             value = results[indent_level][node]
#             return value
#         else:
#             return computed_symbols[node].value
#             # raise ValueError(f"Undeclared variable '{node}'")
#     elif node is None:
#         return node
#     else:
#         raise ValueError(f"Invalid expression {node}")


def generate_declaration(node, computed_symbols, indent_level):
    print(node)
    indent = "    " * indent_level  # Calculate indentation
    if len(node) == 4:
        var_type, var_name = node[2], node[3]
        return f"{indent}{var_name} = None\n"
    elif len(node) == 5:
        var_type, var_name, value = node[2], node[3], node[4]
        if var_type == "string":
            return f"{indent}{var_name} = '{value}'\n"
        if isinstance(value, tuple):
            # value = handle_expression(value, computed_symbols, indent_level)
            value = conditional_switcher(value)
            # Clear all indentation levels except 0 (global scope)
            for level in list(results.keys()):
                if level != 0 and level != indent_level:
                    results.pop(level)
            if indent_level not in results:
                results[indent_level] = {}
            results[indent_level][var_name] = value
            print(results)
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


def generate_assignment(node, computed_symbols, indent_level):
    if indent_level > 0:
        print(node)
    indent = "    " * indent_level  # Calculate indentation
    var_name, value = node[1], node[3]
    if isinstance(value, tuple):
        values = conditional_switcher(value)
        # value = handle_expression(value, computed_symbols, indent_level)
        # # Clear all indentation levels except 0 (global scope)
        # for level in list(results.keys()):
        #     if level != 0 and level != indent_level:
        #         results.pop(level)
        # if indent_level not in results:
        #     results[indent_level] = {}
        # results[indent_level][var_name] = value
        # print(results)
        # return f"{indent}{var_name} = {value}\n"
        return f"{indent}{var_name} = {values}\n"
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
    # return f"{indent}{var_name} = {value}\n"


def generate_print_statement(node, computed_symbols, indent_level):
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


def handle_attempt_findout_block(node, computed_symbols, indent_level):
    indent = "    " * indent_level  # Calculate indentation
    attempt_block, findout_block = node[1], node[2]
    generated_code = f"{indent}try:\n"
    generated_code += handle_attempt_block(
        attempt_block, computed_symbols, indent_level + 1
    )
    exception_var = get_python_error_token(findout_block[1])
    generated_code += f"{indent}except {exception_var} as e:\n"
    generated_code += handle_findout_block(
        findout_block, computed_symbols, indent_level + 1
    )
    return generated_code


def handle_attempt_block(node, computed_symbols, indent_level):
    indent = "    " * indent_level  # Calculate indentation
    attempt_block = node[1]
    generated_code = ""
    for statement in attempt_block:
        generated_code += (
            generate_code([statement], computed_symbols, indent_level) + "\n"
        )
    return f"{generated_code}"


def handle_findout_block(node, computed_symbols, indent_level):
    indent = "    " * indent_level  # Calculate indentation
    findout_block = node[2]
    generated_code = ""
    for statement in findout_block:
        generated_code += (
            generate_code([statement], computed_symbols, indent_level) + "\n"
        )
    return f"{generated_code}"


def handle_abstract_function_declaration(node, computed_symbols, indent_level):
    # print(node)
    # print("HERRRRRRRRRRRERRRRRRRRRRRRRRRRRRRRR")
    indent = "    " * indent_level
    function = computed_symbols[node[1]]
    function_name = function.name
    # name, params, return_type, statements
    # print(function_name)
    print(function.params[0])
    # print(function.return_type)
    print(function.statements)
    parameters = function.params
    # print(parameters[0])
    function_body = function.statements
    generated_code = f"def {function_name}("
    if parameters[0] == None:
        generated_code += "):\n"
        # generated_code = generated_code[:-2]  # Remove the last comma and space
        # generated_code += "):\n"
        for statement in function_body:
            generated_code += generate_code(
                [statement], computed_symbols, indent_level + 1
            )
        return f"{indent}{generated_code}"
    else:
        for param in parameters:
            print(param[2])
            generated_code += f"{param[2]}, "
        generated_code = generated_code[:-2]  # Remove the last comma and space
        generated_code += "):\n"
        for statement in function_body:
            generated_code += generate_code(
                [statement], computed_symbols, indent_level + 1
            )
        # return ""
        # print(generated_code)
        return f"{indent}{generated_code}"


def handle_abstract_call(node, computed_symbols, indent_level):
    print(node)
    indent = "    " * indent_level
    function_name = node[1]
    arguments = node[2]
    generated_code = f"{function_name}("
    if arguments[0] != None:
        print(arguments)
        for arg in arguments:
            if arg[0] == "argument_declaration":
                # computed_symbols[arg[1]].value
                value = conditional_switcher(arg[1])
                generated_code += f"{value}, "
                generated_code = generated_code[:-1]

            else:
                generated_code += f"{arg}, "
                generated_code = generated_code[:-2]
                print("hit")
    # generated_code = generated_code[:-1]  # Remove the last comma and space
    generated_code += ")\n"
    print(generated_code)
    return f"{indent}{generated_code}"


def handle_conditionals(node, computed_symbols, indent_level):
    print("Handling conditionals\n\n")
    print(node[1][0])
    if node[1][0] == "if":
        return helper_handle_if([node[1]], computed_symbols, indent_level)
    elif node[1][0] == "if_elif":
        return handle_if_elif(node[1], computed_symbols, indent_level)
    elif node[1][0] == "if_else":
        return handle_if_else(node[1], computed_symbols, indent_level)
    elif node[1][0] == "if_elif_else":
        return handle_if_elif_else(node[1], computed_symbols, indent_level)
    elif node[1][0] == "aslongas_statement":
        return handle_aslongas(node[1], computed_symbols, indent_level)
    elif node[1][0] == "for_loop":
        return handle_for_loop(node[1], computed_symbols, indent_level)
    else:
        raise ValueError("Invalid conditional")


def helper_handle_if(node, computed_symbols, indent_level):
    indent = "    " * indent_level
    print(node[0])
    print("Handling if\n\n")
    if node[0][0] == "if":
        # print(len(node[0][1]))
        # if len(node[0][1]) == 3:
        #     x = node[0][1][1]
        #     y = node[0][1][2]
        #     print(x, y)
        # value = handle_expression(node[0][1], computed_symbols, indent_level)
        value = conditional_switcher(node[0][1])
        generated_code = f"if {value}:\n"  # TODO Fix the expressions
        # elif len(node[0][1]) == 1:
        #     generate_code = f"if {node[0][1]}:\n"
        for statement in node[0][2]:
            print([statement])
            generated_code += generate_code(
                [statement], computed_symbols, indent_level + 1
            )
        return generated_code
    else:
        raise ValueError("Invalid conditional block")


def handle_if_elif(node, computed_symbols, indent_level):
    indent = "    " * indent_level
    ifstatement = node[1]
    generated_code = ""
    generated_code += helper_handle_if([ifstatement], computed_symbols, indent_level)
    generated_code += helper_handle_elif(node[2], computed_symbols, indent_level)
    return generated_code


def helper_handle_elif(node, computed_symbols, indent_level):
    indent = "    " * indent_level
    print("Handling elif\n\n")
    print(node[1])
    # value = handle_expression(node[1], computed_symbols, indent_level)
    value = conditional_switcher(node[1])
    generated_code = f"elif {value}:\n"
    for statement in node[2]:
        print([statement])
        generated_code += generate_code([statement], computed_symbols, indent_level + 1)
    print(generated_code)
    return generated_code


def handle_if_else(node, computed_symbols, indent_level):
    ifstatement = node[1]
    generated_code = ""
    generated_code += helper_handle_if([ifstatement], computed_symbols, indent_level)
    generated_code += helper_handle_else(node[2], computed_symbols, indent_level)
    return generated_code


def helper_handle_else(node, computed_symbols, indent_level):
    indent = "    " * indent_level
    print("Handling else\n\n")
    print(node[0])

    generated_code = "else:\n"
    for statement in node[1]:
        print([statement])
        generated_code += generate_code([statement], computed_symbols, indent_level + 1)
    print(generated_code)
    return generated_code
    # else:
    #     raise ValueError("Invalid conditional block")


def handle_if_elif_else(node, computed_symbols, indent_level):
    indent = "    " * indent_level
    ifstatement = node[1]
    generated_code = ""
    generated_code += helper_handle_if([ifstatement], computed_symbols, indent_level)
    generated_code += helper_handle_elif(node[2], computed_symbols, indent_level)
    generated_code += helper_handle_else(node[3], computed_symbols, indent_level)
    return generated_code


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
        # generated_code += f"{node[1]} != {node[2]}"
    elif node[0] == "less_than":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} < {right_operand}"
        # generated_code += f"{node[1]} < {node[2]}"
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
        # generated_code += f"{node[1]} & {node[2]}"
        generated_code += f"{left_operand} & {right_operand}"
    elif node[0] == "bitwise_or":
        # generated_code += f"{node[1]} | {node[2]}"
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} | {right_operand}"
    elif node[0] == "bitwise_xor":
        # generated_code += f"{node[1]} ^ {node[2]}"
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} ^ {right_operand}"
    elif node[0] == "shift_left":
        # generated_code += f"{node[1]} << {node[2]}"
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        generated_code += f"{left_operand} << {right_operand}"
    elif node[0] == "shift_right":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        # generated_code += f"{node[1]} >> {node[2]}"
        generated_code += f"{left_operand} >> {right_operand}"
    elif node[0] == "not":
        operand = conditional_switcher(node[1])
        generated_code += f"not {operand}"
    elif node[0] == "add":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        return f"{left_operand} + {right_operand}"
        # generated_code += f"{node[1]} + {node[2]}"
    elif node[0] == "sub":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        return f"{left_operand} -  {right_operand}"
        # generated_code += f"{node[1]} - {node[2]}"
    elif node[0] == "mul":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        return f"{left_operand} * {right_operand}"
        # generated_code += f"{node[1]} * {node[2]}"
    elif node[0] == "div":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        return f"{left_operand} / {right_operand}"
        # generated_code += f"{node[1]} / {node[2]}"
    elif node[0] == "power":
        left_operand = conditional_switcher(node[1])
        right_operand = conditional_switcher(node[2])
        return f"{left_operand} ** {right_operand}"
        # generated_code += f"{node[1]} ** {node[2]}"
    return generated_code
    # elif p[2] == "<":
    #     p[0] = ("less_than", p[1], p[3])
    # elif p[2] == ">":
    #     p[0] = ("greater_than", p[1], p[3])
    # elif p[2] == "<=":
    #     p[0] = ("less_than_or_equal", p[1], p[3])
    # elif p[2] == ">=":
    #     p[0] = ("greater_than_or_equal", p[1], p[3])
    # elif p[2] == "==":
    #     p[0] = ("equivalent", p[1], p[3])
    # elif p[2] == "&":
    #     p[0] = ("bitwise_and", p[1], p[3])
    # elif p[2] == "|":
    #     p[0] = ("bitwise_or", p[1], p[3])
    # elif p[2] == "^":
    #     p[0] = ("bitwise_xor", p[1], p[3])
    # elif p[2] == "<<":
    #     p[0] = ("shift_left", p[1], p[3])
    # elif p[2] == ">>":
    #     p[0] = ("shift_right", p[1], p[3])


def handle_aslongas(node, computed_symbols, indent_level):
    indent = "    " * indent_level
    print(node[1])
    length = len(node[1])
    print(length)
    print(type(node[1]))
    aslongas = node[2]
    print(aslongas)
    generated_code = ""
    if isinstance(node[1], tuple):
        value = conditional_switcher(node[1])
        # value = conditional_switcher(node[1])
        generated_code += f"while {value}:\n"
        for statement in aslongas:
            generated_code += generate_code(
                [statement], computed_symbols, indent_level + 1
            )
        return generated_code
    generated_code += f"while {node[1]}:\n"
    for statement in aslongas:
        generated_code += generate_code([statement], computed_symbols, indent_level + 1)
    # for block in aslongas:
    #     if block[0] == "aslongas":
    #         generated_code += f"while {block[1]}:\n"
    #         for statement in block[2]:
    #             generated_code += generate_code(
    #                 statement, computed_symbols, indent_level + 1
    #             )
    #     else:
    #         raise ValueError("Invalid conditional block")
    return generated_code


def handle_for_loop(node, computed_symbols, indent_level):
    indent = "    " * indent_level
    print(node)
    for_loop_type = node[1]
    id = node[2]
    generated_code = ""
    if for_loop_type == "range":
        generated_code += f"for {id} in range("
        for i in range(len(node[3])):
            print(node[3][i][1])
            generated_code += f"{node[3][i][1]}, "
        generated_code = generated_code[:-2]  # Remove the last comma and space
        generated_code += "):\n"
        for statement in node[4]:
            generated_code += generate_code(
                [statement], computed_symbols, indent_level + 1
            )
        return generated_code
    elif for_loop_type == "in":
        generated_code += f"for {id} in '{node[3]}':\n"
        for statement in node[4]:
            generated_code += generate_code(
                [statement], computed_symbols, indent_level + 1
            )
        return generated_code
    print(for_loop_type)

    # generated_code += f"for {block[1]} in {block[2]}:\n"
    # for statement in block[3]:
    #     generated_code += generate_code(statement, computed_symbols, indent_level + 1)

    return generated_code


# def handle_conditionals(node, computed_symbols, indent_level):
#     print(node)
#     indent = "    " * indent_level
#     if_elif_else = node[1]
#     generated_code = ""
#     for block in if_elif_else:
#         if block[0] == "if":
#             generated_code += f"if {block[1]}:\n"
#             for statement in block[2]:
#                 generated_code += generate_code(
#                     statement, computed_symbols, indent_level + 1
#                 )
#         elif block[0] == "elif":
#             generated_code += f"elif {block[1]}:\n"
#             for statement in block[2]:
#                 generated_code += generate_code(
#                     statement, computed_symbols, indent_level + 1
#                 )
#         elif block[0] == "else":
#             generated_code += "else:\n"
#             for statement in block[1]:
#                 generated_code += generate_code(
#                     statement, computed_symbols, indent_level + 1
#                 )
#         else:
#             raise ValueError("Invalid conditional block")
#     print(generated_code)
#     return generated_code


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


# Example usage
# generated_python_code = generate_code(ast)
# print("Generated Python code:")
# print(generated_python_code)
