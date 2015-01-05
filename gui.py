# -*- coding: utf-8 -*-

import wx
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas
from matplotlib.backends.backend_wxagg import NavigationToolbar2WxAgg
import fractalapi as fapi
from fractalutils import *


class JuliaPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.japi = fapi.JuliaApi()
        self.initgui(self)
        self.ax = self.fig.add_subplot(111)
        self.execute(self)

    def initgui(self, parent):
        self.fig = Figure(figsize=(5, 5), dpi=100, facecolor=(0.3, 0.25, 0.3))

        #Panels
        paneldraw = wx.Panel(parent, -1)
        panelbut = wx.Panel(parent, -1)
        panelbut.SetBackgroundColour(wx.Colour(255, 255, 255))

        #Main Sizers
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
        labelxmin = wx.StaticText(panelbut, -1, u'  X Mínimo:')
        labelxmax = wx.StaticText(panelbut, -1, u'  X Máximo:')
        labelymin = wx.StaticText(panelbut, -1, u'  Y Mínimo:')
        labelymax = wx.StaticText(panelbut, -1, u'  Y Máximo:')
        labeldens = wx.StaticText(panelbut, -1, u'  Densidad:')
        labelfunc = wx.StaticText(panelbut, -1, u'  Función:')
        labelrec = wx.StaticText(panelbut, -1, u'   Re(c):')
        labelimc = wx.StaticText(panelbut, -1, u'   Im(c):')
        labelcolp = wx.StaticText(panelbut, -1, u'  Paleta de colores:')
        labelextx = wx.StaticText(panelbut, -1, u'Para ampliar el conjunto hacer click derecho.')
        labelmagn = wx.StaticText(panelbut, -1, u'  Magnificación:')

        #TextCtrls / Comboboxes / Checkboxes
        self.boxmiter = wx.TextCtrl(panelbut, -1, value=str(self.japi.maxiter),size=(-1, -1))
        self.boxxmin = wx.TextCtrl(panelbut, -1, value=str(self.japi.xmin), size=(-1, -1))
        self.boxxmax = wx.TextCtrl(panelbut, -1, value=str(self.japi.xmax), size=(-1, -1))
        self.boxymin = wx.TextCtrl(panelbut, -1, value=str(self.japi.ymin), size=(-1, -1))
        self.boxymax = wx.TextCtrl(panelbut, -1, value=str(self.japi.ymax), size=(-1, -1))
        self.boxdens = wx.TextCtrl(panelbut, -1, value=str(self.japi.densidad), size=(-1, -1))
        self.boxfunc = wx.TextCtrl(panelbut, -1, value='quadratic', size=(-1, -1))
        self.boxrec = wx.TextCtrl(panelbut, -1, value='-0.4', size=(-1, -1))
        self.boximc = wx.TextCtrl(panelbut, -1, value='0.6', size=(-1, -1))

        self.colourdict = {'Azul/Amarillo/Rojo' : 'cm.RdYlBu', 'Blanco y negro' : 'cm.binary',
                           'Azules' : 'cm.Blues', 'Verde/Amarillo/Rojo' : 'cm.RdYlGn',
                           'Hot' : 'cm.hot', 'Rosa' : 'cm.PuRd', 'Naranjas' : 'cm.YlOrBr'}
        self.combcolp = wx.ComboBox(panelbut, -1, choices=self.colourdict.keys(), style=wx.CB_READONLY,
                                    value='Azul/Amarillo/Rojo')
        self.invcolp = wx.CheckBox(panelbut, -1, 'Invertir paleta de colores')
        self.boxmagn = wx.TextCtrl(panelbut, -1, value='2', size=(-1,-1))

        #Buttons
        butexec = wx.Button(panelbut, label='Ejecutar')
        butrest = wx.Button(panelbut, label='Restaurar')
        butabout = wx.Button(panelbut, label='Acerca de')

        #Sizers
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
        sizerxmin.Add(labelxmin, -1, wx.ALL)
        sizerxmin.Add(self.boxxmin, -1, wx.ALL)
        sizerbut.Add(sizerxmin, -1, wx.TOP | wx.CENTER)

        sizerxmax = wx.BoxSizer(wx.HORIZONTAL)
        sizerxmax.Add(labelxmax, -1, wx.ALL)
        sizerxmax.Add(self.boxxmax, -1, wx.ALL)
        sizerbut.Add(sizerxmax, -1, wx.TOP | wx.CENTER)

        sizerymin = wx.BoxSizer(wx.HORIZONTAL)
        sizerymin.Add(labelymin, -1, wx.ALL)
        sizerymin.Add(self.boxymin, -1, wx.ALL)
        sizerbut.Add(sizerymin, -1, wx.TOP | wx.CENTER)

        sizerymax = wx.BoxSizer(wx.HORIZONTAL)
        sizerymax.Add(labelymax, -1, wx.ALL)
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
            dlg = wx.MessageDialog(self, u"Error en los parámetros", "Error!", wx.OK | wx.ICON_WARNING)
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

        er = numbercheck(iblist)

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

        self.func = self.boxfunc.GetValue()

        if (not er) or (self.func == ''):
            dlg = wx.MessageDialog(self, u"Error en los parámetros.", "Error!", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        if er:
            iters = self.japi.juliaimage(self.func, self.c)
            self.ax.cla()

            self.paleta = self.combcolp.GetValue()
            self.colourcode = self.colourdict[self.paleta]
            self.k = 1 - self.invcolp.IsChecked()

            self.ax.imshow(self.k + (-1)**self.k *log(iters), cmap=eval(self.colourcode),
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
        self.combcolp.SetValue('Azul/Amarillo/Rojo')
        self.canvas.draw()
        self.boxmiter.SetFocus()
        self.execute(self)

    def about(self, event):
        descripcion = u"""Este programa permite la visualización de los distintos conjuntos de Julia
         asociados a un número complejo c, pudiendo además definirse distintas funciones para
         visualizar J(f) y usarse varias paletas de colores y distintos ajustes."""
        inform = wx.AboutDialogInfo()
        inform.SetIcon(wx.Icon('images/iconojul.png', wx.BITMAP_TYPE_PNG))
        inform.SetName('Conjuntos de Julia')
        inform.SetDescription(descripcion)
        inform.SetCopyright(u'Juan Antonio Macías - Marina Molina - Ana López')
        inform.SetWebSite('www.github.com/JuanMtg/JuliaSets')

        wx.AboutBox(inform)


class MandelbrotPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.mapi = fapi.MandelbrotApi()
        self.initgui(self)
        self.ax = self.fig.add_subplot(111)
        self.execute(self)

    def initgui(self, parent):
        self.fig = Figure(figsize=(5,5), dpi=100, facecolor=(0.3, 0.25, 0.3))

        #Panels
        paneldraw = wx.Panel(parent, -1)
        panelbut = wx.Panel(parent, -1)
        panelbut.SetBackgroundColour(wx.Colour(255, 255, 255))

        #Main Sizers
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
        labelhead.SetFont( wx.Font( 11, 74, 93, 92, True, "Tahoma"))

        whitespace = wx.StaticText(panelbut, -1, '')

        labelmiter = wx.StaticText(panelbut, -1, u'  Máx iteraciones:')
        labelxmin = wx.StaticText(panelbut, -1, u'  X Mínimo:')
        labelxmax = wx.StaticText(panelbut, -1, u'  X Máximo:')
        labelymin = wx.StaticText(panelbut, -1, u'  Y Mínimo:')
        labelymax = wx.StaticText(panelbut, -1, u'  Y Máximo:')
        labeldens = wx.StaticText(panelbut, -1, u'  Densidad:')
        labelfunc = wx.StaticText(panelbut, -1, u'  Función:')
        labelcolp = wx.StaticText(panelbut, -1, u'  Paleta de colores:')
        labelextx = wx.StaticText(panelbut, -1, u'Para ampliar el conjunto hacer click derecho.')
        labelmagn = wx.StaticText(panelbut, -1, u'  Magnificación:')

        #TextCtrls / Comboboxes / Checkboxes
        self.boxmiter = wx.TextCtrl(panelbut, -1, value=str(self.mapi.maxiter), size=(-1,-1))
        self.boxxmin = wx.TextCtrl(panelbut, -1, value=str(self.mapi.xmin), size=(-1,-1))
        self.boxxmax = wx.TextCtrl(panelbut, -1, value=str(self.mapi.xmax), size=(-1,-1))
        self.boxymin = wx.TextCtrl(panelbut, -1, value=str(self.mapi.ymin), size=(-1,-1))
        self.boxymax = wx.TextCtrl(panelbut, -1, value=str(self.mapi.ymax), size=(-1,-1))
        self.boxdens = wx.TextCtrl(panelbut, -1, value=str(self.mapi.densidad), size=(-1,-1))
        self.boxfunc = wx.TextCtrl(panelbut, -1, value='quadratic',size=(-1,-1))

        self.colourdict = {'Azul/Amarillo/Rojo' : 'cm.RdYlBu', 'Blanco y negro' : 'cm.binary',
                           'Azules' : 'cm.Blues', 'Verde/Amarillo/Rojo' : 'cm.RdYlGn',
                           'Hot' : 'cm.hot', 'Rosa' : 'cm.PuRd', 'Naranjas' : 'cm.YlOrBr'}
        self.combcolp = wx.ComboBox(panelbut, -1, choices=self.colourdict.keys(), style=wx.CB_READONLY,
                                       value='Azul/Amarillo/Rojo')
        self.invcolp = wx.CheckBox(panelbut, -1, 'Invertir paleta de colores')
        self.boxmagn = wx.TextCtrl(panelbut, -1, value='2', size=(-1,-1))

        #Buttons
        butexec = wx.Button(panelbut, label='Ejecutar')
        butrest = wx.Button(panelbut,label='Restaurar')
        butabout = wx.Button(panelbut, label='Acerca de')

        #Sizers
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
        sizerxmin.Add(labelxmin, -1, wx.ALL)
        sizerxmin.Add(self.boxxmin, -1, wx.ALL)
        sizerbut.Add(sizerxmin, -1, wx.TOP | wx.CENTER)

        sizerxmax = wx.BoxSizer(wx.HORIZONTAL)
        sizerxmax.Add(labelxmax, -1, wx.ALL)
        sizerxmax.Add(self.boxxmax, -1, wx.ALL)
        sizerbut.Add(sizerxmax, -1, wx.TOP | wx.CENTER)

        sizerymin = wx.BoxSizer(wx.HORIZONTAL)
        sizerymin.Add(labelymin, -1, wx.ALL)
        sizerymin.Add(self.boxymin, -1, wx.ALL)
        sizerbut.Add(sizerymin, -1, wx.TOP | wx.CENTER)

        sizerymax = wx.BoxSizer(wx.HORIZONTAL)
        sizerymax.Add(labelymax, -1, wx.ALL)
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
        sizerextx.Add(labelextx, -1, wx.ALL | wx.CENTER)
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
        self.Bind(wx.EVT_BUTTON,self.restore,butrest)
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
            dlg = wx.MessageDialog(self, u"Error en los parámetros", "Error!", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
        if bt == 3:
            self.boxxmin.SetValue(str(xc - xdist))
            self.mapi.xmin = xc - xdist
            self.boxxmax.SetValue(str(xc + xdist))
            self.mapi.xmax = xc + xdist
            self.boxymin.SetValue(str(yc - ydist))
            self.mapi.ymin = yc - ydist
            self.boxymax.SetValue(str(yc + ydist))
            self.mapi.ymax = yc + ydist
            self.execute(self)

    def execute(self,event):
        iblist = []
        iblist.append(self.boxmiter.GetValue())
        iblist.append(self.boxxmin.GetValue())
        iblist.append(self.boxxmax.GetValue())
        iblist.append(self.boxymin.GetValue())
        iblist.append(self.boxymax.GetValue())
        iblist.append(self.boxdens.GetValue())

        er = numbercheck(iblist)

        if er:
            self.maxiter = int(self.boxmiter.GetValue())
            self.Xmin = float(self.boxxmin.GetValue())
            self.Xmax = float(self.boxxmax.GetValue())
            self.Ymin = float(self.boxymin.GetValue())
            self.Ymax = float(self.boxymax.GetValue())
            self.Densidad = float(self.boxdens.GetValue())

            if self.Xmin > self.Xmax or self.Ymin > self.Ymax:
                er = False
            elif self.maxiter <= 0 or self.Densidad <= 0:
                er = False

        self.func = self.boxfunc.GetValue()

        if (not er) or (self.func == ''):
            dlg = wx.MessageDialog(self, u"Error en los parámetros.", "Error!", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        if er:
            iters = self.mapi.mandimage(self.func)
            self.ax.cla()

            self.paleta = self.combcolp.GetValue()
            self.colourcode = self.colourdict[self.paleta]
            self.k = 1 - self.invcolp.IsChecked()

            self.ax.imshow(self.k + (-1)**self.k *log(iters), cmap=eval(self.colourcode),
                           extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))

            # cmap permite cambiar la paleta de colores. http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
            # Para anadir un color nuevo, escribirlo en self.listacolores y colocar otro elif con su corresp. codigo
            self.canvas.draw()

    def restore(self,event):
        self.boxmiter.SetValue('100')
        self.mapi.maxiter = 100
        self.boxxmin.SetValue('-2.5')
        self.mapi.xmin = -2.5
        self.boxxmax.SetValue('1.5')
        self.mapi.xmax = 1.5
        self.boxymin.SetValue('-1.5')
        self.mapi.ymin = -1.5
        self.boxymax.SetValue('1.5')
        self.mapi.ymax = 1.5
        self.boxdens.SetValue('500')
        self.mapi.densidad = 500
        self.invcolp.SetValue(False)
        self.combcolp.SetValue('Azul/Amarillo/Rojo')
        self.canvas.draw()
        self.boxmiter.SetFocus()
        self.execute(self)

    def about(self, event):
        descripcion = u"""Este programa permite la visualización del fractal de Newton,
        pudiendo definirse nuevas funciones para visualizar dicho conjunto y usarse varias paletas
        de colores y distintos ajustes de visualización."""
        inform = wx.AboutDialogInfo()
        inform.SetIcon(wx.Icon('images/iconomand.png', wx.BITMAP_TYPE_PNG))
        inform.SetName('Conjunto de Mandelbrot')
        inform.SetDescription(descripcion)
        inform.SetCopyright(u'Juan Antonio Macías')
        inform.SetWebSite('www.github.com/JuanMtg/JuliaSets')

        wx.AboutBox(inform)


class RelationPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.japi = fapi.JuliaApi()
        self.mapi = fapi.MandelbrotApi()
        self.initgui(self)
        self.ax2 = self.fig.add_subplot(211)
        self.ax = self.fig.add_subplot(212)
        self.execute(self)

    def initgui(self, parent):
        self.fig = Figure(figsize=(5, 5), dpi=100, facecolor=(0.3, 0.25, 0.3))

        #Panels
        paneldraw = wx.Panel(parent, -1)
        panelbut = wx.Panel(parent, -1)
        panelbut.SetBackgroundColour(wx.Colour(255, 255, 255))

        #Main Sizers
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
        labelxmin = wx.StaticText(panelbut, -1, u'  X Mínimo:')
        labelxmax = wx.StaticText(panelbut, -1, u'  X Máximo:')
        labelymin = wx.StaticText(panelbut, -1, u'  Y Mínimo:')
        labelymax = wx.StaticText(panelbut, -1, u'  Y Máximo:')
        labeldens = wx.StaticText(panelbut, -1, u'  Densidad:')
        labelfunc = wx.StaticText(panelbut, -1, u'  Función:')
        labelrec = wx.StaticText(panelbut, -1, u'   Re(c):')
        labelimc = wx.StaticText(panelbut, -1, u'   Im(c):')
        self.labelconex1 = wx.StaticText(panelbut, -1, u'El punto NO está en el conjunto de '
                                                     u'Mandelbrot.')
        self.labelconex2 = wx.StaticText(panelbut, -1, u'Entonces el conjunto de Julia asociado NO es '
                                                     u'conexo.')
        labelcolp = wx.StaticText(panelbut, -1, u'  Paleta de colores:')
        labelex1 = wx.StaticText(panelbut, -1, u' Haga click derecho en el conjunto de Mandelbrot')
        labelex2 = wx.StaticText(panelbut, -1, u' para ver el conjunto de Julia asociado a dicho punto. ')
        labelex3 = wx.StaticText(panelbut, -1, u'Para ampliar el conjunto de Mandelbrot hacer doble '
                                               u'click.')


        #TextCtrls / Comboboxes / Checkboxes
        self.boxmiter = wx.TextCtrl(panelbut, -1, value=str(self.japi.maxiter),size=(-1, -1))
        self.boxxmin = wx.TextCtrl(panelbut, -1, value=str(self.japi.xmin), size=(-1, -1))
        self.boxxmax = wx.TextCtrl(panelbut, -1, value=str(self.japi.xmax), size=(-1, -1))
        self.boxymin = wx.TextCtrl(panelbut, -1, value=str(self.japi.ymin), size=(-1, -1))
        self.boxymax = wx.TextCtrl(panelbut, -1, value=str(self.japi.ymax), size=(-1, -1))
        self.boxdens = wx.TextCtrl(panelbut, -1, value=str(self.japi.densidad), size=(-1, -1))
        self.boxfunc = wx.TextCtrl(panelbut, -1, value='quadratic', size=(-1, -1))
        self.boxrec = wx.TextCtrl(panelbut, -1, value='-0.4', size=(-1, -1))
        self.boximc = wx.TextCtrl(panelbut, -1, value='0.6', size=(-1, -1))

        self.colourdict = {'Azul/Amarillo/Rojo' : 'cm.RdYlBu', 'Blanco y negro' : 'cm.binary',
                           'Azules' : 'cm.Blues', 'Verde/Amarillo/Rojo' : 'cm.RdYlGn',
                           'Hot' : 'cm.hot', 'Rosa' : 'cm.PuRd', 'Naranjas' : 'cm.YlOrBr'}
        self.combcolp = wx.ComboBox(panelbut, -1, choices=self.colourdict.keys(), style=wx.CB_READONLY,
                                    value='Azul/Amarillo/Rojo')
        self.invcolp = wx.CheckBox(panelbut, -1, 'Invertir paleta de colores')

        #Buttons
        butexec = wx.Button(panelbut, label='Ejecutar')
        butrest = wx.Button(panelbut, label='Restaurar')
        butabout = wx.Button(panelbut, label='Acerca de')

        #Sizers
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
        sizerxmin.Add(labelxmin, -1, wx.ALL)
        sizerxmin.Add(self.boxxmin, -1, wx.ALL)
        sizerbut.Add(sizerxmin, -1, wx.TOP | wx.CENTER)

        sizerxmax = wx.BoxSizer(wx.HORIZONTAL)
        sizerxmax.Add(labelxmax, -1, wx.ALL)
        sizerxmax.Add(self.boxxmax, -1, wx.ALL)
        sizerbut.Add(sizerxmax, -1, wx.TOP | wx.CENTER)

        sizerymin = wx.BoxSizer(wx.HORIZONTAL)
        sizerymin.Add(labelymin, -1, wx.ALL)
        sizerymin.Add(self.boxymin, -1, wx.ALL)
        sizerbut.Add(sizerymin, -1, wx.TOP | wx.CENTER)

        sizerymax = wx.BoxSizer(wx.HORIZONTAL)
        sizerymax.Add(labelymax, -1, wx.ALL)
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

        sizerconex = wx.BoxSizer(wx.VERTICAL)
        sizerconex.Add(self.labelconex1, -1, wx.ALL)
        sizerconex.Add(self.labelconex2, -1, wx.ALL)
        sizerbut.Add(sizerconex, -1, wx.TOP | wx.CENTER)

        sizerws3 = wx.BoxSizer(wx.HORIZONTAL)
        sizerws3.Add(whitespace, -1, wx.ALL)
        sizerbut.Add(sizerws3, -1, wx.TOP | wx.CENTER)

        sizercolp = wx.BoxSizer(wx.HORIZONTAL)
        sizercolp.Add(labelcolp, -1, wx.ALL)
        sizercolp.Add(self.combcolp, -1, wx.ALL)
        sizerbut.Add(sizercolp, -1, wx.TOP | wx.CENTER)

        sizerinvp = wx.BoxSizer(wx.HORIZONTAL)
        sizerinvp.Add(self.invcolp, -1, wx.ALL)
        sizerbut.Add(sizerinvp, -1, wx.TOP | wx.CENTER)

        sizerex = wx.BoxSizer(wx.VERTICAL)
        sizerex.Add(labelex1, -1, wx.ALL)
        sizerex.Add(labelex2, -1, wx.ALL)
        sizerbut.Add(sizerex, -1, wx.TOP | wx.CENTER)

        sizerex2 = wx.BoxSizer(wx.VERTICAL)
        sizerex2.Add(labelex3, -1, wx.ALL)
        sizerbut.Add(sizerex2, -1, wx.TOP | wx.CENTER)

        sizerws4 = wx.BoxSizer(wx.HORIZONTAL)
        sizerws4.Add(whitespace, -1, wx.ALL)
        sizerbut.Add(sizerws4, -1, wx.TOP | wx.CENTER)

        sizerbut.Add(butexec, -1, wx.TOP | wx.EXPAND)
        sizerbut.Add(butrest, -1, wx.TOP | wx.EXPAND)
        sizerbut.Add(butabout, -1, wx.TOP | wx.EXPAND)

        #Bindings
        self.Bind(wx.EVT_BUTTON, self.execute, butexec)
        self.Bind(wx.EVT_BUTTON, self.restore, butrest)
        self.Bind(wx.EVT_BUTTON, self.about, butabout)
        self.fig.canvas.mpl_connect('button_press_event', self.onclick)

        panelbut.SetSizer(sizerbut)
        mainsizer.Add(panelbut, 0, wx.TOP)
        parent.SetSizer(mainsizer)

    def onclick(self, event):
        bt, xc, yc = (event.button, event.xdata, event.ydata)
        iters = int(self.boxmiter.GetValue())*2
        func = self.boxfunc.GetValue()
        zoom = 2
        if bt == 3:
            self.boxrec.SetValue(str(xc))
            self.boximc.SetValue(str(yc))
            self.execjulia(self)
            if inmandelbrot(func, xc + yc*1j, iters):
                self.labelconex1.SetLabel(u'El punto SÍ está en el conjunto de Mandelbrot.')
                self.labelconex2.SetLabel(u'Entonces el conjunto de Julia asociado SÍ es conexo.')
            else:
                self.labelconex1.SetLabel(u'El punto NO está en el conjunto de Mandelbrot.')
                self.labelconex2.SetLabel(u'Entonces el conjunto de Julia asociado NO es conexo.')

        if event.dblclick and bt == 1:
            xdist = (float(self.mapi.xmax) - float(self.mapi.xmin))/(2*zoom)
            ydist = (float(self.mapi.ymax) - float(self.mapi.ymin))/(2*zoom)
            self.mapi.xmin = xc - xdist
            self.mapi.xmax = xc + xdist
            self.mapi.ymin = yc - ydist
            self.mapi.ymax = yc + ydist
            self.execmand(self)

    def execmand(self, event):
        funct = self.boxfunc.GetValue()
        iters = self.mapi.mandimage(funct)
        self.ax2.cla()

        self.paleta = self.combcolp.GetValue()
        self.colourcode = self.colourdict[self.paleta]
        self.k = 1 - self.invcolp.IsChecked()

        self.ax2.imshow(self.k + (-1)**self.k *log(iters), cmap=eval(self.colourcode),
                       extent=(self.mapi.xmin, self.mapi.xmax, self.mapi.ymin, self.mapi.ymax))

        # cmap permite cambiar la paleta de colores. http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
        # Para anadir un color nuevo, escribirlo en self.listacolores y colocar otro elif con su corresp. codigo
        self.canvas.draw()

    def execjulia(self, event):
        iblist = []
        iblist.append(self.boxmiter.GetValue())
        iblist.append(self.boxxmin.GetValue())
        iblist.append(self.boxxmax.GetValue())
        iblist.append(self.boxymin.GetValue())
        iblist.append(self.boxymax.GetValue())
        iblist.append(self.boxdens.GetValue())
        iblist.append(self.boxrec.GetValue())
        iblist.append(self.boximc.GetValue())

        er = numbercheck(iblist)

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

        self.func = self.boxfunc.GetValue()

        if (not er) or (self.func == ''):
            dlg = wx.MessageDialog(self, u"Error en los parámetros.", "Error!", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        if er:
            iters = self.japi.juliaimage(self.func, self.c)
            self.ax.cla()

            self.paleta = self.combcolp.GetValue()
            self.colourcode = self.colourdict[self.paleta]
            self.k = 1 - self.invcolp.IsChecked()

            self.ax.imshow(self.k + (-1)**self.k *log(iters), cmap=eval(self.colourcode),
                           extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))

            # cmap permite cambiar la paleta de colores. http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
            # Para anadir un color nuevo, escribirlo en self.listacolores y colocar otro elif con su corresp. codigo
            self.canvas.draw()

    def execute(self, event):
        self.execmand(self)
        self.execjulia(self)

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
        self.combcolp.SetValue('Azul/Amarillo/Rojo')
        self.canvas.draw()
        self.boxmiter.SetFocus()
        #self.execjulia(self)
        # Restauramos los valores internos de Mandelbrot
        self.mapi.xmin = -2.5
        self.mapi.xmax = 1.5
        self.mapi.ymin = -1.5
        self.mapi.ymax = 1.5
        self.mapi.densidad = 500
        self.mapi.maxiter = 100
        self.execmand(self)

    def about(self, event):
        descripcion = u"""Este programa permite ver la correspondencia entre los puntos
        pertenecientes al conjunto de Mandelbrot y su respectivo conjunto de Julia asociado. En él
        se observa que si un punto pertenece al conjunto, entonces el conjunto de Julia es
        conexo."""
        inform = wx.AboutDialogInfo()
        inform.SetIcon(wx.Icon('images/iconoconnec.png', wx.BITMAP_TYPE_PNG))
        inform.SetName(u'Relación entre los conjuntos')
        inform.SetDescription(descripcion)
        inform.SetCopyright(u'Juan Antonio Macías - Marina Molina - Ana López')
        inform.SetWebSite('www.github.com/JuanMtg/JuliaSets')

        wx.AboutBox(inform)


class NewtonPanel(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.napi = fapi.NewtonApi()
        self.initgui(self)
        self.ax = self.fig.add_subplot(111)
        self.execute(self)

    def initgui(self, parent):
        self.fig = Figure(figsize=(5,5), dpi=100, facecolor=(0.3, 0.25, 0.3))

        #Panels
        paneldraw = wx.Panel(parent, -1)
        panelbut = wx.Panel(parent, -1)
        panelbut.SetBackgroundColour(wx.Colour(255, 255, 255))

        #Main Sizers
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
        labelhead.SetFont( wx.Font( 11, 74, 93, 92, True, "Tahoma"))

        whitespace = wx.StaticText(panelbut, -1, '')

        labelmiter = wx.StaticText(panelbut, -1, u'  Máx iteraciones:')
        labelxmin = wx.StaticText(panelbut, -1, u'  X Mínimo:')
        labelxmax = wx.StaticText(panelbut, -1, u'  X Máximo:')
        labelymin = wx.StaticText(panelbut, -1, u'  Y Mínimo:')
        labelymax = wx.StaticText(panelbut, -1, u'  Y Máximo:')
        labeldens = wx.StaticText(panelbut, -1, u'  Densidad:')
        labelfunc = wx.StaticText(panelbut, -1, u'  Función:')
        labelcolp = wx.StaticText(panelbut, -1, u'  Paleta de colores:')
        labelextx = wx.StaticText(panelbut, -1, u'Para ampliar el conjunto hacer click derecho.')
        labelmagn = wx.StaticText(panelbut, -1, u'  Magnificación:')

        #TextCtrls / Comboboxes / Checkboxes
        self.boxmiter = wx.TextCtrl(panelbut, -1, value=str(self.napi.maxiter), size=(-1,-1))
        self.boxxmin = wx.TextCtrl(panelbut, -1, value=str(self.napi.xmin), size=(-1,-1))
        self.boxxmax = wx.TextCtrl(panelbut, -1, value=str(self.napi.xmax), size=(-1,-1))
        self.boxymin = wx.TextCtrl(panelbut, -1, value=str(self.napi.ymin), size=(-1,-1))
        self.boxymax = wx.TextCtrl(panelbut, -1, value=str(self.napi.ymax), size=(-1,-1))
        self.boxdens = wx.TextCtrl(panelbut, -1, value=str(self.napi.densidad), size=(-1,-1))
        self.boxfunc = wx.TextCtrl(panelbut, -1, value=u'x**3 + 1',size=(-1,-1))

        self.colourdict = {'Azul/Amarillo/Rojo' : 'cm.RdYlBu', 'Blanco y negro' : 'cm.binary',
                           'Azules' : 'cm.Blues', 'Verde/Amarillo/Rojo' : 'cm.RdYlGn',
                           'Hot' : 'cm.hot', 'Rosa' : 'cm.PuRd', 'Naranjas' : 'cm.YlOrBr'}
        self.combcolp = wx.ComboBox(panelbut, -1, choices=self.colourdict.keys(), style=wx.CB_READONLY,
                                       value='Azul/Amarillo/Rojo')
        self.invcolp = wx.CheckBox(panelbut, -1, 'Invertir paleta de colores')
        self.boxmagn = wx.TextCtrl(panelbut, -1, value='2', size=(-1,-1))

        #Buttons
        butexec = wx.Button(panelbut, label='Ejecutar')
        butrest = wx.Button(panelbut,label='Restaurar')
        butabout = wx.Button(panelbut, label='Acerca de')

        #Sizers
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
        sizerxmin.Add(labelxmin, -1, wx.ALL)
        sizerxmin.Add(self.boxxmin, -1, wx.ALL)
        sizerbut.Add(sizerxmin, -1, wx.TOP | wx.CENTER)

        sizerxmax = wx.BoxSizer(wx.HORIZONTAL)
        sizerxmax.Add(labelxmax, -1, wx.ALL)
        sizerxmax.Add(self.boxxmax, -1, wx.ALL)
        sizerbut.Add(sizerxmax, -1, wx.TOP | wx.CENTER)

        sizerymin = wx.BoxSizer(wx.HORIZONTAL)
        sizerymin.Add(labelymin, -1, wx.ALL)
        sizerymin.Add(self.boxymin, -1, wx.ALL)
        sizerbut.Add(sizerymin, -1, wx.TOP | wx.CENTER)

        sizerymax = wx.BoxSizer(wx.HORIZONTAL)
        sizerymax.Add(labelymax, -1, wx.ALL)
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
        sizerextx.Add(labelextx, -1, wx.ALL | wx.CENTER)
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
        self.Bind(wx.EVT_BUTTON,self.restore,butrest)
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
            dlg = wx.MessageDialog(self, u"Error en los parámetros", "Error!", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()
        if bt == 3:
            self.boxxmin.SetValue(str(xc - xdist))
            self.napi.xmin = xc - xdist
            self.boxxmax.SetValue(str(xc + xdist))
            self.napi.xmax = xc + xdist
            self.boxymin.SetValue(str(yc - ydist))
            self.napi.ymin = yc - ydist
            self.boxymax.SetValue(str(yc + ydist))
            self.napi.ymax = yc + ydist
            self.execute(self)

    def execute(self,event):
        iblist = []
        iblist.append(self.boxmiter.GetValue())
        iblist.append(self.boxxmin.GetValue())
        iblist.append(self.boxxmax.GetValue())
        iblist.append(self.boxymin.GetValue())
        iblist.append(self.boxymax.GetValue())
        iblist.append(self.boxdens.GetValue())

        er = numbercheck(iblist)

        if er:
            self.maxiter = int(self.boxmiter.GetValue())
            self.Xmin = float(self.boxxmin.GetValue())
            self.Xmax = float(self.boxxmax.GetValue())
            self.Ymin = float(self.boxymin.GetValue())
            self.Ymax = float(self.boxymax.GetValue())
            self.Densidad = float(self.boxdens.GetValue())

            if self.Xmin > self.Xmax or self.Ymin > self.Ymax:
                er = False
            elif self.maxiter <= 0 or self.Densidad <= 0:
                er = False

        self.polyst = self.boxfunc.GetValue()
        self.func = sp.sympify(self.polyst)

        if (not er) or (self.polyst == ''):
            dlg = wx.MessageDialog(self, u"Error en los parámetros.", "Error!", wx.OK | wx.ICON_WARNING)
            dlg.ShowModal()
            dlg.Destroy()

        if er:
            iters = self.napi.newtonimage(self.func)
            self.ax.cla()

            self.paleta = self.combcolp.GetValue()
            self.colourcode = self.colourdict[self.paleta]
            self.k = 1 - self.invcolp.IsChecked()

            self.ax.imshow(self.k + (-1)**self.k *iters, cmap=eval(self.colourcode),
                           extent=(self.Xmin, self.Xmax, self.Ymin, self.Ymax))

            # cmap permite cambiar la paleta de colores. http://wiki.scipy.org/Cookbook/Matplotlib/Show_colormaps
            # Para anadir un color nuevo, escribirlo en self.listacolores y colocar otro elif con su corresp. codigo
            self.canvas.draw()

    def restore(self,event):
        self.boxmiter.SetValue('100')
        self.napi.maxiter = 100
        self.boxxmin.SetValue('-2')
        self.napi.xmin = -2
        self.boxxmax.SetValue('2')
        self.napi.xmax = 2
        self.boxymin.SetValue('-2')
        self.napi.ymin = -2
        self.boxymax.SetValue('2')
        self.napi.ymax = 2
        self.boxdens.SetValue('500')
        self.napi.densidad = 500
        self.invcolp.SetValue(False)
        self.combcolp.SetValue('Azul/Amarillo/Rojo')
        self.canvas.draw()
        self.boxmiter.SetFocus()
        self.execute(self)

    def about(self, event):
        descripcion = u"""Este programa permite la visualización del conjunto de Mandelbrot,
        pudiendo definirse nuevas funciones para visualizar dicho conjunto y usarse varias paletas
        de colores y distintos ajustes de visualización."""
        inform = wx.AboutDialogInfo()
        inform.SetIcon(wx.Icon('images/iconomand.png', wx.BITMAP_TYPE_PNG))
        inform.SetName('Conjunto de Mandelbrot')
        inform.SetDescription(descripcion)
        inform.SetCopyright(u'Juan Antonio Macías - Marina Molina - Ana López')
        inform.SetWebSite('www.github.com/JuanMtg/JuliaSets')

        wx.AboutBox(inform)


if __name__ == '__main__':
    pass