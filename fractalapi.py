# -*- coding: utf-8 -*-
from pylab import *
from fractalutils import *


class WxPythonUtil():
    def __init__(self):
        pass


class JuliaApi():
    def __init__(self):
        self.xmin = -2
        self.xmax = 2
        self.ymin = -1.5
        self.ymax = 1.5
        self.densidad = 500
        self.maxiter = 100

    def juliaimage(self, func, c):
        xg, yg = meshgrid(linspace(self.xmin, self.xmax, self.densidad),
                          linspace(self.ymax, self.ymin, self.densidad))
        iters = zeros((self.densidad, self.densidad))
        z = xg + 1j*yg

        for n in xrange(self.maxiter):
            indic = (abs(z) <= 10)
            z[indic] = feval(func, z[indic], c)
            iters[indic] = n

        return iters


class MandelbrotApi():
    def __init__(self):
        self.xmin = -2.5
        self.xmax = 1.5
        self.ymin = -1.5
        self.ymax = 1.5
        self.densidad = 500
        self.maxiter = 100

    def mandimage(self, func):
        xg, yg = meshgrid(linspace(self.xmin, self.xmax, self.densidad),
                          linspace(self.ymax, self.ymin, self.densidad))
        iters = zeros((self.densidad, self.densidad))
        c = xg + 1j*yg

        z = zeros_like(c)
        for n in xrange(self.maxiter):
            indic = (abs(z) <= 10)
            z[indic] = feval(func, z[indic], c[indic])
            iters[indic] = n

        return iters

if __name__ == '__main__':
    pass