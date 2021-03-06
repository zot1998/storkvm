
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression
                  | LPAREN expression RPAREN
                  | NUMBER'''
    if (len(p) > 2):
    	if p[2] == '+':
    		p[0] = p[1] + p[3]
    	elif p[2] == '-':
    	    p[0] = p[1] - p[3]
    	elif p[2] == '*':
    		p[0] = p[1] * p[3]
    	elif p[2] == '/':
    		p[0] = p[1] / p[3]
        elif p[1] == '(':
            p[0] = p[2]
    else:
    	p[0] = p[1]



#def p_assignment_1(p):
#    'assignment : ID EQUALS method'
#    p[0] = AST(':=', p[1], p[3])


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