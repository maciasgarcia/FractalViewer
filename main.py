# -*- coding: utf-8 -*-
import wx
from gui import *


class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Fractales", size=(1000, 700))

        # Created Panel and Notebook.
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        # Defining pages.
        page1 = MandelbrotPanel(nb)
        page2 = JuliaPanel(nb)
        page3 = RelationPanel(nb)

        # Adding pages.
        nb.AddPage(page1, u"Mandelbrot")
        nb.AddPage(page2, u"Julia")
        nb.AddPage(page3, u"Relación")

        # Putting the notebook in a sizer and defining it as the main one.
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    MainFrame().Show()
    app.MainLoop()
