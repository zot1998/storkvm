
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = "leftANDORleftLPARENRPARENleftPLUSMINUSleftTIMESDIVIDEOBJECT EQUAL1 NUMBER LPAREN RPAREN PLUS MINUS TIMES DIVIDE DOT AND OR COMMENT ELSE IFexpression : expression '+' expression\n                  | expression '-' expression\n                  | expression '*' expression\n                  | expression '/' expression\n                  | NUMBER "
    
_lr_action_items = {'+':([1,2,7,8,9,10,],[-5,4,4,4,4,4,]),'*':([1,2,7,8,9,10,],[-5,5,5,5,5,5,]),'-':([1,2,7,8,9,10,],[-5,3,3,3,3,3,]),'NUMBER':([0,3,4,5,6,],[1,1,1,1,1,]),'/':([1,2,7,8,9,10,],[-5,6,6,6,6,6,]),'$end':([1,2,7,8,9,10,],[-5,0,-2,-1,-3,-4,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,4,5,6,],[2,7,8,9,10,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression + expression','expression',3,'p_expression_binop','compile.py',76),
  ('expression -> expression - expression','expression',3,'p_expression_binop','compile.py',77),
  ('expression -> expression * expression','expression',3,'p_expression_binop','compile.py',78),
  ('expression -> expression / expression','expression',3,'p_expression_binop','compile.py',79),
  ('expression -> NUMBER','expression',1,'p_expression_binop','compile.py',80),
]
