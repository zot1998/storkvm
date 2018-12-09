import os
import sys
import ply
from ply_excute import ply_excute

curdir = os.path.dirname(os.path.abspath(__file__))
if curdir not in sys.path:
    sys.path.append(curdir)


context = ''' A := CALL(PARA0,PARA1, 5,DD)'''

cc = ply_excute(context)
cc.run()







