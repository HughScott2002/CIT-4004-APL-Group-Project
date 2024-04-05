# import parser_1 as parser
# from shortsourcecode import data as shortdata

# Symobol Table
# from SymbolTable import *
from symbol_table import *


def semantic_analyzer(ast, current_scope):
    for x in ast:
        if x[0] == "declaration":
            handle_declaration(x, current_scope)
        elif x[0] == "assignment":
            handle_assignment(x, current_scope)
        elif x[0] == "abstract_function_declaration":
            handle_abstract_function_declaration(x, current_scope)
        elif x[0] == "print_statement":
            handle_print_statement(x, current_scope)
        elif x[0] == "attempt_findout_block":
            handle_attempt_findout_block(x, current_scope)
        elif x[0] == "abstract_call":
            handle_abstract_call(x, current_scope)
        # elif x[0] == "conditionals":
        #     print("*" * 30)
        #     print(symbol_table)
        #     # print(scope_stack)
        #     print("*" * 30)
        #     handle_conditionals(x)
        # elif x[0] == "argument_declaration":
        #     print(x[2])


# Type checking
def type_checking(var_type, value):
    if var_type == "int":
        # print(type(value))
        if type(value) != int:
            return False
        # if not isinstance(value, int):
        # print(f"Expected an integer, got type '{type(value).__name__}'")
        # raise ValueError(f"Expected an integer, got '{type(value).__name__}'")
        # return False
        else:
            return True
    elif var_type == "float":
        if type(value) != float:
            print(f"Expected a float, got '{type(value).__name__}'")
            return False
        # if not isinstance(value, float):
        #     # raise ValueError(f"Expected a float, got '{type(value).__name__}'")
        #     return False
        else:
            return True
    elif var_type == "bool":
        if type(value) != bool:
            print(f"Expected a boolean, got '{type(value).__name__}'")
            return False
        # if not isinstance(value, bool):
        #     print(f"Expected a boolean, got '{type(value).__name__}'")
        #     # raise ValueError(f"Expected a boolean, got '{type(value).__name__}'")
        #     return False
        else:
            return True
    elif var_type == "string":
        if type(value) != str:
            print(f"Expected a string, got '{type(value).__name__}'")
            return False
        # if not isinstance(value, str):
        #     print(f"Expected a string, got '{type(value).__name__}'")
        #     # raise ValueError(f"Expected a string, got '{type(value).__name__}'")
        #     return False
        else:
            return True
    else:
        print(f"Unknown type '{var_type}'")
        # raise ValueError(f"Unknown type '{var_type}'")
        return False


# Handles expressions
def handle_expression(node, current_scope):
    if isinstance(node, int) or isinstance(node, float) or isinstance(node, bool):
        return node
    elif isinstance(node, tuple):
        if node[0] == "add":
            left_operand = handle_expression(node[1], current_scope)
            right_operand = handle_expression(node[2], current_scope)
            result = left_operand + right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "sub":
            left_operand = handle_expression(node[1], current_scope)
            right_operand = handle_expression(node[2], current_scope)
            result = left_operand - right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "mul":
            left_operand = handle_expression(node[1], current_scope)
            right_operand = handle_expression(node[2], current_scope)
            result = left_operand * right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "div":
            left_operand = handle_expression(node[1], current_scope)
            right_operand = handle_expression(node[2], current_scope)
            result = left_operand / right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "power":
            left_operand = handle_expression(node[1], current_scope)
            right_operand = handle_expression(node[2], current_scope)
            result = left_operand**right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "not":
            # Check if the operand is a primitive type
            operand = handle_expression(node[1], current_scope)
            if not isinstance(operand, bool):
                # print(f"Expected a boolean, got '{type(operand).__name__}'")
                raise ValueError(f"Expected a boolean, got '{type(operand).__name__}'")
            result = not operand
            print(operand, result)
            return result
        elif node[0] == "equivalent":
            left_operand = handle_expression(node[1], current_scope)
            right_operand = handle_expression(node[2], current_scope)
            result = left_operand == right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "greater_than":
            left_operand = handle_expression(node[1], current_scope)
            right_operand = handle_expression(node[2], current_scope)
            result = left_operand > right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "less_than":
            left_operand = handle_expression(node[1], current_scope)
            right_operand = handle_expression(node[2], current_scope)
            result = left_operand < right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "not_equal":
            left_operand = handle_expression(node[1], current_scope)
            right_operand = handle_expression(node[2], current_scope)
            result = left_operand != right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "less_than_or_equal":
            left_operand = handle_expression(node[1], current_scope)
            right_operand = handle_expression(node[2], current_scope)
            result = left_operand <= right_operand
            print(left_operand, right_operand, result)
            return result
        elif node[0] == "greater_than_or_equal":
            left_operand = handle_expression(node[1], current_scope)
            right_operand = handle_expression(node[2], current_scope)
            result = left_operand >= right_operand
            print(left_operand, right_operand, result)
            return result
    # Check if the node is a string
    elif isinstance(node, str):
        # Check is the node is a variable
        if node[0] == "_":
            # If the node is a variable, check if it is in the symbol table
            # check = check_symbol_table(node)
            lookup_var = current_scope.lookup(node)
            if not lookup_var:
                # print(f"Undeclared variable '{node}'")
                raise ValueError(f"Undeclared variable '{node}'")
            # var_type, value, is_locked, symbol_type = symbol_table[node]
            value = lookup_var.value
            return value
    elif node == None:
        return node
    else:
        raise ValueError(f"Invalid expression {node}")


# Handles declarations
def handle_declaration(node, current_scope):
    if len(node) == 4:
        print((node))
        var_mut, var_type, var_name = node[1][1], node[2], node[3]
        if var_mut == "lock":
            is_locked = True
        elif var_mut == "unlock":
            is_locked = False
        else:
            raise ValueError("Invalid mutex declaration")
        # is_locked = var_mut == "lock"
        # type_checking(var_type, None)
        print("Got passed the mut check")
        # LOOKUP
        check_if_variable_exists = current_scope.lookup(var_name)
        print(check_if_variable_exists)
        if check_if_variable_exists:
            print(f"Variable '{var_name}' is already declared")
            raise ValueError(f"Variable '{var_name}' is already declared")
        elif check_if_variable_exists is None:
            add_to_symbol_table = current_scope.insert(
                VariableSymbol(var_name, var_type, None, is_locked)
            )
            if add_to_symbol_table == False:
                raise ValueError(f"Variable '{var_name}' is already declared")
        print("Got passed the lookup check")
        # Adds to the symbol table or sends back false

        # check_symbol = add_to_symbol_table(var_name, var_type, None, is_locked)
    elif len(node) == 5:
        var_mut, var_type, var_name, value = node[1][1], node[2], node[3], node[4]
        if var_mut == "lock":
            is_locked = True
        elif var_mut == "unlock":
            is_locked = False
        else:
            raise ValueError("Invalid mutex declaration")

        # LOOKUP
        check_if_variable_exists = current_scope.lookup(var_name)
        # Check if the variable is already declared
        if check_if_variable_exists:  # If the variable is already declared
            if (
                is_locked == True and check_if_variable_exists.value is not None
            ):  # If the variable is locked and has a value
                raise ValueError(f"Cannot reassign locked variable '{var_name}'")
            # raise ValueError(f"Variable '{var_name}' is already declared") #

        # Handles any expressions
        if isinstance(value, tuple):
            value = handle_expression(value, current_scope)
        # Checks if the type is correct
        type_check = type_checking(var_type, value)
        if not type_check:
            raise ValueError(f"Expected an {var_type}, got '{type(value).__name__}'")
            # raise ValueError(f"Cannot assign locked variable '{var_name}'")

        # Checks if the variable is locked
        # if is_locked:
        #     raise ValueError(f"Cannot assign locked variable '{var_name}'")

        # Adds to the symbol table or sends back false
        add_to_symbol_table = current_scope.insert(
            VariableSymbol(var_name, var_type, value, is_locked)
        )
        if add_to_symbol_table == False:
            raise ValueError(f"Variable '{var_name}' is already declared")

        var = current_scope.lookup(var_name)
        if var:
            print(
                f"Declared '{var_mut}' variable '{var.name}' of type '{var.type}' with value '{var.value}'"
            )
        # print("This is node[4]")
        # print(node[4])
        # print("This is value")
        # print(value)
        # node[4] = value
    else:
        raise ValueError("Invalid declaration")


# Handles assignments
def handle_assignment(node, current_scope):
    if len(node) == 4:
        var_name, value = node[1], node[3]
        if isinstance(value, tuple):
            value = handle_expression(value, current_scope)
        # Check if the variable is in the symbol table
        # Check if the variable has a value
        # Check if the variable is locked

        lookup_var = current_scope.lookup(var_name)
        if lookup_var is None:
            # print(f"Undeclared variable '{var_name}'")
            raise ValueError(f"Undeclared variable '{var_name}'")
        else:
            var_type = lookup_var.type
            old_value = lookup_var.value
            is_locked = lookup_var.is_locked
            if is_locked and old_value is not None:
                # print(f"Cannot reassign locked variable '{var_name}'")
                raise ValueError(f"Cannot reassign locked variable '{var_name}'")
            else:

                # Check if the type is correct
                type_check = type_checking(var_type, value)
                # If the type is incorrect, raise an error
                if type_check == False:
                    raise ValueError(
                        f"Expected an {var_type}, got '{type(value).__name__}'"
                    )
                # If the type is correct, assign the value to the variable
                elif type_check:
                    lookup_var.value = value
                    print(f"Assigned value '{value}' to variable '{var_name}'")
                else:
                    # print(
                    #     f"Type mismatch for variable '{var_name}' expected '{var_type}'"
                    # )
                    raise ValueError(
                        f"Type mismatch for variable '{var_name}' expected '{var_type}'"
                    )

    else:
        raise ValueError("Invalid assignment")


# TODO: Fix the print statement so it accepts variables (DONE)
# # Handles print statements
def handle_print_statement(node, current_scope):
    if len(node) == 2:
        # Check is it an identifier or a string
        if isinstance(node[1], str):
            if node[1][0] == "_":
                lookup_var = current_scope.lookup(node[1])
                if not lookup_var:
                    # print(f"Undeclared variable '{node}'")
                    raise ValueError(
                        f"Undeclared variable '{node[1]}' in scribe statement "
                    )
                # var_type, value, is_locked, symbol_type = symbol_table[node]
                # value = lookup_var.value
                # return value
                else:
                    print(lookup_var.value)
            else:
                print(node[1])
        else:
            raise ValueError("Invalid scribe statement")
        # print("2")

        # print(node[1])
    elif len(node) == 3:
        if isinstance(node[1], str):
            if node[1][0] == "_":
                lookup_var_1 = current_scope.lookup(node[1])
                lookup_var_2 = current_scope.lookup(node[2])
                if not lookup_var_1:
                    # print(f"Undeclared variable '{node}'")
                    raise ValueError(
                        f"Undeclared variable '{node[1]}' in scribe statement "
                    )
                if not lookup_var_2:
                    # print(f"Undeclared variable '{node}'")
                    raise ValueError(
                        f"Undeclared variable '{node[2]}' in scribe statement "
                    )
                # var_type, value, is_locked, symbol_type = symbol_table[node]
                # value = lookup_var.value
                # return value
                else:
                    print(lookup_var_1.value, lookup_var_2.value)
            else:
                lookup_var_2 = current_scope.lookup(node[2])
                print(node[1], lookup_var_2.value)
        else:
            raise ValueError("Invalid scribe statement")
        # if isinstance(node[2], str):
        #     if node[2][0] == "_":
        #         lookup_var = current_scope.lookup(node[2])
        #         if not lookup_var:
        #             # print(f"Undeclared variable '{node}'")
        #             raise ValueError(
        #                 f"Undeclared variable '{node[2]}' in scribe statement "
        #             )
        #         # var_type, value, is_locked, symbol_type = symbol_table[node]
        #         # value = lookup_var.value
        #         # return value
        #         else:
        #             print(node[2], lookup_var.value)
        #     else:
        #         raise ValueError(
        #             "If using the second argument in the scribe statement, it must be a variable"
        #         )
        # else:
        #     raise ValueError("Invalid scribe statement")
    else:
        raise ValueError("Invalid scribe statement")
    # print(len(node))
    # print(node)
    # if node[2] != "@":

    #     if check_symbol_table(node[2]):
    #         var_name = node[2]
    #         # TODO remove the print statement
    #         var_type, value, is_locked, symbol_type = symbol_table[var_name]
    #         print(f"{node[1]}, '{value}'")
    #     else:
    #         print(f"Undeclared variable '{node[2]}'")
    #         raise ValueError(f"Undeclared variable '{node[2]}'")
    # else:
    #     print(f"{node[1]}")


# # Handles attempt and findout blocks
def handle_attempt_findout_block(node, current_scope):
    handle_attempt_block(node[1], current_scope)
    handle_findout_block(node[2], current_scope)
    # print(node)


# # Handles attempt block
def handle_attempt_block(node, current_scope):
    # print(node[1])
    semantic_analyzer(node[1], current_scope)


# # Handles findout block
def handle_findout_block(node, current_scope):
    #     # print(node)
    semantic_analyzer(node[2], current_scope)


# TODO: Implement parameter and argument declaration
# Handles abstract function declaration
def handle_abstract_function_declaration(node, current_scope):
    check_if_function_exists = current_scope.lookup(node[1])
    if check_if_function_exists:
        # print(f"Function '{node[1]}' is already declared")
        raise ValueError(f"Function '{node[1]}' is already declared")
    else:
        add_function = current_scope.insert(
            FunctionSymbol(node[1], node[2], "void", node[3])
        )
        if add_function == False:
            raise ValueError(f"Function '{node[1]}' is already declared")
        elif add_function:
            print(f"Declared function '{node[1]}'")
        else:
            raise ValueError(f"Function '{node[1]}' was not declared")
        # add_to_symbol_table(node[1], None, node[3], True, "function")
        # add_to_abstract_function_symbol_table(node[1], node[2], node[3])


# def handle_parameter_declaration(node):
#     pass


# # TODO: Implement parameter and argument declaration
# # Handles abstract function call
def handle_abstract_call(node, current_scope):
    check_if_function_exists = current_scope.lookup(node[1])
    print(node)
    if check_if_function_exists:
        # Declaring a new scope for the function
        function_scope = new_scope(current_scope)
        # Check if the function has parameters
        params = check_if_function_exists.params
        print(params)
        # Check if the function has arguments
        arguments = node[2]
        # if the function has no parameters and no arguments run the function
        if arguments == [None] and params == [None]:
            statements_ast = check_if_function_exists.statements
            semantic_analyzer(statements_ast, function_scope)
        # if the function has parameters but no arguments raise an error
        if arguments == [None] and params != [None]:
            raise ValueError(f"Expected {len(params)} arguments, got 0")
        # Check if the number of arguments match the number of parameters
        if len(params) != len(arguments):
            raise ValueError(f"Expected {len(params)} arguments, got {len(arguments)}")

        for param, argument in zip(params, arguments):
            print(param, argument)
            if isinstance(argument[1], tuple):
                argument_value = handle_expression(argument[1], current_scope)
                print(argument_value)
                if argument_value:
                    lookup_param = current_scope.lookup(param[2])
                    print(lookup_param)
                    print(param)
                    if lookup_param == None:
                        check_if_param_and_arg_are_same_type = type_checking(
                            param[1], argument_value
                        )
                        print(param[1], argument_value)
                        if not check_if_param_and_arg_are_same_type:
                            raise ValueError(
                                f"Invalid argument'{argument_value}' of type '{type(argument_value).__name__}' not the same type as the parameter '{param[1]}'"
                            )
                        print(check_if_param_and_arg_are_same_type)

                        if check_if_param_and_arg_are_same_type:
                            function_scope.insert(
                                VariableSymbol(
                                    param[2], param[1], argument_value, False
                                )
                            )
                            lookup_param = function_scope.lookup(param[2])
                            print(
                                f"Declared '{lookup_param.name}' of type '{lookup_param.type}' with value '{lookup_param.value}'"
                            )
                        # print(f"Declared '{param[2]}' of type '{argument_value[1]}'")
                    else:
                        check_if_param_and_arg_are_same_type = type_checking(
                            lookup_param.type, argument_value
                        )
                        if check_if_param_and_arg_are_same_type:
                            function_scope.insert(
                                VariableSymbol(
                                    param[2], param[1], argument_value, False
                                )
                            )
                        else:
                            raise ValueError(
                                f"Invalid argument'{argument[1]}' not the same type as the parameter '{param[1]}'"
                            )
                else:
                    raise ValueError(
                        f"Invalid argument'{argument[1]}' expression not calculated"
                    )
            elif isinstance(argument[1], str):
                # print(argument[1][0])
                if argument[1][0] == "_":
                    lookup_var = current_scope.lookup(argument[1])
                    if not lookup_var:
                        raise ValueError(
                            f"Undeclared variable '{argument[1]}' in argument"
                        )
                    lookup_param = current_scope.lookup(param[2])
                    if lookup_param.value == lookup_var.value:
                        check_type = type_checking(lookup_param.type, lookup_var.value)
                        if not check_type:
                            raise ValueError(
                                f"Invalid argument'{lookup_var.value}' of type '{type(lookup_var.value).__name__}' not the same type as the parameter '{param[1]}'"
                            )
                        function_scope.insert(
                            VariableSymbol(param[2], param[1], lookup_var.value, False)
                        )
                        print(function_scope.lookup(param[2]).value)
                else:
                    check_type = type_checking(argument[1], param[1])
                    if not check_type:
                        raise ValueError(
                            f"Invalid argument'{lookup_var.value}' of type '{type(lookup_var.value).__name__}' not the same type as the parameter '{param[1]}'"
                        )
                    function_scope.insert(
                        VariableSymbol(param[2], param[1], lookup_var.value, False)
                    )
                    print(function_scope.lookup(param[2]).value)
                    # print(lookup_param.type, lookup_var.value)
                    # raise ValueError("stop here")
                    # check_if_param_and_arg_are_same_type = type_checking(
                    #     param[1], argument_value
                    # )
                    # print(param[1], argument_value)
                    # if not check_if_param_and_arg_are_same_type:
                    #     raise ValueError(
                    #         f"Invalid argument'{argument_value}' of type '{type(argument_value).__name__}' not the same type as the parameter '{param[1]}'"
                    #     )
                    # print(check_if_param_and_arg_are_same_type)
                    # function_scope.insert(
                    #     VariableSymbol(param[2], param[1], lookup_var.value, False)
                    # )
            elif (
                isinstance(argument[1], int)
                or isinstance(argument[1], float)
                or isinstance(argument[1], bool)
            ):
                check_if_param_and_arg_are_same_type = type_checking(
                    param[1], argument[1]
                )
                if not check_if_param_and_arg_are_same_type:
                    raise ValueError(
                        f"Invalid argument'{argument[1]}' of type '{type(argument[1]).__name__}' not the same type as the parameter '{param[1]}'"
                    )
                print(check_if_param_and_arg_are_same_type)
                function_scope.insert(
                    VariableSymbol(param[2], param[1], argument[1], False)
                )
        statements_ast = check_if_function_exists.statements
        semantic_analyzer(statements_ast, function_scope)
    else:
        print(f"Function '{node[1]}' is not declared")
        raise ValueError(f"Function '{node[1]}' is not declared")


# # Handles conditionals
# def handle_conditionals(node):
#     if node[1][0] == "if":
#         helper_handle_if(node[1])
#     elif node[1][0] == "if_elif":
#         handle_if_elif(node[1])
#     elif node[1][0] == "if_else":
#         handle_if_else(node[1])
#     elif node[1][0] == "if_elif_else":
#         handle_if_elif_else(node[1])
#     elif node[1][0] == "aslongas_statement":
#         handle_aslongas(node[1])
#     elif node[1][0] == "for_loop":
#         handle_for_loop(node[1])
#     else:
#         raise ValueError("Invalid conditional")


# def handle_if_elif(node):
#     ifstatement = node[1]
#     helper_handle_if(ifstatement)
#     elifstatement = node[2]
#     helper_handle_elif(elifstatement)
#     print(node)

# def handle_if_else(node):
#     ifstatement = node[1]
#     helper_handle_if(ifstatement)
#     helper_handle_else(node[2])
#     print(node)

# def handle_if_elif_else(node):
#     ifstatement = node[1]
#     helper_handle_if(ifstatement)
#     helper_handle_elif(node[2])
#     helper_handle_else(node[3])
#     print(node)

# def helper_handle_if(node):
#     expression = handle_expression(node[1])
#     print(expression)
#     if isinstance(expression, bool):
#         semantic_analyzer(node[2])
#     else:
#         raise ValueError("Expected a boolean expression in IF statement")

# def helper_handle_elif(node):
#     expression = handle_expression(node[1])
#     print(expression)
#     if isinstance(expression, bool):
#         semantic_analyzer(node[2])
#     else:
#         raise ValueError("Expected a boolean expression in ELIF statement")

# def helper_handle_else(node):
#     semantic_analyzer(node[1])

# def handle_aslongas(node):
#     expression = handle_expression(node[1])
#     print(expression)
#     if type(expression) == bool:
#         semantic_analyzer(node[2])
#     else:
#         raise ValueError("Expected a boolean expression in ASLONGAS statement")

# # # Handles for loops
# # # TODO: Handle the identifier in the for loop, they need to local scope and be removed after the loop
# # # TODO: Handle the arguments in the for loop, they need to be added to the symbol table and removed after the loop
# # def handle_for_loop(node):
# if node[1] == "range":
#     print("Range")
#     for x in node[3]:
#         add = add_to_symbol_table(x[0], type(x[1]).__name__, x[1], "for_argument")
#         if add:
#             print(f"Added '{x[0]}' to symbol table")
#             semantic_analyzer(node[4])
# elif node[1] == "in":
#     # TODO: Add scope so that the variable declared in the for loop is removed after the loop and is used within the for loop
#     semantic_analyzer(node[4])
#     print("In")
# else:
#     raise ValueError("Invalid for loop")


# semantic_analyzer(prints, global_symbol_table)
