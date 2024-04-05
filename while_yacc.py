import ply.yacc as yacc
from while_lex import tokens

def p_while_statement(p):
    '''while_statement : WHILE LPAREN expression RPAREN LBRACE statements RBRACE'''
    p[0] = f'while ({p[3]}) {{\n{p[6]}\n}}'

def p_statements(p):
    '''statements : statement
        | statement statements'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + '\n' + p[2]

def p_statement(p):
    '''statement : assignment_statement
        | print_statement
        | while_statement'''
    p[0] = p[1]

def p_assignment_statement(p):
    '''assignment_statement : IDENTIFIER ASSIGN expression'''
    p[0] = f'{p[1]} = {p[3]}'

def p_print_statement(p):
    '''print_statement : PRINT LPAREN expression RPAREN'''
    p[0] = f'print({p[3]})'

def p_expression(p):
    '''
    expression : IDENTIFIER
               | NUMBER
               | BOOL_TRUE
               | BOOL_FALSE
               | expression PLUS expression
               | expression MINUS expression
               | expression TIMES expression
               | expression DIVIDE expression
               | LPAREN expression RPAREN
               | expression LOGICAL expression
               | expression LESS_THAN expression
    '''
    # Remaining code for handling different expressions

    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = f'{p[1]} {p[2]} {p[3]}'

def p_error(p):
    print("Syntax error at '%s'" % p.value)

parser = yacc.yacc()

while True:
    try:
        s = input('for > ')
    except EOFError:
        break
    if not s:
        continue
    result = parser.parse(s)
    if result is not None:
        print("Valid syntax")