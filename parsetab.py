
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\xa8>\x01uXw4\x8f\x91Wd\xe1\x1b\x18\xc7)'
    
_lr_action_items = {'RPAREN':([4,6,8,10,11,12,13,],[-6,9,-7,14,-9,-8,-5,]),'NUMBER':([4,6,8,13,],[-6,11,-7,-5,]),'EQUALS':([2,],[3,]),'COMMA':([10,11,12,],[13,-9,-8,]),'LPAREN':([5,],[8,]),'ID':([0,3,4,6,8,13,],[2,5,-6,12,-7,-5,]),'$end':([1,7,9,14,],[0,-1,-4,-3,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'assignment':([0,],[1,]),'method_start':([3,],[4,]),'method':([3,],[7,]),'para':([6,],[10,]),'method_append':([3,],[6,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> assignment","S'",1,None,None,None),
  ('assignment -> ID EQUALS method','assignment',3,'p_assignment_1','/root/share/storkvm/storkvm/ply_yacc.py',31),
  ('condition_action -> method COMMA ID','condition_action',3,'p_condition_action_1','/root/share/storkvm/storkvm/ply_yacc.py',37),
  ('method -> method_append para RPAREN','method',3,'p_expression_method','/root/share/storkvm/storkvm/ply_yacc.py',45),
  ('method -> method_append RPAREN','method',2,'p_expression_method','/root/share/storkvm/storkvm/ply_yacc.py',46),
  ('method_append -> method_append para COMMA','method_append',3,'p_expression_method','/root/share/storkvm/storkvm/ply_yacc.py',48),
  ('method_append -> method_start','method_append',1,'p_expression_method','/root/share/storkvm/storkvm/ply_yacc.py',49),
  ('method_start -> ID LPAREN','method_start',2,'p_expression_method','/root/share/storkvm/storkvm/ply_yacc.py',51),
  ('para -> ID','para',1,'p_expression_method','/root/share/storkvm/storkvm/ply_yacc.py',53),
  ('para -> NUMBER','para',1,'p_expression_method','/root/share/storkvm/storkvm/ply_yacc.py',54),
]
