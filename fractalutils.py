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


def turnintoarray(str):
    nstr = str[1:-1]
    array = nstr.split(',')
    return [float(s) for s in array if is_number(s)]


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


def newtoniter(polyn, z):
    num = polyn(z)
    dnum = poly1d.deriv(polyn)
    den = dnum(z)
    return z - num/den


def quadratic(z, c):
    """Quadratic function to represent its julia associated fractal."""
    return z**2 + c


def cubic(z, c):
    return z**3 + c


if __name__ == '__main__':
    pass