#coding: utf8
from pylab import *

#Datos para dibujar
maxiter = 100
xmin = -2
xmax = 2
ymin = -1.5
ymax = 1.5
dens = 1000


def funcjulia(x, c):
    """Función de la cual vamos a representar su conjunto de Mandelbrot"""
    return x**2 + c

xg, yg = meshgrid(linspace(xmin, xmax, dens), linspace(ymin, ymax, dens))
iters = zeros((dens, dens))
# Este va a ser el c del conjunto de Julia que queremos calcular.
c = 0
#Creamos la matriz con todos los puntos que vamos a evaluar.
z = xg + 1j*yg

for n in xrange(maxiter):
    indices = (abs(z) <= 10) # Conjunto de índices que verifican |z| <= 10 (10 para mejor dibujado, 2 es suficiente)
    z[indices] = funcjulia(z[indices], c) # Aplicamos la función que hemos definido.
    iters[indices] = n

imshow(1 - log(iters), cmap = cm.Blues, extent = (xmin, xmax, ymin, ymax))
# cmap permite cambiar la paleta de colores. Paletas aquí: http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
show()

