import ply.lex as lex
tokens = (
    'if',
    'print',
    'LPAREN',
    'RPAREN',
    'let',
    'LOGICAL',
    'dquote',
    'ASSIGN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'identifier',
    'NUMBER',
    'RBRACE',
    'LBRACE'
)

t_NUMBER = r'\d+(\.\d+)?'
t_identifier = r'[a-zA-Z_][a-zA-Z0-9_\\-\\.]*'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
def t_dquote(t):
    r'"'
    return t
def t_if(t):
    r'if'
    return t
def t_print(t):
    r'print'
    return t
def t_let(t):
    r'let'
    return t
def t_LOGICAL(t):
    r'\&\&|\|\||\!|\&|\||\<=|\>=|\>|\<' 

    return t
t_ignore = ' \t'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Test the lexer with some input
input_text = '''
    if age>=18 {print("you are a adult")}
'''

# Give the lexer some input
lexer.input(input_text)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)