import ply.lex as lex
from sourcecode import data as longdata
from shortsourcecode import data as shortdata

#####################################
#         Authors:
#####################################
# Hugh Scott
# Barrington Patterson
# Sharethia McCarthy
# Christina Wilson


# Reserved words
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

# list holing the mutex states
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
    "POWER",
    "BITWISEAND",
    "BITWISEOR",
    "BITWISEXOR",
    "SHIFTLEFT",
    "SHIFTRIGHT",
    "BITWISEINVERT",
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
t_POWER = r"\*\*"
t_BITWISEAND = r"&"
t_BITWISEOR = r"\|"
t_BITWISEXOR = r"\^"
t_SHIFTLEFT = r"<<"
t_SHIFTRIGHT = r">>"
t_BITWISEINVERT = r"~"


# Function identifier token
def t_FUNCTIONID(t):
    r"[A-Z][A-Z_0-9]*"
    if t.value in reserved_word:
        t.type = reserved_word[t.value]
    else:
        t.type = "FUNCTIONID"
    return t


# Regular expression rule for booleans
def t_BOOLEAN(t):
    r"true|false"
    t.value = bool(t.value == "true")
    return t


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
    print(f"ERROR: Invalid Character {t.value[0]!r} at line {t.lineno}")
    print(f"********************************")
    t.lexer.skip(1)


# EOF handling rule
# def t_eof(t):
#     # Get more input (Example)
#     more = raw_input("... ")
#     if more:
#         t.lexer.input(more)
#         return t.lexer.token()
#     return None


# Build the lexer
lexer = lex.lex()

# Test the lexer here |
#                     V
lexer.input("( ) + = -")
for token in lexer:
    print(token.type)
    print(token.value)
    print("  ")
