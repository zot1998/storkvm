import os
import sys
import ply
from ply_rule import rule

curdir = os.path.dirname(os.path.abspath(__file__))
if curdir not in sys.path:
    sys.path.append(curdir)


context = '''
AA := 55 + 3
//a = x
//A = B(a, 5) + 20*2
'''

rule = rule(context)
rc,a,b,c = rule.lex()
if rc:
    rule.yacc()
else:
    print(rc,a,b,c)






