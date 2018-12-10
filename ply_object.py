import os
import sys

class PlyException(Exception):
    def __init__(self, lineno, pos, msg):
        Exception.__init__(self, 'ply error')
        self._lineno = lineno
        self._pos = pos
        self._msg = msg

class object():
    _name = None
    _value = None
    _type  = None
    def __init__(self, name):
        self._name = str(name)

    def getname(self):
        return self._name
    def getvalue(self):
        return self._value

    def setname(self, name):
        self._name = name
    def setvalue(self, value):
        self._value = value

class ID(object):
    def __init__(self, name):
        object.__init__(self, name)
        self._name = name
        self._type = self.__class__.__name__


class NUMBER(object):
    def __init__(self, value):
        object.__init__(self, value)
        self._value = value
        self._type = self.__class__.__name__

    def __add__(self, o):
        self._value = self._value + o._value
        return NUMBER(self._value)

    def __sub__(self, o):
        self._value = self._value - o._value
        return NUMBER(self._value)

    def __mul__(self, o):
        self._value = self._value * o._value
        return NUMBER(self._value)

    def __div__(self, o):
        self._value = self._value / o._value
        return NUMBER(self._value)

class METHOD(object):
    _paras = []
    def __init__(self, name):
        object.__init__(self, name)
        self._name = name
        self._type = self.__class__.__name__

    def appendpara(self, o):
        self._paras.append(o)



class AST(object):
    _left = None
    _right = None
    _op = None

    def __init__(self, op, left, right):
        self._op = op
        self._left = left
        self._right = right

    def setleft(self, left):
        self._left = left

    def setright(self, right):
        self._right = right

    def show(self, ent = 0):
        spaces = ' ' * ent
        print(spaces + "OP :" + str(self._op))

        print(spaces + 'L:'),
        if isinstance(self._left, AST):
            print("AST")
            self._left.show(ent + 2)
        elif self._left:
            print(self._left.getname())

        print(spaces + 'R:'),
        if isinstance(self._right, AST):
            print("AST")
            self._right.show(ent + 2)
        elif self._right:
            print(self._right.getname())











