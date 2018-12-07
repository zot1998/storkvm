import os
import sys
from ply_object import object
from ply_object import PlyException

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


# Tokens
t_EQUAL1 = r'\:\='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'/'
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
    #print("Illegal character '%s'" % t.value[0])
    #t.lexer.skip(1)
    raise PlyException(t.lineno, t.lexpos, t.value)


literals = ['=', '+', '-', '*', '/', '(', ')',',']


precedence = (
    ('left', 'AND', 'OR'),    
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
    )

def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression '-' expression
                  | expression '*' expression
                  | expression '/' expression
                  | NUMBER '''
    #print('p type={}'.format(type(p)))
    #print('p[0]={}'.format(type(p[0])))
    #print('p[1]={}'.format(type(p[1])))

    if (len(p) > 2):
    	if p[2] == '+':
    		p[0] = p[1] + p[3]
    	elif p[2] == '-': 
    		p[0] = p[1] - p[3]
    	elif p[2] == '*': 
    		p[0] = p[1] * p[3]
    	elif p[2] == '/': 
    		p[0] = p[1] / p[3]
    else:
    	p[0] = p[1]






def p_error(p):
    if p:
        print(" *** Syntax error at (line:{},pos:{}, error:{})".format(p.lineno, p.lexpos, p.value))
    else:
        print(" *** Syntax error at EOF")


class rule(object):
    def __init__(self, context):
        object.__init__(self)
        self._lexer = lex.lex()
        self._yacer = yacc.yacc()
        self._context = context

    def reset(self):
        pass

    def lex(self):
        try:
            self._lexer.input(self._context)
            while True:
                tok = self._lexer.token()
                if not tok: 
                    break
        except PlyException as e:
            return False, e._lineno, e._pos, e._msg
        return True, None, None, None

    def yacc(self):
        #try:
        if True:
            result =  self._yacer.parse(self._context)
            print(result)
        #except:
        #    print("#####")

    def run(self):
        pass

        






