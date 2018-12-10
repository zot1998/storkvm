import os
import sys
import ply
from ply_excute import ply_excute

curdir = os.path.dirname(os.path.abspath(__file__))
if curdir not in sys.path:
    sys.path.append(curdir)


#context = ''' A := MA(CLOSE,5);B := MA(CLOSE,5);CROSS(A, B), BP;'''
context = '''A:=MA(C,5);CROSS(A, B), BD'''

cc = ply_excute(context)
cc.run()







