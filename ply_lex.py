import os
import sys

curdir = os.path.dirname(os.path.abspath(__file__))
if curdir not in sys.path:
    sys.path.append(curdir)

from ply_object import object, ID, NUMBER, METHOD, AST
from ply_object import PlyException

import ply.lex as lex



tokens_reserved ={
	'IF':'IF',
	'ELSE':'ELSE',
}

tokens = [
    'ID',
#    'METHOD',
    'EQUALS',
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
    'COMMA',
    'COMMENT',
    'SEMICOLON',

    'LESS',
] + tokens_reserved.values()


# Tokens
t_EQUALS = r':='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_PLUS   = r'\+'
t_MINUS  = r'-'
t_TIMES  = r'\*'
t_DIVIDE = r'\/'
t_DOT    = r'\.'
t_AND    = r'(?<=[\t ])AND(?=[\t ])'
t_OR     = r'(?<=[\t ])OR(?=[\t ])'
t_COMMA  = r','

t_LESS = r'<'

def t_ID(t):
    r'[A-Z][A-Z0-9]*'
    t.type = tokens_reserved.get(t.value, 'ID')
    t.value = ID(t.value)

    return t

#def t_METHOD(t):
#    r'[A-Z][A-Z0-9]*(?=\()'
#    t.value = METHOD(t.value)
#    return t

def t_NUMBER(t):
    r'\d+(\.\d+)*'
    t.value = NUMBER(float(t.value))
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


