
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