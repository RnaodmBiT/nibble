from ply import lex

# List of tokens in the nibble files
tokens = [
    "ID",
    "LBRACE", "RBRACE",
    "COLON", "SEMICOLON"
]

# Reserved keywords
reserved = {
    "struct": "STRUCT"
}

tokens += reserved.values()

# Define the regular expressions for the tokens
t_LBRACE = "{"
t_RBRACE = "}"
t_COLON = ":"
t_SEMICOLON = ";"
t_ignore = " \t\n"

def t_ID(t):
    r"[_a-zA-Z]+[_a-zA-Z0-9]*"
    if t.value in reserved:
        t.type = reserved[t.value]
    return t

# Handle the error case
def t_error(t):
    raise LexerError("Illegal character '{}'".format(t.value))

lexer = lex.lex()