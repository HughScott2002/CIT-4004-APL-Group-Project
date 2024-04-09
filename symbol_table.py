# Symbol table entry for variables
# name, var_type, value=None, is_locked=True
class VariableSymbol:
    def __init__(self, name, var_type, value=None, is_locked=True):
        self.name = name
        self.type = var_type
        self.value = value
        self.is_locked = is_locked
        # self.visibility = visibility


# Symbol table entry for functions
# name, params, return_type, statements
class FunctionSymbol:
    def __init__(self, name, params, return_type, statements):
        self.name = name
        self.params = params
        # Return type is not used in the current implementation
        self.return_type = return_type
        self.statements = statements
        # self.visibility = visibility


# Symbol table for handling nested scopes
class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent
        self.child_scopes = []

    def insert(self, symbol):
        if symbol.name in self.symbols:
            return False
        self.symbols[symbol.name] = symbol
        return True

    def lookup(self, name, current_scope_only=False):
        symbol = self.symbols.get(name)
        if symbol is not None:
            # Symbol found in the current scope
            return symbol
        elif not current_scope_only and self.parent:
            # Symbol not found in the current scope, looking in the parent scope
            return self.parent.lookup(name)
        else:
            # "Symbol not found in the current scope or its parents"
            return None

    def update(self, name, new_symbol):
        if name not in self.symbols:
            raise ValueError(f"Symbol '{name}' does not exist and couldn't be updated")
        self.symbols[name] = new_symbol

    def get_all_symbols(self):
        symbols = {}
        self._collect_symbols(symbols)
        return symbols

    def _collect_symbols(self, symbols):
        for symbol_name, symbol in self.symbols.items():
            symbols[symbol_name] = symbol

        for child_scope in self.child_scopes:
            child_scope._collect_symbols(symbols)


# Function to create a new scope
def new_scope(parent=None):
    new_scope = SymbolTable(parent)
    if parent is not None:
        parent.child_scopes.append(new_scope)
    return new_scope


# Test the symobol table here |
#                             V


# # Global symbol table
# global_symbol_table = SymbolTable()

# # Create a new scope (e.g. inside a function)
# plus = new_scope(global_symbol_table)  # This is a new scope inside the global scope
# minus = new_scope(global_symbol_table)  # This is a new scope inside the global scope
# inside_plus = new_scope(plus)  # This is a new scope inside the plus scope

# # Example usage
# # Declare global variables

# global_symbol_table.insert(
#     VariableSymbol(
#         "_Global_var", "str", value="This is a global variable.", is_locked=False
#     )
# )
# global_symbol_table.insert(VariableSymbol("_A", "int", value=5))
# global_symbol_table.insert(VariableSymbol("_TEN", "int", value=10))
# global_symbol_table.insert(VariableSymbol("_PI", "float", value=3.14))
# global_symbol_table.insert(
#     VariableSymbol("_BINARY", "bool", value=True, is_locked=False)
# )

# # Declare a function
# func_params = [
#     VariableSymbol("_X", "int"),
#     VariableSymbol("_Y", "int"),
# ]
# func_symbol = FunctionSymbol(
#     "PLUS",
#     func_params,
#     "void",
#     [
#         ("declaration", ("mutex_declaration", "lock"), "float", "_A", 5.5),
#         ("declaration", ("mutex_declaration", "lock"), "float", "_B", 10.5),
#         (
#             "declaration",
#             ("mutex_declaration", "lock"),
#             "float",
#             "_SUM",
#             ("add", "_A", "_B"),
#         ),
#     ],
# )
# global_symbol_table.insert(func_symbol)


# # Declare local variables
# plus.insert(VariableSymbol("_A", "float", value=95.5))
# plus.insert(VariableSymbol("_B", "float", value=10.5))
# plus.insert(VariableSymbol("_SUM", "float", value=15.5))

# minus.insert(VariableSymbol("_A", "bool", value=True))
# minus.insert(VariableSymbol("_BB", "float", value=20.5))
# minus.insert(VariableSymbol("_SUMM", "float", value=25.5))

# inside_plus.insert(VariableSymbol("_Locked_var", "int", value=42, is_locked=True))
# inside_plus.insert(
#     VariableSymbol("_My_Name", "string", value="TypeSnake", is_locked=True)
# )
# inside_plus.insert(
#     VariableSymbol("_A", "string", value="A inside the inside_plus scope")
# )

# # Lookup symbols
# print("Global Symbol Table:")
# print(
#     "This is the variable _Global_var =",
#     global_symbol_table.lookup("_Global_var").value,
# )  # Output: This is a global variable.
# print(
#     "This is the variable _TEN =", global_symbol_table.lookup("_TEN").value
# )  # Output: 10
# print(
#     "This is the variable _PI =", global_symbol_table.lookup("_PI").value
# )  # Output: 3.14
# print(
#     "This is the variable _BINARY =", global_symbol_table.lookup("_BINARY").value
# )  # Output: True
# print(
#     "This is the function delcared =", global_symbol_table.lookup("PLUS").name
# )  # Output: PLUS
# print("\n")

# print("Plus Symbol Table:")
# print("_B in plus scope = ", plus.lookup("_B").value)  # Output: 10.5
# print("_SUM in plus scope = ", plus.lookup("_SUM").value)  # Output: 15.5
# print("\n")

# print("Minus Symbol Table:")
# print("_BB in minus scope = ", minus.lookup("_BB").value)  # Output: 20.5
# print("_SUMM in minus scope = ", minus.lookup("_SUMM").value)  # Output: 25.5
# print("\n")

# print("Inside Plus Symbol Table:")
# print(
#     "_Locked_var in inside_plus scope", inside_plus.lookup("_Locked_var").is_locked
# )  # Output: True
# print(
#     "_My_Name in inside_plus scope", inside_plus.lookup("_My_Name").value
# )  # Output: TypeSnake
# print("\n")

# print("Variable Shadowing:")
# # Notice how _A can be redefined inside each scope
# print("_A in global scope =", global_symbol_table.lookup("_A").value)  # Output: 5
# print("_A in minus scope = ", minus.lookup("_A").value)  # Output: True
# print("_A in plus scope =", plus.lookup("_A").value)  # Output: 95.5
# print(
#     "_A in inside_plus scope", inside_plus.lookup("_A").value
# )  # Output: A inside the inside_plus scope
