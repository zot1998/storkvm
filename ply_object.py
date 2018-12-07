import os
import sys

class object():
    def __init__(self):
        pass

class PlyException(Exception):
    def __init__(self, lineno, pos, msg):
        Exception.__init__(self, 'ply error')
        self._lineno = lineno
        self._pos = pos
        self._msg = msg






