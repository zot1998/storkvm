import os
import sys
import ply

import ply.lex as lex
import ply.yacc as yacc


tokens_reserved ={
	'IF':'IF',
	'ELSE':'ELSE',
}

tokens = [
    'OBJECT',
    'EQUAL1',
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
    'COMMENT',
] + tokens_reserved.values()

literals = ['=', '+', '-', '*', '/', '(', ')',',']

# Tokens
t_EQUAL1 = r'\:\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS   = r'\+'
t_MINUS  = r'\-'
t_TIMES  = r'\*'
t_DIVIDE = r'\/'
t_DOT    = r'\.'
t_AND    = r'(?<=[\t ])AND(?=[\t ])'
t_OR     = r'(?<=[\t ])OR(?=[\t ])'

def t_OBJECT(t):
    r'[A-Z][A-Z0-9]*'
    t.type = tokens_reserved.get(t.value, 'OBJECT')
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore_COMMENT = "//.*"
t_ignore = '[\t ]'


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

def p_expression_binop(p):
    '''expression : expression '+' expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | NUMBER '''
    print('p type={}'.format(type(p)))
    print('p[0]={}'.format(type(p[0])))
    print('p[1]={}'.format(type(p[1])))

    if p[2] == '+'  : 
    	p[0] = p[1] + p[3]
    elif p[2] == '-': 
    	p[0] = p[1] - p[3]
    elif p[2] == '*': 
    	p[0] = p[1] * p[3]
    elif p[2] == '/': 
    	p[0] = p[1] / p[3]

    print('p type={}'.format(type(p)))
    print('p[0]={}'.format(type(p[0])))
    print('p[1]={}'.format(type(p[1])))
    print('p[2]={}'.format(type(p[2])))
    print('p[3]={}'.format(type(p[3])))



def p_error(p):
    if p:
        print("Syntax error at '%s'" % p.value)
    else:
        print("Syntax error at EOF")

lex.lex()
yacc.yacc()

context = '''
5*3
//a = x
//A = B(a, 5) + 20*2
'''
yacc.parse('5* 3')

