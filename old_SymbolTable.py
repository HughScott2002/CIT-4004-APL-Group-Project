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
