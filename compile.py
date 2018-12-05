import os
import sys
import ply

import ply.lex as lex
import ply.yacc as yacc



tokens = (
    'OBJECT',
    'EQUAL',
    'NUMBER',
    'LPAREN',
    'RPAREN',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'DOT',
    'AND',
    'OR',
)

literals = ['=', '+', '-', '*', '/', '(', ')',',']

# Tokens
t_OBJECT = r'[A-Z][A-Z0-9]*'
t_EQUAL  = r'\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_TIMES = r'\*'
t_DIVIDE = r'\/'
t_DOT    = r'\.'
t_AND    = r' AND '
t_OR     = r' OR '

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = "//.*"


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


precedence = (
    ('left', 'AND', 'OR'),
    ('left', 'LPAREN', 'RPAREN'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    )


names = { }

def p_statement_assign(p):
    'statement : NAME "=" expression'
    names[p[1]] = p[3]

def p_statement_expr(p):
    'statement : expression'
    print("----")
    print(p[1])

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression'''
    if p[2] == '+'  : p[0] = p[1] + p[3]
    elif p[2] == '-': p[0] = p[1] - p[3]
    elif p[2] == '*': p[0] = p[1] * p[3]
    elif p[2] == '/': p[0] = p[1] / p[3]


def p_expression_number(p):
    "expression : NUMBER"
    p[0] = p[1]

def p_expression_name(p):
    "expression : NAME"
    try:
        p[0] = names[p[1]]
    except LookupError:
        print("Undefined name '%s'" % p[1])
        p[0] = 0

def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

lex.lex()
yacc.yacc()

context = '''
a = x
A = B(a, 5) + 20
'''
yacc.parse(context)

