import parser_1 as parser
from shortsourcecode import data as shortdata
import ply.lex as lex

# from ast_1 import ast


symbol_table = {}


def add_to_symbol_table(var_name, var_type, var_value=None, is_locked=False):
    if var_name in symbol_table:
        # print(f"Variable '{var_name}' is already declared")
        # raise ValueError(f"Variable '{var_name}' is already declared")
        return False
    symbol_table[var_name] = (var_type, var_value, is_locked)
    return True


def check_symbol_table(var_name):
    if var_name in symbol_table:
        return True
    return False


# Type checking
def type_checking(var_type, value):
    if var_type == "int":
        if not isinstance(value, int):
            print(f"Expected an integer, got '{value}'")
            # raise ValueError(f"Expected an integer, got '{value}'")
            return False
        else:
            return True
    elif var_type == "float":
        if not isinstance(value, float):
            print(f"Expected a float, got '{value}'")
            # raise ValueError(f"Expected a float, got '{value}'")
            return False
        else:
            return True
    elif var_type == "bool":
        if not isinstance(value, bool):
            print(f"Expected a boolean, got '{value}'")
            # raise ValueError(f"Expected a boolean, got '{value}'")
            return False
        else:
            return True
    elif var_type == "string":
        if not isinstance(value, str):
            print(f"Expected a string, got '{value}'")
            # raise ValueError(f"Expected a string, got '{value}'")
            return False
        else:
            return True
    else:
        print(f"Unknown type '{var_type}'")
        # raise ValueError(f"Unknown type '{var_type}'")
        return False


def semantic_analyzer(ast):
    for x in ast:
        if x[0] == "declaration":
            handle_declaration(x)
        elif x[0] == "assignment":
            handle_assignment(x)
        elif x[0] == "abstract_function_declaration":
            handle_assignment(x)
        # elif x[0] == "abstract_call":
        #     print(x[1])
        # elif x[0] == "parameter":
        #     print(x[2])
        # elif x[0] == "argument_declaration":
        #     print(x[2])


def handle_declaration(node):
    if len(node) == 4:
        var_mut, var_type, var_name = node[1][1], node[2], node[3]
        is_locked = ""
        if var_mut == "lock":
            is_locked = True
        else:
            is_locked = False
        # type_checking(var_type, None)
        check_symbol = add_to_symbol_table(var_name, var_type, None, is_locked)
        if check_symbol:
            print(f"Declared '{var_mut}' variable '{var_name}' of type '{var_type}'")
        else:
            print(f"Variable '{var_name}' is already declared")
    elif len(node) == 5:
        var_mut, var_type, var_name, value = node[1][1], node[2], node[3], node[4]
        is_locked = var_mut == "lock"
        # Checks if the type is correct
        type_check = type_checking(var_type, value)
        if not type_check:
            print(f"Error in type checking for '{var_name}'")
        # Adds to the symbol table or sends back false
        check_symbol = add_to_symbol_table(var_name, var_type, value, is_locked)
        if check_symbol:
            print(f"'{var_name}' added to symbol table")
            print(symbol_table)
        else:
            print(f"Variable '{var_name}' is already declared")
        print(
            f"Declared '{var_mut}' variable '{var_name}' of type '{var_type}' with value '{value}'"
        )
    else:
        raise ValueError("Invalid declaration")


def handle_assignment(node):
    if len(node) == 4:
        var_name, value = node[1], node[3]
        check_symbol = check_symbol_table(var_name)
        if not check_symbol:
            print(f"Undeclared variable '{var_name}'")
        else:
            var_type, old_value, is_locked = symbol_table[var_name]
            if is_locked and old_value is not None:
                print(f"Cannot reassign locked variable '{var_name}'")
                raise ValueError(f"Cannot reassign locked variable '{var_name}'")
            else:
                type_check = type_checking(var_type, value)
                if type_check:
                    symbol_table[var_name] = (var_type, value, is_locked)
                    print(f"Assigned value '{value}' to variable '{var_name}'")
                else:
                    print(
                        f"Type mismatch for variable '{var_name}' expected '{var_type}'"
                    )
    else:
        raise ValueError("Invalid assignment")


# semantic_analyzer(ast)

# class SemanticAnalyzer:
#     def __init__(self):
#         self.symbol_table = {}

#     def analyze(self, ast):
#         self.visit(ast)

#     def visit(self, node):
#         if isinstance(node, tuple):
#             node_type = node[0]

#             if node_type == "declaration":
#                 self.handle_declaration(node)
#             elif node_type == "abstract_function_declaration":
#                 self.handle_function_declaration(node)
#             elif node_type == "abstract_call":
#                 self.handle_function_call(node)
#             # elif node_type == "if":
#             #     self.handle_if_statement(node)
#             # elif node_type == "for_loop":
#             #     self.handle_for_loop(node)
#             # elif node_type == "aslongas_statement":
#             #     self.handle_while_loop(node)
#             # elif node_type == "attempt_block":
#             #     self.handle_try_block(node)
#             # elif node_type == "findout_block":
#             #     self.handle_except_block(node)
#             else:
#                 for child in node[1:]:
#                     self.visit(child)

#     def handle_declaration(self, node):
#         _, data_type, identifier, *value = node
#         if identifier in self.symbol_table:
#             raise ValueError(f"Variable '{identifier}' is already declared.")
#         self.symbol_table[identifier] = data_type

#     def handle_function_declaration(self, node):
#         _, function_name, parameters, body = node
#         if function_name in self.symbol_table:
#             raise ValueError(f"Function '{function_name}' is already declared.")
#         self.symbol_table[function_name] = ("function", parameters, body)

#     def handle_function_call(self, node):
#         _, function_name, arguments = node
#         if function_name not in self.symbol_table:
#             raise ValueError(f"Function '{function_name}' is not declared.")
#         function_info = self.symbol_table[function_name]
#         if function_info[0] != "function":
#             raise ValueError(f"'{function_name}' is not a function.")

#     # Additional checks for arguments and parameters can be done here

#     # Implement handlers for other AST nodes


# # lexer = lex.lex()
# # parser = yacc.yacc()
# # ast = parser.parse(shortdata)
# # ast = ("declaration", "bool", "_BINARY", True)
# # semantic_analyzer = SemanticAnalyzer()
# # semantic_analyzer.analyze(ast)
