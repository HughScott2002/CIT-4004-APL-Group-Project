import ply.yacc as yacc

from lexer import tokens
from sourcecode import data as longdata
from shortsourcecode import data as shortdata


def p_program(p):
    """
    program : statements
    """
    p[0] = p[1]


def p_statements(p):
    """
    statements : statement statements
               | empty
    """
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = []


#   | attempt_block
#   | findout_block


def p_statement(p):
    """
    statement : declaration
              | assignment
              | abstract_call
              | abstract_function_declaration
              | print_statement
              | conditionals
              | attempt_findout_block

    """
    p[0] = p[1]


def p_declaration_with_assignment(p):
    """
    declaration : mutex type IDENTIFIER EQUAL expression LINEEND
    """
    p[0] = ("declaration", p[1], p[2], p[3], p[5])  # Literal value


def p_declaration_without_assignment(p):
    """declaration : mutex type IDENTIFIER LINEEND"""
    p[0] = ("declaration", p[1], p[2], p[3])


# ASSIGNMENT
def p_assignment(p):
    """
    assignment : IDENTIFIER EQUAL expression LINEEND
    """
    p[0] = ("assignment", p[1], p[2], p[3])


# ABSTRACT_CALL
def p_abstract_call(p):
    """
    abstract_call : HAIL FUNCTIONID LPAREN arguments RPAREN LINEEND
    """
    p[0] = ("abstract_call", p[2], p[4])


# ABSTRACT_FUNCTION_DECLARATION
def p_abstract_function_declaration(p):
    """
    abstract_function_declaration : ABSTRACT FUNCTIONID LPAREN parameters RPAREN LBRACE statements RBRACE
    """
    p[0] = ("abstract_function_declaration", p[2], p[4], p[7])


# PRINT_STATEMENT
def p_print_statement(p):
    """
    print_statement : SCRIBE LPAREN STRING_LITERAL COMMA IDENTIFIER RPAREN LINEEND
        | SCRIBE LPAREN STRING_LITERAL RPAREN LINEEND
        | SCRIBE LPAREN IDENTIFIER RPAREN LINEEND
    """
    p[0] = ("print_statement", p[3], p[5])


# CONDITIONALS
def p_conditionals(p):
    """
    conditionals : if_statement
                 | for_statement
                 | aslongas_statement
    """
    p[0] = p[1]


def p_for_statement(p):
    """
    for_statement : FOR IDENTIFIER IN RANGE LPAREN expression RPAREN LBRACE statements RBRACE
    """
    p[0] = ("for_loop", p[2], p[6], p[9])


def p_if_statement(p):
    """
    if_statement : IF expression LBRACE statements RBRACE
                 | IF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACE
                 | IF expression LBRACE statements RBRACE ELIF expression LBRACE statements RBRACE
                 | IF expression LBRACE statements RBRACE ELIF expression LBRACE statements RBRACE ELSE LBRACE statements RBRACE
    """
    if len(p) == 6:
        p[0] = ("if", p[2], p[4])
    elif len(p) == 9:
        if p[6] == "ELSE":
            p[0] = ("if_else", p[2], p[4], p[8])
        else:
            p[0] = ("if_elif", p[2], p[4], p[7])
    elif len(p) == 11:
        p[0] = ("if_elif_else", p[2], p[4], p[7], p[10])


# EXPRESSION
# def p_expression_uminus(p):
#     "expression : MINUS expression %prec UMINUS"
#     p[0] = -p[2]


def p_expression_group(p):
    "expression : LPAREN expression RPAREN"
    p[0] = p[2]


def p_expression(p):
    """
    expression : expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | expression POWER expression
               | expression NOTEQUAL expression
               | expression LESSTHAN expression
               | expression GREATERTHAN expression
               | expression LESSTHANOREQUAL expression
               | expression GREATERTHANOREQUAL expression
               | expression EQUIVALENT expression
               | expression BITWISEAND expression
               | expression BITWISEOR expression
               | expression BITWISEXOR expression
               | expression SHIFTLEFT expression
               | expression SHIFTRIGHT expression
               | NOT expression
               | PLUS expression
               | MINUS expression
               | BITWISEINVERT expression
               | INTEGER
               | FLOAT
               | IDENTIFIER
               | BOOLEAN
               | STRING_LITERAL
    """
    precedence = (
        ("left", "PLUS", "MINUS"),
        ("left", "TIMES", "DIVIDE"),
        ("left", "POWER"),
        ("right", "UNARY_MINUS", "UNARY_PLUS", "NOT", "BITWISEINVERT"),
        ("left", "BITWISEAND"),
        ("left", "BITWISEXOR"),
        ("left", "BITWISEOR"),
        ("left", "SHIFTLEFT", "SHIFTRIGHT"),
    )
    if len(p) == 4:
        # if isinstance(p[2], tuple):
        #     print("is a tuple")
        #     print(p[1])
        #     print(p[2])
        #     print(p[3])
        #     if p[2][0] == "add":
        #         p[0] = ("add", p[1], p[3])
        # p[0] = p[0]
        if p[2] == "+":
            p[0] = ("add", p[1], p[3])
        elif p[2] == "-":
            p[0] = ("sub", p[1], p[3])
        elif p[2] == "*":
            p[0] = ("mul", p[1], p[3])
        elif p[2] == "/":
            p[0] = ("div", p[1], p[3])
        elif p[2] == "**":
            p[0] = ("power", p[1], p[3])
        elif p[2] == "!=":
            p[0] = ("not_equal", p[1], p[3])
        elif p[2] == "<":
            p[0] = ("less_than", p[1], p[3])
        elif p[2] == ">":
            p[0] = ("greater_than", p[1], p[3])
        elif p[2] == "<=":
            p[0] = ("less_than_or_equal", p[1], p[3])
        elif p[2] == ">=":
            p[0] = ("greater_than_or_equal", p[1], p[3])
        elif p[2] == "==":
            p[0] = ("equivalent", p[1], p[3])
        elif p[2] == "&":
            p[0] = ("bitwise_and", p[1], p[3])
        elif p[2] == "|":
            p[0] = ("bitwise_or", p[1], p[3])
        elif p[2] == "^":
            p[0] = ("bitwise_xor", p[1], p[3])
        elif p[2] == "<<":
            p[0] = ("shift_left", p[1], p[3])
        elif p[2] == ">>":
            p[0] = ("shift_right", p[1], p[3])
        # print(type(p[2]))
        # print(p[2])
    elif len(p) == 3:
        if p[1] == "!":
            p[0] = ("not", p[2])
        elif p[1] == "+":
            p[0] = p[2]
        elif p[1] == "-":
            p[0] = ("unary_minus", p[2])
        elif p[1] == "~":
            p[0] = ("bitwise_invert", p[2])
    elif len(p) == 2:
        p[0] = p[1]
    else:
        raise ValueError("Invalid expression")

    # if isinstance(p[0], tuple):
    #     # print("Hit here *")
    #     # print("*2*")
    #     # print(p[0])
    #     # print("*2*")
    #     p[0] = p[0]  # Convert the result to a tuple for better performance
    # # print(p[0])


def p_attempt_findout_block(p):
    """
    attempt_findout_block : attempt_block findout_block
    """
    p[0] = ("attempt_findout_block", p[1], p[2])


# ATTEMPT_BLOCK
def p_attempt_block(p):
    """
    attempt_block : ATTEMPT LBRACE statements RBRACE
    """
    p[0] = ("attempt_block", p[3])


# FINDOUT_BLOCK
def p_findout_block(p):
    """
    findout_block : FINDOUT error_type LBRACE statements RBRACE
    """
    p[0] = ("findout_block", p[2], p[4])


# ASLONGAS_BLOCK
def p_aslongas_statement(p):
    """
    aslongas_statement : ASLONGAS expression LBRACE statements RBRACE
    """
    p[0] = ("aslongas_statement", p[2], p[4])


def p_error_type(p):
    """
    error_type : UNBOUNDLOCALERROR
                | TYPEERROR
                | VALUEERROR
                | INDEXERROR
                | KEYERROR
                | EXCEPTION
                | SYNTAXERROR
                | STOPITERATION
                | ARITHMETICERROR
                | FLOATINGPOINTERROR
                | OVERFLOWERROR
                | ZERODIVISIONERROR
                | ASSERTIONERROR
                | ATTRIBUTEERROR
                | BUFFERERROR
                | EOFERROR
                | IMPORTERROR
                | MODULENOTFOUNERROR
                | LOOKUPERROR
                | MEMORYERROR
                | NAMEERROR
                | BLOCKINGIOERROR
                | CHILDPROCESSERROR
                | CONNECTIONERROR
                | BROKENPIPEERROR
                | CONNECTIONABORTEDERROR
                | CONNECTIONREFUSEDERROR
                | CONNECTIONRESETERROR
                | FILEEXISTERROR
                | FILENOTFOUNERROR
                | INTERRUPTEDERROR
                | ISADIRECTORYERROR
                | NOTADIRECTORYERROR
                | PERMISSIONERROR
                | PROCESSLOOKUPERROR
                | TIMEOUTERROR
                | REFERENCEERROR
                | RUNTIMEERROR
                | INDENTATIONERROR
                | TABERROR
                | SYSTEMERROR
                | UNICODEERROR
                | UNICODEENCODEERROR
                | UNICODEDECODEERROR
                | UNICODETRANSLATEERROR
                | WARNING
                | USERWARNING
                | DEPRECATIONWARNING
                | PENDINGDEPRECATIONWARNING
                | SYNTAXWARNING
                | RUNTIMEWARNING
                | FUTUREWARNING
                | IMPORTWARNING
                | UNICODEWARNING
                | BYTESWARNING
                | RESOURCEWARNING
                | KEYBOARDINTERRUPT
    """
    p[0] = p[1]


def p_parameter(p):
    """
    parameter : type IDENTIFIER
    """
    p[0] = ("parameter", p[1], p[2])


def p_parameters(p):
    """
    parameters : parameter COMMA parameters
               | parameter
               | empty
    """
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []


def p_arguments(p):
    """
    arguments : argument COMMA arguments
              | argument
              | empty
    """
    if len(p) == 4:
        p[0] = [p[1]] + p[3]
    elif len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = []


def p_argument(p):
    """
    argument : IDENTIFIER
    """
    p[0] = ("argument_declaration", p[1])


def p_mutex(p):
    """
    mutex : UNLOCK
        | LOCK
    """
    p[0] = ("mutex_declaration", p[1])


def p_type(p):
    """
    type : INT_TYPE
         | FLOAT_TYPE
         | BOOL_TYPE
         | STRING_TYPE
    """
    p[0] = p[1]


def p_empty(p):
    """
    empty :
    """
    pass


def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, token='{p.value}'")
        raise ValueError(f"Syntax error at line {p.lineno}, token='{p.value} '")
    else:
        print("Syntax error at EOF")
        raise ValueError(f"Syntax error at EOF")


parser = yacc.yacc()

input_data = shortdata

result = parser.parse(input_data)
print(result)
