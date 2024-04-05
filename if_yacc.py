import ply.yacc as yacc
from if_lex import tokens

def p_if(p):
    '''IF : if parameters LBRACE statements RBRACE'''
    p[0] = 'if' + p[2] + '{' + p[4] + '}'
    pass 
def p_parameters(p):
    '''parameters : parameter
                  | parameter LOGICAL parameters'''
    if len(p) == 2:
        p[0] = p[1] 
    else:
        p[0] = p[1] + p[2] + p[3]
def p_parameter(p):
    '''parameter : identifier 
                 | NUMBER'''
    p[0] = p[1]
def p_statements(p):
    '''statements : statement
                  | statement statements'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]
def p_statement(p):
    '''statement : assignment_statement
                 | print_statement'''
    p[0] = p[1] 
def p_assignment_statement(p):
    '''assignment_statement : let identifier ASSIGN NUMBER'''
    p[0] = 'let' + p[2] + '=' + p[4] 
def p_print_statement(p):
    '''print_statement : print LPAREN expressions RPAREN'''
    p[0] = 'print(' + p[3] + ')'
def p_expressions(p):
    '''expressions : expression
                   | expression expressions'''
    if len(p) == 2:
        p[0] = p[1]
    else: p[0] = p[1] + p[2]
def p_expression(p):
    '''expression : identifier
                  | NUMBER
                  | expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | dquote sentences dquote'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 4:
        if p[1] == '"':
            p[0] = '"' + p[2] + '"'
        else:
            p[0] = p[1] + p[2] + p[3]
def p_sentences(p):
    '''sentences : sentence
                 | sentence sentences'''
    if len(p)==2:
        p[0] = p[1]
    else:
        p[0] = p[1] + p[2]
def p_sentence(p):
    '''sentence :  identifier
                  | NUMBER
                  | sentence PLUS
                  | sentence MINUS
                  | sentence PLUS sentence
                  | sentence MINUS sentence
                  | sentence TIMES sentence
                  | sentence DIVIDE sentence'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1] + p[2] + p[3]
def p_error(p):
    print("Syntax error at '%s'" % p.value)

parser = yacc.yacc()
while True:
    try:
        s = input('calc > ')
    except EOFError:
        break
    if not s: continue
    result = parser.parse(s)
    if result is None:
        print("Error")
    else:
        print("Valid statement")