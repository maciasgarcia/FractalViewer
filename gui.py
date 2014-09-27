# -*- coding: utf-8 -*-
import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg
import fractalapi as fapi
from fractalutils import *


class FractalApp(wx.App):
    japi = fapi.JuliaApi()

    def OnInit(self):
        self.frame = wx.Frame(None, -1, title=u'Conjunto de Julia', size=(850, 550))
        self.initgui(self.frame)
        self.frame.Show()
        self.ax = self.fig.add_subplot(111)
        self.execute(self)
        return True

    def initgui(self, parent):
        self.fig = Figure(figsize=(5, 5), dpi=100, facecolor=(0.3, 0.25, 0.3))

        #Panels
        paneldraw = wx.Panel(parent, -1)
        panelbut = wx.Panel(parent, -1)
        panelbut.SetBackgroundColour(wx.Colour(255, 255, 255))

        #Sizers
        mainsizer = wx.BoxSizer(wx.HORIZONTAL)
        mainsizer.Add(paneldraw, 1, wx.LEFT | wx.EXPAND)

        sizerPlotToolbar = wx.BoxSizer(wx.VERTICAL)
        self.canvas = FigureCanvas(paneldraw, -1, self.fig)
        self.canvas.draw()
        sizerPlotToolbar.Add(self.canvas, 1, wx.TOP | wx.LEFT | wx.EXPAND)

        self.toolbar = NavigationToolbar2WxAgg(self.canvas)
        self.toolbar.Realize()
        sizerPlotToolbar.Add(self.toolbar, 0, wx.LEFT | wx.EXPAND)
        self.toolbar.update()
        paneldraw.SetSizer(sizerPlotToolbar)

        #Labels
        labelhead = wx.StaticText(panelbut, -1, u'Parámetros')
        labelhead.Wrap(-1)
        labelhead.SetFont(wx.Font(11, 74, 93, 92, True, "Tahoma"))

        whitespace = wx.StaticText(panelbut, -1, '')

        labelmiter = wx.StaticText(panelbut, -1, u'  Máx iteraciones:')
        labelmxmin = wx.StaticText(panelbut, -1, u'  X Mínimo:')
        labelmxmax = wx.StaticText(panelbut, -1, u'  X Máximo:')
        labelmymin = wx.StaticText(panelbut, -1, u'  Y Mínimo:')
        labelmymax = wx.StaticText(panelbut, -1, u'  Y Máximo:')
        labeldens = wx.StaticText(panelbut, -1, u'  Densidad:')
        labelfunc = wx.StaticText(panelbut, -1, u'  Función:')
        labelrec = wx.StaticText(panelbut, -1, u'   Re(c):')
        labelimc = wx.StaticText(panelbut, -1, u'   Im(c):')
        labelcolp = wx.StaticText(panelbut, -1, u'  Paleta de colores:')
        labelextx = wx.StaticText(panelbut, -1, u'Para ampliar el conjunto hacer click derecho.')
        labelmagn = wx.StaticText(panelbut, -1, u'  Magnificación:')

        #TextCtrls / Comboboxes / Checkboxes
        self.boxmiter =  wx.TextCtrl(panelbut, -1, value=str(self.japi.maxiter),size=(-1, -1))
        self.boxxmin = wx.TextCtrl(panelbut, -1, value=str(self.japi.xmin), size=(-1, -1))
        self.boxxmax = wx.TextCtrl(panelbut, -1, value=str(self.japi.xmax), size=(-1, -1))
        self.boxymin = wx.TextCtrl(panelbut, -1, value=str(self.japi.ymin), size=(-1, -1))
        self.boxymax = wx.TextCtrl(panelbut, -1, value=str(self.japi.ymax), size=(-1, -1))
        self.boxdens = wx.TextCtrl(panelbut, -1, value=str(self.japi.densidad), size=(-1, -1))
        self.boxfunc = wx.TextCtrl(panelbut, -1, value='quadratic', size=(-1, -1))
        self.boxrec = wx.TextCtrl(panelbut, -1, value='-0.4', size=(-1, -1))
        self.boximc = wx.TextCtrl(panelbut, -1, value='0.6', size=(-1, -1))
        self.colourlist = ['Azul/Amarillo/Rojo', 'Blanco y negro', 'Azules', 'Verde/Amarillo/Rojo',
                           'Hot', 'Rosa', 'Naranjas']
        self.combcolp = wx.ComboBox(panelbut, -1, choices=self.colourlist, style=wx.CB_READONLY,
                                    value=self.colourlist[0])
        self.invcolp = wx.CheckBox(panelbut, -1, 'Invertir paleta de colores')
        self.boxmagn = wx.TextCtrl(panelbut, -1, value='2', size=(-1,-1))
        #Buttons
        butexec = wx.Button(panelbut, label='Ejecutar')
        butrest = wx.Button(panelbut, label='Restaurar')
        butabout = wx.Button(panelbut, label='Acerca de')

        #Additions to sizers
        sizerbut = wx.BoxSizer(wx.VERTICAL)

        sizerhead = wx.BoxSizer(wx.HORIZONTAL)
        sizerhead.Add(labelhead, -1, wx.ALL | wx.CENTER)
        sizerbut.Add(sizerhead, -1, wx.TOP | wx.CENTER)

        sizerws1 = wx.BoxSizer(wx.HORIZONTAL)
        sizerws1.Add(whitespace, -1, wx.ALL)
        sizerbut.Add(sizerws1, -1, wx.TOP | wx.CENTER)

        sizermiter = wx.BoxSizer(wx.HORIZONTAL)
        sizermiter.Add(labelmiter, -1, wx.ALL)
        sizermiter.Add(self.boxmiter, -1, wx.ALL)
        sizerbut.Add(sizermiter, -1, wx.TOP | wx.CENTER)

        sizerxmin = wx.BoxSizer(wx.HORIZONTAL)
        sizerxmin.Add(labelmxmin, -1, wx.ALL)
        sizerxmin.Add(self.boxxmin, -1, wx.ALL)
        sizerbut.Add(sizerxmin, -1, wx.TOP | wx.CENTER)

        sizerxmax = wx.BoxSizer(wx.HORIZONTAL)
        sizerxmax.Add(labelmxmax, -1, wx.ALL)
        sizerxmax.Add(self.boxxmax, -1, wx.ALL)
        sizerbut.Add(sizerxmax, -1, wx.TOP | wx.CENTER)

        sizerymin = wx.BoxSizer(wx.HORIZONTAL)
        sizerymin.Add(labelmymin, -1, wx.ALL)
        sizerymin.Add(self.boxymin, -1, wx.ALL)
        sizerbut.Add(sizerymin, -1, wx.TOP | wx.CENTER)

        sizerymax = wx.BoxSizer(wx.HORIZONTAL)
        sizerymax.Add(labelmymax, -1, wx.ALL)
        sizerymax.Add(self.boxymax, -1, wx.ALL)
        sizerbut.Add(sizerymax, -1, wx.TOP | wx.CENTER)

        sizerdens = wx.BoxSizer(wx.HORIZONTAL)
        sizerdens.Add(labeldens, -1, wx.ALL)
        sizerdens.Add(self.boxdens, -1, wx.ALL)
        sizerbut.Add(sizerdens, -1, wx.TOP | wx.CENTER)

        sizerfunc = wx.BoxSizer(wx.HORIZONTAL)
        sizerfunc.Add(labelfunc, -1, wx.ALL)
        sizerfunc.Add(self.boxfunc, -1, wx.ALL)
        sizerbut.Add(sizerfunc, -1, wx.TOP | wx.CENTER)

        sizerrec = wx.BoxSizer(wx.HORIZONTAL)
        sizerrec.Add(labelrec, -1, wx.ALL)
        sizerrec.Add(self.boxrec, -1, wx.ALL)
        sizerbut.Add(sizerrec, -1, wx.TOP | wx.CENTER)

        sizerimc = wx.BoxSizer(wx.HORIZONTAL)
        sizerimc.Add(labelimc, -1, wx.ALL)
        sizerimc.Add(self.boximc, -1, wx.ALL)
        sizerbut.Add(sizerimc, -1, wx.TOP | wx.CENTER)

        sizerws2 = wx.BoxSizer(wx.HORIZONTAL)
        sizerws2.Add(whitespace, -1, wx.ALL)
        sizerbut.Add(sizerws2, -1, wx.TOP | wx.CENTER)

        sizercolp = wx.BoxSizer(wx.HORIZONTAL)
        sizercolp.Add(labelcolp, -1, wx.ALL)
        sizercolp.Add(self.combcolp, -1, wx.ALL)
        sizerbut.Add(sizercolp, -1, wx.TOP | wx.CENTER)

        sizerinvp = wx.BoxSizer(wx.HORIZONTAL)
        sizerinvp.Add(self.invcolp, -1, wx.ALL)
        sizerbut.Add(sizerinvp, -1, wx.TOP | wx.CENTER)

        sizerextx = wx.BoxSizer(wx.HORIZONTAL)
        sizerextx.Add(labelextx, -1, wx.ALL)
        sizerbut.Add(sizerextx, -1, wx.TOP | wx.CENTER)

        sizermagn = wx.BoxSizer(wx.HORIZONTAL)
        sizermagn.Add(labelmagn, -1, wx.ALL)
        sizermagn.Add(self.boxmagn, -1, wx.ALL)
        sizerbut.Add(sizermagn, -1, wx.TOP | wx.CENTER)

        sizerws3 = wx.BoxSizer(wx.HORIZONTAL)
        sizerws3.Add(whitespace, -1, wx.ALL)
        sizerbut.Add(sizerws3, -1, wx.TOP | wx.CENTER)

        sizerbut.Add(butexec, -1, wx.TOP | wx.EXPAND)
        sizerbut.Add(butrest, -1, wx.TOP | wx.EXPAND)
        sizerbut.Add(butabout, -1, wx.TOP | wx.EXPAND)

        #Bindings
        self.Bind(wx.EVT_BUTTON, self.execute, butexec)
        self.Bind(wx.EVT_BUTTON, self.restore, butrest)
        self.Bind(wx.EVT_BUTTON, self.about, butabout)
        cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)

        panelbut.SetSizer(sizerbut)
        mainsizer.Add(panelbut, 0, wx.TOP)
        parent.SetSizer(mainsizer)

    def onclick(self, event):
        bt, xc, yc = (event.button, event.xdata, event.ydata)
        zoom = float(self.boxmagn.GetValue())
        if is_number(zoom) and float(zoom)!= 0:
            xdist = (float(self.boxxmax.GetValue()) - float(self.boxxmin.GetValue()))/(2*zoom)
            ydist = (float(self.boxymax.GetValue()) - float(self.boxymin.GetValue()))/(2*zoom)
        else:
            dlg = wx.MessageDialog(self.frame, u"Error en los parámetros", "Error!", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        if bt == 3:
            self.boxxmin.SetValue(str(xc - xdist))
            self.japi.xmin = xc - xdist
            self.boxxmax.SetValue(str(xc + xdist))
            self.japi.xmax = xc + xdist
            self.boxymin.SetValue(str(yc - ydist))
            self.japi.ymin = yc - ydist
            self.boxymax.SetValue(str(yc + ydist))
            self.japi.ymax = yc + ydist
            self.execute(self)

    def numbercheck(self, numberlist):
        for numb in numberlist:
            if not is_number(numb):
                return False
        return True

    def execute(self, event):
        iblist = []
        iblist.append(self.boxmiter.GetValue())
        iblist.append(self.boxxmin.GetValue())
        iblist.append(self.boxxmax.GetValue())
        iblist.append(self.boxymin.GetValue())
        iblist.append(self.boxymax.GetValue())
        iblist.append(self.boxdens.GetValue())
        iblist.append(self.boxrec.GetValue())
        iblist.append(self.boximc.GetValue())

        er = self.numbercheck(iblist)

        if er:
            self.maxiter = int(self.boxmiter.GetValue())
            self.Xmin = float(self.boxxmin.GetValue())
            self.Xmax = float(self.boxxmax.GetValue())
            self.Ymin = float(self.boxymin.GetValue())
            self.Ymax = float(self.boxymax.GetValue())
            self.Densidad = float(self.boxdens.GetValue())

            self.c = complex(float(self.boxrec.GetValue()), float(self.boximc.GetValue()))
            if self.Xmin > self.Xmax or self.Ymin > self.Ymax:
                er = False
            elif self.maxiter <= 0 or self.Densidad <= 0:
                er = False

        self.fun = self.boxfunc.GetValue()

        if (not er) or (self.fun == ''):
            dlg = wx.MessageDialog(self.frame, u"Error en los parámetros.", "Error!", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
        if er:
            iters = self.japi.juliaimage(self.fun, self.c)
            self.ax.cla()

            self.paleta = self.combcolp.GetValue()
            self.k = 1 - self.invcolp.IsChecked()

            if self.paleta == self.colourlist[0]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.RdYlBu,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.colourlist[1]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.binary,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.colourlist[2]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.Blues,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.colourlist[3]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.RdYlGn,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.colourlist[4]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.hot,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.colourlist[5]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.PuRd,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))
            elif self.paleta == self.colourlist[6]:
                self.ax.imshow(self.k + (-1)**self.k * log(iters), cmap=cm.YlOrBr,
                               extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))

            # cmap permite cambiar la paleta de colores. http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
            # Para anadir un color nuevo, escribirlo en self.listacolores y colocar otro elif con su corresp. codigo
            self.canvas.draw()

    def restore(self, event):
        self.boxmiter.SetValue('100')
        self.japi.maxiter = 100
        self.boxxmin.SetValue('-2')
        self.japi.xmin = -2
        self.boxxmax.SetValue('2')
        self.japi.xmax = 2
        self.boxymin.SetValue('-1.5')
        self.japi.ymin = -1.5
        self.boxymax.SetValue('1.5')
        self.japi.ymax = 1.5
        self.boxdens.SetValue('500')
        self.japi.densidad = 500
        self.boxrec.SetValue('-0.4')
        self.boximc.SetValue('0.6')
        self.invcolp.SetValue(False)
        self.combcolp.SetValue(self.colourlist[0])
        self.canvas.draw()
        self.boxmiter.SetFocus()
        self.execute(self)



    def about(self, event):
        descripcion = u"""Este programa permite la visualización de los distintos conjuntos de Julia
         asociados a un número complejo c, pudiendo además definirse distintas funciones para
         visualizar J(f) y usarse varias paletas de colores y distintos ajustes."""
        inform = wx.AboutDialogInfo()
        inform.SetIcon(wx.Icon('iconojul.png', wx.BITMAP_TYPE_PNG))
        inform.SetName('Conjuntos de Julia')
        inform.SetDescription(descripcion)
        inform.SetCopyright(u'Juan Antonio Macías - Marina Molina - Ana López')
        inform.SetWebSite('www.github.com/JuanMtg/JuliaSets')

        wx.AboutBox(inform)

def main():
    app = FractalApp(0)
    app.MainLoop()

if __name__ == '__main__':
    main()