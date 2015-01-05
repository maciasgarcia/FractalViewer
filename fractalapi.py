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

        for n in range(1, self.maxiter + 1):
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
        for n in range(1, self.maxiter + 1):
            indic = (abs(z) <= 10)
            z[indic] = feval(func, z[indic], c[indic])
            iters[indic] = n

        return iters


class NewtonApi():
    def __init__(self):
        self.xmin = -2
        self.xmax = 2
        self.ymin = -2
        self.ymax = 2
        self.densidad = 500
        self.maxiter = 100
        self.epsilon = 0.05

    def newtonimage(self, polyn):
        xg, yg = meshgrid(linspace(self.xmin, self.xmax, self.densidad),
                          linspace(self.ymax, self.ymin, self.densidad))

        iters = zeros((self.densidad, self.densidad))
        z = xg + 1j*yg
        indic = (abs(z) >= 0)
        zold = copy(z)

        for n in range(self.maxiter):
            zold[indic] = newtoniter(polyn, z[indic])
            indic = (abs(z - zold) >= self.epsilon)
            z[indic] = zold[indic]
            iters[indic] = n

        return iters

    def newtonimage2(self, func):
        xg, yg = meshgrid(linspace(self.xmin, self.xmax, self.densidad),
                          linspace(self.ymax, self.ymin, self.densidad))

        iters = zeros((self.densidad, self.densidad))
        z = xg + 1j*yg
        indic = (abs(z) >= 0)
        zold = copy(z)

        for n in range(self.maxiter):
            zold[indic] = newtoniter2(func, z[indic])
            indic = (abs(z - zold) >= self.epsilon)
            z[indic] = zold[indic]
            iters[indic] = n

        return iters

if __name__ == '__main__':
    pass