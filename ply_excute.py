# -*- coding: UTF-8 -*-
import os
import sys
import ply.lex as lex
import ply.yacc as yacc

curdir = os.path.dirname(os.path.abspath(__file__))
if curdir not in sys.path:
    sys.path.append(curdir)

import ply_lex
import ply_yacc
from ply_object import object, NUMBER, METHOD, object
from ply_object import PlyException





#Demo版本: 简易处理，不构建ast，逐条分析/解释/运行；
# 不支持 IF xxx ; THEN yyy; 指令
# 不支持()嵌套,譬如 AA(B(),11)
class ply_excute():
    def __init__(self, context):
        self._var = {} # 只支持全局变量
        self._symbols = {}
        self._lexer = lex.lex(module=ply_lex)
        self._yacer = yacc.yacc(module=ply_yacc)

        self._context = context.split(';')

        self._ast_table = {
            ':=': self.ast_assign,
        }

    def ast_assign(self, id, value):
        self._symbols[id.getname()] = value



    def lex(self, context):
        try:
            self._lexer.input(context)
            while True:
                tok = self._lexer.token()
                if not tok:
                    break
                #print tok
        except PlyException as e:
            return False, e._lineno, e._pos, e._msg
        return True, None, None, None



    def check(self):
        pass

    def excute(self, ast):

        pass

    def run(self):
        for text in self._context:
            if not text:
                continue
            print("#####:{}".format(text))

            rc,_,_,msg = self.lex(text)
            if not rc:
                print('{} -> lex error:{}'.format(text, msg))

            ast = self._yacer.parse(text)
            if ast:
                pass
                ast.show()







        






