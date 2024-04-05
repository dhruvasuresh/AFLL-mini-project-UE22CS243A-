import ply.lex as lex

tokens = (
    'WHILE',
    'IDENTIFIER',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'PRINT',
    'LOGICAL',
    'RANGE',
    'COLON',
    'BOOL_TRUE',
    'BOOL_FALSE',
    'LESS_THAN'
)

t_NUMBER = r'(\d{1,3}(,\d{3})|\d+(\.\d)?)'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_\\-\\.]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_RANGE = r'\.\.'
t_COLON = r':'

def t_PRINT(t):
    r'print'
    return t

def t_WHILE(t):
    r'while'
    return t

def t_BOOL_TRUE(t):
    r'true'
    return t

def t_BOOL_FALSE(t):
    r'false'
    return t

def t_COMMA(t):
    r','
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Add a new token for the '<' operator
def t_LESS_THAN(t):
    r'<'
    return t

def t_LOGICAL(t):
    r'\&\&|\|\||\!|\&|\||<=|>=|>|<'
    return t


t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Build the lexer
lexer = lex.lex()


# Test the lexer with some input
input_text = '''
while (x < 10) {
    print(x)
    x = x + 1
}
'''
# Give the lexer some input
lexer.input(input_text)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
    