import os
import sys

curdir = os.path.dirname(os.path.abspath(__file__))
if curdir not in sys.path:
    sys.path.append(curdir)

from ply_object import object, ID, NUMBER, METHOD, AST
from ply_object import PlyException

import ply.lex as lex
import ply.yacc as yacc
import ply_lex

tokens = ply_lex.tokens


literals = ['=', '+', '-', '*', '/', '(', ')',',']


precedence = (
    #('nonassoc', 'LESSTHAN', 'GREATERTHAN'),
    #('left', 'EQUALS'),
    ('left', 'AND', 'OR'),    
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE'),
    ('left', 'LPAREN', 'RPAREN'),
    )

def p_assignment_1(p):
    'assignment : ID EQUALS method'
    p[0] = AST(':=', p[1], p[3])


def p_condition_action_1(p):
    '''
    condition_action : method COMMA ID
    '''
    p[0] = AST('condition_action', p[1], p[3])



def p_expression_method(p):
    '''
    method  :   method_append para RPAREN
            |   method_append RPAREN

    method_append   : method_append para COMMA
                    | method_start

    method_start    : ID LPAREN

    para    : ID
            | NUMBER
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        if p[2] == '(':
            ast = AST('METHOD', p[1], None)
            p[0] = {
                'root':ast,
                'current':ast,
            }
        elif p[2] == ')':
            p[0] = p[1]['root']
    elif len(p) == 4:
        if p[3] == ',':
            ast = AST(',', p[2], None)

            p[1]['current'].setright(ast)
            p[1]['current'] = ast
            p[0] = p[1]
        elif p[3] == ')':
            p[1]['current'].setright(p[2])
            p[0] = p[1]['root']

def p_error(p):
    if p:
        print(" *** Syntax error at [line {} pos {} error '{}']".format(p.lineno, p.lexpos, p.value))
    else:
        print(" *** Syntax error at EOF")



        






