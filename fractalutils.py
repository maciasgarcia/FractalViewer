# -*- coding: utf-8 -*-
from pylab import *


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def feval(mf0, *args):
    """ Funcion auxiliar que permite la evaluacion de funciones
    definidas por el usuario"""
    return eval(mf0)(*args)

def quadratic(self, x, c):
    """Quadratic function to represent its julia associated fractal."""
    return x**2 + c

def cubic(self, x, c):
    return x**3 + c

if __name__ == '__main__':
    pass