# -*- coding: utf-8 -*-
#from pylab import matplotlib, ion
import wx
from pylab import *
from matplotlib.pyplot import *

from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg

from matplotlib.figure import Figure


def feval(mf0, *args):
    """ Funcion auxiliar que permite la evaluacion de funciones
    definidas por el usuario"""
    return eval(mf0)(*args)


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def julia(x, c):
    """Funcion de la cual vamos a representar su conjunto de Julia"""
    return x**2 + c


class App(wx.App):
    def OnInit(self):
        self.frame = wx.Frame(None, -1, title=u'Conjunto de Julia', size=(850, 550))
        self.crear_gui_masfigura(self.frame)
        self.frame.Show()        
        self.ax = self.fig.add_subplot(111)
        self.ejecutar(self)
        return True

    def crear_gui_masfigura(self, parent):
        self.fig = Figure(figsize=(5, 5), dpi=100, facecolor=(0.3, 0.25, 0.3))
        sizer = wx.BoxSizer(wx.HORIZONTAL)
        
        paneldraw = wx.Panel(parent, -1)
        sizer.Add(paneldraw, 1, wx.LEFT | wx.EXPAND)
        
        sizerPlotToolbar = wx.BoxSizer(wx.VERTICAL)
        self.canvas = FigureCanvas(paneldraw, -1, self.fig)
        self.canvas.draw()
        sizerPlotToolbar.Add(self.canvas, 1, wx.TOP | wx.LEFT | wx.EXPAND)
        
        self.toolbar = NavigationToolbar2WxAgg(self.canvas)
        self.toolbar.Realize()
        sizerPlotToolbar.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
        paneldraw.SetSizer(sizerPlotToolbar)

        # Panel y sizers para parametros y botones
        panelbut = wx.Panel(parent, -1)
        sizerbut = wx.BoxSizer(wx.VERTICAL)
        panelbut.SetBackgroundColour(wx.Colour(255, 255, 255))

        sizer0 = wx.BoxSizer(wx.HORIZONTAL)
        label0 = wx.StaticText(panelbut, -1, u'Parámetros')
        label0.Wrap(-1)
        label0.SetFont( wx.Font( 11, 74, 93, 92, True, "Tahoma" ))
        sizer0.Add(label0, -1, wx.ALL | wx.CENTER)
        sizerbut.Add(sizer0, -1, wx.TOP | wx.CENTER)

        # Espacio en blanco
        sizerws = wx.BoxSizer(wx.HORIZONTAL)
        whitespace = wx.StaticText(panelbut, -1, '')
        sizerws.Add(whitespace, -1, wx.ALL)
        sizerbut.Add(sizerws, -1, wx.TOP | wx.CENTER)

        # Parametros
        sizer1 = wx.BoxSizer(wx.HORIZONTAL)
        label1 = wx.StaticText(panelbut, -1, u'  Máx iteraciones:')
        sizer1.Add(label1, -1, wx.ALL)

        self.caja_maxiter = wx.TextCtrl(panelbut, -1, value='100',size=(-1, -1))
        sizer1.Add(self.caja_maxiter, -1, wx.ALL)
        sizerbut.Add(sizer1, -1, wx.TOP | wx.CENTER)
             
        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        label2 = wx.StaticText(panelbut, -1, '  Xmin:')
        sizer2.Add(label2, -1, wx.ALL)

        self.caja_Xmin = wx.TextCtrl(panelbut, -1, value='-2', size=(-1, -1))
        sizer2.Add(self.caja_Xmin, -1, wx.ALL)
        sizerbut.Add(sizer2, -1, wx.TOP | wx.CENTER)
        
        sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        label3 = wx.StaticText(panelbut, -1, '  Xmax:')
        sizer3.Add(label3, -1, wx.ALL)

        self.caja_Xmax = wx.TextCtrl(panelbut, -1, value='2', size=(-1, -1))
        sizer3.Add(self.caja_Xmax, -1, wx.ALL)
        sizerbut.Add(sizer3, -1, wx.TOP | wx.CENTER)

        sizer4 = wx.BoxSizer(wx.HORIZONTAL)
        label4 = wx.StaticText(panelbut,-1,'  Ymin:')
        sizer4.Add(label4, -1, wx.ALL)

        self.caja_Ymin = wx.TextCtrl(panelbut, -1, value='-1.5', size=(-1, -1))
        sizer4.Add(self.caja_Ymin, -1, wx.ALL)
        sizerbut.Add(sizer4, -1, wx.TOP | wx.CENTER)

        sizer5 = wx.BoxSizer(wx.HORIZONTAL)
        label5 = wx.StaticText(panelbut, -1, '  Ymax:')
        sizer5.Add(label5, -1, wx.ALL)

        self.caja_Ymax = wx.TextCtrl(panelbut, -1, value='1.5', size=(-1, -1))
        sizer5.Add(self.caja_Ymax, -1, wx.ALL)
        sizerbut.Add(sizer5, -1, wx.TOP | wx.CENTER)

        sizer6 = wx.BoxSizer(wx.HORIZONTAL)
        label6 = wx.StaticText(panelbut, -1, '  Densidad:')
        sizer6.Add(label6, -1, wx.ALL)

        self.caja_Densidad = wx.TextCtrl(panelbut, -1, value='500', size=(-1, -1))
        sizer6.Add(self.caja_Densidad, -1, wx.ALL)
        sizerbut.Add(sizer6, -1, wx.TOP | wx.CENTER)
        
        sizer7 = wx.BoxSizer(wx.HORIZONTAL)
        label7 = wx.StaticText(panelbut, -1, '  Funcion:')
        sizer7.Add(label7, -1, wx.ALL)

        self.caja_fun = wx.TextCtrl(panelbut, -1, value='julia', size=(-1, -1))
        sizer7.Add(self.caja_fun, -1, wx.ALL)
        sizerbut.Add(sizer7, -1, wx.TOP | wx.CENTER)

        sizer8 = wx.BoxSizer(wx.HORIZONTAL)
        label8 = wx.StaticText(panelbut, -1, '  Re(c):')
        sizer8.Add(label8, -1, wx.ALL)

        self.caja_Rec = wx.TextCtrl(panelbut, -1, value='-0.4',size=(-1, -1))
        sizer8.Add(self.caja_Rec, -1, wx.ALL)
        sizerbut.Add(sizer8, -1, wx.TOP | wx.CENTER)

        sizer9 = wx.BoxSizer(wx.HORIZONTAL)
        label9 = wx.StaticText(panelbut, -1, '  Im(c):')
        sizer9.Add(label9, -1, wx.ALL)

        self.caja_Imc = wx.TextCtrl(panelbut, -1, value='0.6', size=(-1, -1))
        sizer9.Add(self.caja_Imc, -1, wx.ALL)
        sizerbut.Add(sizer9, -1, wx.TOP | wx.CENTER)

        # Espacio en blanco
        sizerws = wx.BoxSizer(wx.HORIZONTAL)
        whitespace = wx.StaticText(panelbut, -1, '')
        sizerws.Add(whitespace, -1, wx.ALL)
        sizerbut.Add(sizerws, -1, wx.TOP | wx.CENTER)

        sizer10 = wx.BoxSizer(wx.HORIZONTAL)
        label10 = wx.StaticText(panelbut, -1, '  Paleta de colores:')
        sizer10.Add(label10, -1, wx.ALL)

        self.listacolores = ['Azul/Amarillo/Rojo', 'Blanco y negro', 'Azules', 'Verde/Amarillo/Rojo', 'Hot',
                             'Rosa', 'Naranjas']
        self.despcolores = wx.ComboBox(panelbut, -1, choices=self.listacolores, style=wx.CB_READONLY,
                                       value=self.listacolores[0])
        sizer10.Add(self.despcolores, -1, wx.ALL)
        sizerbut.Add(sizer10, -1, wx.TOP | wx.CENTER)

        sizer11 = wx.BoxSizer(wx.HORIZONTAL)
        self.invertpaleta = wx.CheckBox(panelbut, -1, 'Invertir paleta de colores')
        sizer11.Add(self.invertpaleta, -1, wx.ALL)
        sizerbut.Add(sizer11, -1, wx.TOP | wx.CENTER)

        sizer12 = wx.BoxSizer(wx.HORIZONTAL)
        label12 = wx.StaticText(panelbut, -1, u'Para ampliar el conjunto hacer click derecho.')
        sizer12.Add(label12, -1, wx.ALL | wx.CENTER)
        sizerbut.Add(sizer12, -1, wx.TOP | wx.CENTER)

        sizer13 = wx.BoxSizer(wx.HORIZONTAL)
        label13 = wx.StaticText(panelbut, -1, u'  Magnificación:')
        sizer13.Add(label13, -1, wx.ALL)

        self.caja_zoom = wx.TextCtrl(panelbut, -1, value='2', size=(-1,-1))
        sizer13.Add(self.caja_zoom, -1, wx.ALL)
        sizerbut.Add(sizer13, -1, wx.TOP | wx.CENTER)

        # Espacio en blanco
        sizerws = wx.BoxSizer(wx.HORIZONTAL)
        whitespace = wx.StaticText(panelbut, -1, '')
        sizerws.Add(whitespace, -1, wx.ALL)
        sizerbut.Add(sizerws, -1, wx.TOP | wx.CENTER)

        # Botones
        botejecutar = wx.Button(panelbut, label='Ejecutar')
        sizerbut.Add(botejecutar, -1, wx.TOP | wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.ejecutar, botejecutar)

        botrestaurar = wx.Button(panelbut, label='Restaurar')
        sizerbut.Add(botrestaurar, -1, wx.TOP | wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.restaurar, botrestaurar)

        botabout = wx.Button(panelbut, label='Acerca de')
        sizerbut.Add(botabout, -1, wx.TOP | wx.EXPAND)
        self.Bind(wx.EVT_BUTTON, self.about, botabout)

        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        
        panelbut.SetSizer(sizerbut)
        
        sizer.Add(panelbut, 0, wx.TOP)
        parent.SetSizer(sizer)

    def onclick(self, event):
        bt, xc, yc = (event.button, event.xdata, event.ydata)
        zoom = float(self.caja_zoom.GetValue())
        if is_number(zoom) and float(zoom)!= 0:
            xdist = (float(self.caja_Xmax.GetValue()) - float(self.caja_Xmin.GetValue()))/(2*zoom)
            ydist = (float(self.caja_Ymax.GetValue()) - float(self.caja_Ymin.GetValue()))/(2*zoom)
        else:
            dlg = wx.MessageDialog(self.frame, u"Error en los parámetros", "Error!", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        if bt == 3:
            self.caja_Xmin.SetValue(str(xc - xdist))
            self.caja_Xmax.SetValue(str(xc + xdist))
            self.caja_Ymin.SetValue(str(yc - ydist))
            self.caja_Ymax.SetValue(str(yc + ydist))
            self.ejecutar(self)



    def ejecutar(self, event):
        er = 0
        if is_number(self.caja_maxiter.GetValue()):
            self.maxiter = int(self.caja_maxiter.GetValue())
        else:
            er = 1
            self.maxiter = 0
        if is_number(self.caja_Xmin.GetValue()):
            self.Xmin = float(self.caja_Xmin.GetValue())
        else:
            er = 1
            self.Xmin = 0.0
        if is_number(self.caja_Xmax.GetValue()):
            self.Xmax = float(self.caja_Xmax.GetValue())
        else:
            er = 1
            self.Xmax = 0.0
        if is_number(self.caja_Ymin.GetValue()):
            self.Ymin = float(self.caja_Ymin.GetValue())
        else:
            er = 1
            self.Ymin = 0.0
        if is_number(self.caja_Ymax.GetValue()):
            self.Ymax = float(self.caja_Ymax.GetValue())
        else:
            er = 1
            self.Ymax = 0.0
        if is_number(self.caja_Densidad.GetValue()):
            self.Densidad = float(self.caja_Densidad.GetValue())
        else:
            er = 1
            self.Densidad = 0
        if is_number(self.caja_Rec.GetValue()) and is_number(self.caja_Imc.GetValue()):
            self.c = complex(float(self.caja_Rec.GetValue()), float(self.caja_Imc.GetValue()))
        else:
            er = 1
            self.c = 0

        self.fun = self.caja_fun.GetValue()

        if ((er == 1) | (self.Xmin > self.Xmax) | (self.Ymin > self.Ymax) |  (self.maxiter <= 0) | (self.fun == '')
                | (self.c == '') | (self.Densidad == '')):
            dlg = wx.MessageDialog(self.frame, u"Error en los parámetros", "Error!", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
            er = 1
        if (er == 0):
            xg, yg = meshgrid(linspace(self.Xmin, self.Xmax,self.Densidad),
                              linspace(self.Ymax, self.Ymin, self.Densidad))
                    # Meshgrid desde el maximo al minimo en Y para solucionar problema de margenes incorrectos.
            iters = zeros((self.Densidad, self.Densidad))
            z = xg + 1j*yg # Matriz cuadrada de dens x dens con los distintos valores de x que vamos a evaluar.

            for n in xrange(self.maxiter):
                indices = (abs(z) <= 10) # Conjunto de indices tal que |z| <= 10 (10 para mejor dibujado, 2 es sufic)
                z[indices] = feval(self.fun, z[indices], self.c) # Aplicamos la funcion que hemos definido
                iters[indices] = n
            self.ax.cla()

            self.paleta = self.despcolores.GetValue()
            self.k = 1 - self.invertpaleta.IsChecked()

            if self.paleta == self.listacolores[0]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.RdYlBu,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.listacolores[1]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.binary,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.listacolores[2]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.Blues,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.listacolores[3]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.RdYlGn,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.listacolores[4]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.hot,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.listacolores[5]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.PuRd,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.listacolores[6]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.YlOrBr,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))

            # cmap permite cambiar la paleta de colores. http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
            # Para anadir un color nuevo, escribirlo en self.listacolores y colocar otro elif con su corresp. codigo
            self.canvas.draw()

    def restaurar(self, event):
        self.caja_maxiter.SetValue('100')
        self.caja_Xmin.SetValue('-2')
        self.caja_Xmax.SetValue('2')
        self.caja_Ymin.SetValue('-1.5')
        self.caja_Ymax.SetValue('1.5')
        self.caja_Densidad.SetValue('500')
        self.caja_Rec.SetValue('-0.4')
        self.caja_Imc.SetValue('0.6')
        self.invertpaleta.SetValue(False)
        self.despcolores.SetValue(self.listacolores[0])
        self.canvas.draw()
        self.caja_maxiter.SetFocus()




    def about(self, event):
        descripcion = u"""Este programa permite la visualización de los distintos conjuntos de Julia asociados a un
número complejo c, pudiendo además definirse distintas funciones para visualizar J(f) y usarse varias paletas de colores
y distintos ajustes."""
        inform = wx.AboutDialogInfo()
        inform.SetIcon(wx.Icon('iconojul.png', wx.BITMAP_TYPE_PNG))
        inform.SetName('Conjuntos de Julia')
        inform.SetDescription(descripcion)
        inform.SetCopyright(u'Juan Antonio Macías - Marina Molina - Ana López')
        inform.SetWebSite('www.github.com/JuanMtg/JuliaSets')

        wx.AboutBox(inform)


def main():
    app = App(0)
    app.MainLoop()
if __name__ == '__main__':
    main()