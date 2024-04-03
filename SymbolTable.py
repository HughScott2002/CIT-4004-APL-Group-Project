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


# Check if the variable is in the symbol table
def check_symbol_table(var_name):
    if var_name in symbol_table:
        return True
    return False
