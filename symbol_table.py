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
        self.return_type = return_type
        self.statements = statements
        # self.visibility = visibility


# Symbol table for handling nested scopes
class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def insert(self, symbol):
        if symbol.name in self.symbols:
            return False
            # raise ValueError(
            #     f"Symbol '{symbol.name}' already exists in the current scope."
            # )
        self.symbols[symbol.name] = symbol
        return True

    def lookup(self, name, current_scope_only=False):
        symbol = self.symbols.get(name)
        if symbol is not None:
            return symbol
        elif not current_scope_only and self.parent:
            return self.parent.lookup(name)
        else:
            # raise ValueError(f"Symbol '{name}' not found in the current scope.")
            return None

    def update(self, name, new_symbol):
        if name not in self.symbols:
            raise ValueError(f"Symbol '{name}' does not exist and couldn't be updated")
        self.symbols[name] = new_symbol

    # def dump(self):
    #     print("Symbols in the current scope:")
    #     for key, value in self.symbols.items():
    #         if self.symbols.get(key):
    #             print(f"Name: {key}, Value: {value.value}")
    #         print(f"Name: {key}, Value: {value[key]}")


# Function to create a new scope
def new_scope(parent=None):
    return SymbolTable(parent)


# # Global symbol table
# global_symbol_table = SymbolTable()
# # Create a new scope (e.g. inside a function)
# plus = new_scope(global_symbol_table)
# minus = new_scope(global_symbol_table)

# # # # Example usage
# # # # Declare global variables

# global_symbol_table.insert(
#     VariableSymbol(
#         "_Global_var", "str", value="This is a global variable.", is_locked=False
#     )
# )
# global_symbol_table.insert(VariableSymbol("_TEN", "int", value=10))
# global_symbol_table.insert(VariableSymbol("_PI", "float", value=3.14))
# # global_symbol_table.insert(VariableSymbol("_PI", "float", value=3.14))
# global_symbol_table.insert(
#     VariableSymbol("_BINARY", "bool", value=True, is_locked=False)
# )
# global_symbol_table.insert(VariableSymbol("_Assignment", "int", value=None))
# global_symbol_table.update("_Assignment", VariableSymbol("_Assignment", "int", value=5))
# global_symbol_table.insert(
#     VariableSymbol("locked_var", "bool", value=True, is_locked=True)
# )

# # # Declare a function
# # # func_params = [VariableSymbol("x", "int"), VariableSymbol("y", "int")]
# # # Maybe change these form being locked
# # func_params = [
# #     VariableSymbol("_X", "int"),
# #     VariableSymbol("_Y", "int"),
# # ]
# # # Maybe I should and and arguments sections to the function symbol
# # func_symbol = FunctionSymbol(
# #     "PLUS",
# #     func_params,
# #     "void",
# #     [
# #         ("declaration", ("mutex_declaration", "lock"), "float", "_A", 5.5),
# #         ("declaration", ("mutex_declaration", "lock"), "float", "_B", 10.5),
# #         (
# #             "declaration",
# #             ("mutex_declaration", "lock"),
# #             "float",
# #             "_SUM",
# #             ("add", "_A", "_B"),
# #         ),
# #     ],
# # )
# # global_symbol_table.insert(func_symbol)


# # # # Declare local variables
# plus.insert(VariableSymbol("_A", "float", value=5.5))
# plus.insert(VariableSymbol("_B", "float", value=10.5))
# plus.insert(VariableSymbol("_SUM", "float", value=15.5))

# minus.insert(VariableSymbol("_AA", "float", value=15.5))
# minus.insert(VariableSymbol("_BB", "float", value=20.5))
# minus.insert(VariableSymbol("_SUMM", "float", value=25.5))

# # # Lookup symbols

# # print("*******These are the gobal variables*******")
# # print(
# #     global_symbol_table.lookup("_Global_var").value
# # )  # Output: This is a global variable.
# # print(global_symbol_table.lookup("_TEN").value)  # Output: 10
# # print(global_symbol_table.lookup("_PI").value)  # Output: 3.14
# # print(global_symbol_table.lookup("_BINARY").value)  # Output: True
# # print(global_symbol_table.lookup("_Assignment").value)  # Output: 5


# # print("\n")
# # print("*******These are the local variables*******")
# print(plus.lookup("_A").value)  # Output: 5.5
# print(plus.lookup("_B").value)  # Output: 10.5
# print(plus.lookup("_SUM").value)  # Output: 15.5
# # print(plus.lookup("local_var").value)  # Output: 3.14
# # print(plus.lookup("global_var").value)  # Output: 42
# print(plus.lookup("locked_var").is_locked)  # Output: True
# # print(plus.lookup("my_func").return_type)  # Output: int
# print(plus.lookup("_TEN").value)  # Output: 10
# # print(global_symbol_table.lookup("_A").value)  # Output: Error


# print(minus.lookup("_AA").value)  # Output: 15.5
# print(minus.lookup("_BB").value)  # Output: 20.5
# print(minus.lookup("_SUMM").value)  # Output: 25.5
# print(minus.lookup("_SUM").is_locked)  # Output: True
