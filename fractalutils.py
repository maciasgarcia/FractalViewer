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


def numbercheck(numberlist):
        for numb in numberlist:
            if not is_number(numb):
                return False
        return True


def inmandelbrot(func, c, iterat):
    i = 0
    newc = c
    while i <= iterat:
        if abs(newc) <= 2:
            newc = feval(func, newc, c)
            i += 1
        else:
            return False
    return True


def newtoniter(polyn, dpolyn, z):
    return z - feval(polyn, z)/ feval(dpolyn, z)


def quadratic(z, c):
    """Quadratic function to represent its julia associated fractal."""
    return z**2 + c


def cubic(z, c):
    return z**3 + c


def cubomenos1(z):
    return z**3 - 1


def dcubomenos1(z):
    return 3*z**2


if __name__ == '__main__':
    pass