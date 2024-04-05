# Symbol Tables


# Global symbol table
# Everything that is declared globally is stored in the global symbol table.
global_symbol_table = {}
# (name, type="variable"| "function")

# Local symbol table within a function or block
# This table stores all the variables declared within a function or block.
local_symbol_table = {}
# (name, type="variable"| "function", locale="function" | "block")

# Variable symbol table
# This table stores all the variables declared in the program.
variable_symbol_table = {}
# (var_name, var_type, var_value=None, is_locked=True)


# Function symbol table
# This table stores all the functions declared in the program.
function_symbol_table = {}
# (function_name, params, statements)


symbol_table = {}


# Add to the symbol table
def add_to_symbol_table(
    var_name, var_type, var_value=None, is_locked=True, symbol_type="variable"
):
    check_table = check_symbol_table(var_name)
    if check_table:
        return False
    else:
        symbol_table[var_name] = (var_type, var_value, is_locked, symbol_type)
    return True


def add_to_abstract_function_symbol_table(abs_name, params, statements):
    if abs_name in function_symbol_table:
        return False
    else:
        function_symbol_table[abs_name] = (params, statements)
        return True


def check_abstract_function_symbol_table(abs_name):
    if abs_name in function_symbol_table:
        return True
    return False


# Check if the variable is in the symbol table
def check_symbol_table(var_name):
    if var_name in symbol_table:
        return True
    return False


# Symbol table entry for variables
# class VariableSymbol:
#     def __init__(
#         self, name, var_type, value=None, is_locked=True, visibility="private"
#     ):
#         self.name = name
#         self.type = var_type
#         self.value = value
#         self.is_locked = is_locked
#         self.visibility = visibility


# Symbol table entry for functions
# class FunctionSymbol:
#     def __init__(self, name, params, return_type, statements, visibility="private"):
#         self.name = name
#         self.params = params
#         self.return_type = return_type
#         self.statements = statements
#         self.visibility = visibility

# # Symbol table for handling nested scopes
# class SymbolTable:
#     def __init__(self, parent=None):
#         self.symbols = {}
#         self.parent = parent

#     def insert(self, symbol):
#         if symbol.name in self.symbols:
#             raise ValueError(f"Symbol '{symbol.name}' already exists in the current scope.")
#         self.symbols[symbol.name] = symbol

#     def lookup(self, name, current_scope_only=False):
#         symbol = self.symbols.get(name)
#         if symbol is not None:
#             return symbol
#         elif not current_scope_only and self.parent:
#             return self.parent.lookup(name)
#         else:
#             return None

#     def update(self, name, new_symbol):
#         if name not in self.symbols:
#             raise ValueError(f"Symbol '{name}' does not exist in the current scope.")
#         self.symbols[name] = new_symbol

# def new_scope(parent=None):
#     return SymbolTable(parent)

# def insert_symbol(symbol_table, symbol):
#     symbol_table.insert(symbol)

# def lookup_symbol(symbol_table, name, current_scope_only=False):
#     return symbol_table.lookup(name, current_scope_only)

# def update_symbol(symbol_table, name, new_symbol):
#     symbol_table.update(name, new_symbol)

# # Global symbol table
# global_symbol_table = SymbolTable()

# # Example usage
# # Declare global variables
# insert_symbol(global_symbol_table, VariableSymbol("global_var", "int", value=42))
# insert_symbol(global_symbol_table, VariableSymbol("locked_var", "bool", value=True, is_locked=True))

# # Declare a function
# func_params = [VariableSymbol("x", "int"), VariableSymbol("y", "int")]
# func_symbol = FunctionSymbol("my_func", func_params, "int", [])
# insert_symbol(global_symbol_table, func_symbol)

# # Create a new scope (e.g., inside a function)
# local_scope = new_scope(global_symbol_table)

# # Declare local variables
# insert_symbol(local_scope, VariableSymbol("local_var", "float", value=3.14))
# insert_symbol(local_scope, VariableSymbol("another_var", "string", value="hello"))

# # Lookup symbols
# print(lookup_symbol(local_scope, "local_var").value)  # Output: 3.14
# print(lookup_symbol(local_scope, "global_var").value)  # Output: 42
# print(lookup_symbol(local_scope, "locked_var").is_locked)  # Output: True
# print(lookup_symbol(local_scope, "my_func").return_type)  # Output: int


# 1111
