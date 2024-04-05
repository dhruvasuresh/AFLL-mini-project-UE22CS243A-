import ply.lex as lex

tokens = (
    'FOR',
    'IN',
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
)

t_NUMBER = r'\d+(\.\d+)?'
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

def t_PRINT(t):
    r'print'
    return t

def t_FOR(t):
    r'for'
    return t

def t_IN(t):
    r'in'
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

def t_LOGICAL(t):
    r'\&\&|\|\||\!|\&|\||\<=|\>=|\>|\<'
    return t

t_ignore = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Build the lexer
lexer = lex.lex()

# Test the lexer with some input
input_text = '''
for i in 0..10 {print(i)}
'''

# Give the lexer some input
lexer.input(input_text)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)