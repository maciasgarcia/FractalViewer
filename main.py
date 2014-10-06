# -*- coding: utf-8 -*-
import wx
from gui import *


class SplashScreen(wx.SplashScreen):
    """
Create a splash screen widget.
    """
    def __init__(self, parent=None):
        # This is a recipe to a the screen.
        # Modify the following variables as necessary.
        aBitmap = wx.Image(name = "images/splashscreen.png").ConvertToBitmap()
        splashStyle = wx.SPLASH_CENTRE_ON_SCREEN | wx.SPLASH_TIMEOUT
        splashDuration = 1000 # milliseconds
        # Call the constructor with the above arguments in exactly the
        # following order.
        wx.SplashScreen.__init__(self, aBitmap, splashStyle,
                                 splashDuration, parent)

        wx.Yield()

class MainFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Fractales", size=(1000, 700))
        self.Center()
        # Created Panel and Notebook.
        p = wx.Panel(self)
        nb = wx.Notebook(p)

        # Defining pages.
        page1 = MandelbrotPanel(nb)
        page2 = JuliaPanel(nb)
        page3 = RelationPanel(nb)
        page4 = NewtonPanel(nb)

        # Adding pages.
        nb.AddPage(page1, u"Mandelbrot")
        nb.AddPage(page2, u"Julia")
        nb.AddPage(page3, u"Relación")
        nb.AddPage(page4, u'Newton')

        # Putting the notebook in a sizer and defining it as the main one.
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        p.SetSizer(sizer)

class MainApp(wx.App):
    def OnInit(self):
        MySplash = SplashScreen()
        MySplash.Show()
        MainFrame().Show()

        return True


if __name__ == "__main__":
    app = MainApp(1, 'log')
    app.MainLoop()
