import ply.lex as lex
from sourcecode import data as longdata
from shortsourcecode import data as shortdata

# Reserved words and type specifiers
reserved_word = {
    "abstract": "ABSTRACT",
    "hail": "HAIL",
    "scribe": "SCRIBE",
    "unlock": "UNLOCK",
    "lock": "LOCK",
    "if": "IF",
    "elif": "ELIF",
    "then": "THEN",
    "else": "ELSE",
    "for": "FOR",
    "do": "DO",
    "while": "WHILE",
    "end": "END",
    "print": "PRINT",
    "contract": "CONTRACT",
    "public": "PUBLIC",
    "private": "PRIVATE",
    "internal": "INTERNAL",
    "external": "EXTERNAL",
    "return": "RETURN",
    "returns": "RETURNS",
    "emit": "EMIT",
    "event": "EVENT",
    "int": "INT_TYPE",
    "float": "FLOAT_TYPE",
    "bool": "BOOL_TYPE",
    "string": "STRING_TYPE",
    "var": "VAR",
    "range": "RANGE",
    "in": "IN",
    "aslongas": "ASLONGAS",
    "attempt": "ATTEMPT",
    "findout": "FINDOUT",
    "exception": "EXCEPTION",
    "stoptteration": "STOPITERATION",
    "arithmeticerror": "ARITHMETICERROR",
    "floatingpointerror": "FLOATINGPOINTERROR",
    "overflowerror": "OVERFLOWERROR",
    "zerodivisionerror": "ZERODIVISIONERROR",
    "assertionerror": "ASSERTIONERROR",
    "attributeerror": "ATTRIBUTEERROR",
    "buffererror": "BUFFERERROR",
    "eoferror": "EOFERROR",
    "importerror": "IMPORTERROR",
    "modulenotfounderror": "MODULENOTFOUNERROR",
    "lookuperror": "LOOKUPERROR",
    "indexerror": "INDEXERROR",
    "keyerror": "KEYERROR",
    "memoryerror": "MEMORYERROR",
    "nameerror": "NAMEERROR",
    "unboundlocalerror": "UNBOUNDLOCALERROR",
    "oserror": "OSERROR",
    "blockingioerror": "BLOCKINGIOERROR",
    "childprocesserror": "CHILDPROCESSERROR",
    "connectionerror": "CONNECTIONERROR",
    "brokenpipeerror": "BROKENPIPEERROR",
    "connectionabortederror": "CONNECTIONABORTEDERROR",
    "connectionrefusederror": "CONNECTIONREFUSEDERROR",
    "connectionreseterror": "CONNECTIONRESETERROR",
    "fileexistserror": "FILEEXISTERROR",
    "filenotfounderror": "FILENOTFOUNERROR",
    "interruptederror": "INTERRUPTEDERROR",
    "isadirectoryerror": "ISADIRECTORYERROR",
    "notadirectoryerror": "NOTADIRECTORYERROR",
    "permissionerror": "PERMISSIONERROR",
    "processlookuperror": "PROCESSLOOKUPERROR",
    "timeouterror": "TIMEOUTERROR",
    "referenceerror": "REFERENCEERROR",
    "runtimeerror": "RUNTIMEERROR",
    "syntaxerror": "SYNTAXERROR",
    "indentationerror": "INDENTATIONERROR",
    "taberror": "TABERROR",
    "systemerror": "SYSTEMERROR",
    "typeerror": "TYPEERROR",
    "valueerror": "VALUEERROR",
    "unicodeerror": "UNICODEERROR",
    "unicodeencodeerror": "UNICODEENCODEERROR",
    "unicodedecodeerror": "UNICODEDECODEERROR",
    "unicodetranslateerror": "UNICODETRANSLATEERROR",
    "warning": "WARNING",
    "userwarning": "USERWARNING",
    "deprecationwarning": "DEPRECATIONWARNING",
    "pendingdeprecationwarning": "PENDINGDEPRECATIONWARNING",
    "syntaxwarning": "SYNTAXWARNING",
    "runtimewarning": "RUNTIMEWARNING",
    "futurewarning": "FUTUREWARNING",
    "importwarning": "IMPORTWARNING",
    "unicodewarning": "UNICODEWARNING",
    "byteswarning": "BYTESWARNING",
    "resourcewarning": "RESOURCEWARNING",
    "keyboardinterrupt": "KEYBOARDINTERRUPT",
}

# type_specifiers = {"int", "string", "bool", "address"}
mutables = {"lock", "unlock"}
# Token list
tokens = [
    "INTEGER",
    "FLOAT",
    "BOOLEAN",
    "EQUAL",
    "PLUS",
    "LINEEND",
    "MINUS",
    "TIMES",
    "DIVIDE",
    "LESSTHAN",
    "GREATERTHAN",
    "LESSTHANOREQUAL",
    "GREATERTHANOREQUAL",
    "NOTEQUAL",
    "EQUIVALENT",
    "SEMICOLON",
    "COLON",
    "COMMA",
    "LPAREN",
    "RPAREN",
    "LBRACE",
    "RBRACE",
    "IDENTIFIER",
    "FUNCTIONID",
    "VISIBILITY",
    # "ADDRESS_LITERAL",
    "STRING_LITERAL",
    "TYPE_SPECIFIER",
    "NOT",
    "POWER",  # Added POWER token
    "BITWISEAND",  # Added BITWISEAND token
    "BITWISEOR",  # Added BITWISEOR token
    "BITWISEXOR",  # Added BITWISEXOR token
    "SHIFTLEFT",  # Added SHIFTLEFT token
    "SHIFTRIGHT",  # Added SHIFTRIGHT token
    "BITWISEINVERT",  # Added BITWISEINVERT token
] + list(reserved_word.values())

# Ignored characters
t_ignore = "\t "
t_ignore_COMMENT = r"//.*|\#[^\n]*"

# Regular expressions for operators and punctuations
t_EQUAL = r"="
t_PLUS = r"\+"
t_MINUS = r"-"
t_TIMES = r"\*"
t_DIVIDE = r"/"
t_LESSTHAN = r"<"
t_GREATERTHAN = r">"
t_LESSTHANOREQUAL = r"<="
t_GREATERTHANOREQUAL = r">="
t_NOTEQUAL = r"!="
t_NOT = r"!"
t_EQUIVALENT = r"=="
t_SEMICOLON = r";"
t_COLON = r":"
t_LINEEND = r"@"
t_COMMA = r","
t_LPAREN = r"\("
t_RPAREN = r"\)"
t_LBRACE = r"\{"
t_RBRACE = r"\}"
t_POWER = r"\*\*"  # Added regular expression for POWER token
t_BITWISEAND = r"&"  # Added regular expression for BITWISEAND token
t_BITWISEOR = r"\|"  # Added regular expression for BITWISEOR token
t_BITWISEXOR = r"\^"  # Added regular expression for BITWISEXOR token
t_SHIFTLEFT = r"<<"  # Added regular expression for SHIFTLEFT token
t_SHIFTRIGHT = r">>"  # Added regular expression for SHIFTRIGHT token
t_BITWISEINVERT = r"~"  # Added regular expression for BITWISEINVERT token


# Define a function identifier token
def t_FUNCTIONID(t):
    r"[A-Z][A-Z_0-9]*"
    if t.value in reserved_word:
        t.type = reserved_word[t.value]
    else:
        t.type = "FUNCTIONID"
    return t
    # t.type = "FUNCTIONID"
    # return t


# Regular expression rule for booleans
def t_BOOLEAN(t):
    r"true|false"
    t.value = bool(t.value == "true")
    return t


# def t_match_error(t):
#     r"Error[a-zA-Z_0-9]*"
#     # r"_?[a-zA-Z][a-zA-Z_0-9]*"
#     if t.value in reserved_word:
#         t.type = reserved_word[t.value]
#     else:
#         t.type = "ERROR"
#     return t


# Define an identifier token
def t_IDENTIFIER(t):
    r"_?[a-zA-Z][a-zA-Z_0-9]*"
    if t.value in reserved_word:
        t.type = reserved_word[t.value]
    else:
        t.type = "IDENTIFIER"
    return t


# Regular expression rule for floats
def t_FLOAT(t):
    r"\d+\.\d+"
    t.value = float(t.value)
    return t


# Regular expression rule for integers
def t_INTEGER(t):
    r"\d+"
    t.value = int(t.value)
    return t


# Define a string literal token
def t_STRING_LITERAL(t):
    r'"([^"\\]|\\.)*"'
    t.value = t.value[1:-1]
    t.type = "STRING_LITERAL"
    return t


# Define a boolean token
def t_BOOL(t):
    r"true|false"
    t.type = "BOOL"
    return t


# Define a visibility token
def t_VISIBILITY(t):
    r"private|public"
    t.type = "VISIBILITY"
    return t


# Define a newline token to track line numbers
def t_newline(t):
    r"\n+"
    t.lexer.lineno += len(t.value)


# Error handling for invalid characters
def t_error(t):
    print(f"********************************")
    print(f"ERROR: Invalid Character {t.value[0]} at line {t.lineno}")
    print(f"********************************")
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

# def t_IDENTIFIER(t):
#     r"_?[a-zA-Z][a-zA-Z_0-9]*"
#     if t.value.startswith("_"):
#         t.type = "IDENTIFIER"
#     elif t.value in reserved_word:
#         t.type = reserved_word[t.value]
#     return t


# def t_keyword(t):
#     r"[A-Z][a-zA-Z]*"
#     if t.value in reserved_word:
#         t.type = reserved_word[t.value]
#     else:
#         t.type = "IDENTIFIER"
#     return t


# # Regular expression rule for floats
# def t_FLOAT(t):
#     r"\d+\.\d*"
#     t.value = float(t.value)
#     return t


# Define an address literal token
# def t_ADDRESS_LITERAL(t):
#     r'"0x[a-fA-F0-9]{40}"|"[a-fA-F0-9]{64}"'
#     t.value = t.value[1:-1]  # Extract the actual address value
#     t.type = "ADDRESS_LITERAL"
#     return t


# Test the lexer

lexer.input(shortdata)

# for token in lexer:
#     print("*********************************")
#     print("TOKEN TYPE: ", token.type)
#     print("TOKEN VALUE: ", token.value)
#     print("TOKEN LINE NUMBER: ", token.lineno)
#     print("TOKEN POSITION: ", token.lexpos)
#     print("*********************************")

# for token in lexer:
#     print(token.type)
