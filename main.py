# -*- coding: utf-8 -*-
import wx
import ventana_julia
import ventana_mandelbrot

class MainWindow(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, title = title, size=(800,600))
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        #Texto Principal
        textcontent = u"""Elija el programa que quiere ejecutar"""
        sizerText = wx.BoxSizer(wx.HORIZONTAL)
        text = wx.StaticText(self, -1, textcontent)
        sizerText.Add(text, -1, wx.ALL | wx.CENTER)
        self.sizer.Add(sizerText, -1, wx.TOP | wx.CENTER)

        #Botones
        sizerbut = wx.BoxSizer(wx.HORIZONTAL)
        self.sizer.Add(sizerbut, -1, wx.TOP | wx.CENTER)

        sizerJulia = wx.BoxSizer(wx.HORIZONTAL)
        imgJulia = wx.Image('iconojul.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        butJulia = wx.BitmapButton(self, -1, imgJulia,
            pos=(10, 20), size = (imgJulia.GetWidth()+5, imgJulia.GetHeight()+5))

        sizerJulia.Add(butJulia, -1, wx.TOP | wx.CENTER)
        sizerbut.Add(sizerJulia, -1, wx.TOP | wx.CENTER)

        sizerMand = wx.BoxSizer(wx.HORIZONTAL)
        imgMand = wx.Image('iconomand.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap()
        butMand = wx.BitmapButton(self, -1, imgMand,
            pos=(10, 20), size = (imgMand.GetWidth()+5, imgMand.GetHeight()+5))
        sizerMand.Add(butMand, -1, wx.TOP | wx.CENTER)
        sizerbut.Add(sizerMand, -1, wx.TOP | wx.CENTER)

        #Eventos para los botones
        self.Bind(wx.EVT_BUTTON, self.onButJulia, butJulia)
        self.Bind(wx.EVT_BUTTON, self.onButMand, butMand)

        #Layout sizers
        self.SetSizer(self.sizer)
        self.SetAutoLayout(1)
        self.sizer.Fit(self)

        self.Show(True)

    #Definición de funciones
    def onButJulia(self, event):
        ventana_julia.main()

    def onButMand(self, event):
        ventana_mandelbrot.main()


if __name__ == '__main__':
    app = wx.App(False)
    frame = MainWindow(None, "Fractales")
    app.MainLoop()

