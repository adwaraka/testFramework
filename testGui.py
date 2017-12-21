import time, wx, sys, subprocess
from threading import *

ID_FRAME = wx.NewId()
ID_PANEL = wx.NewId()
ID_LOG = wx.NewId()
ID_START = wx.NewId()
ID_STOP = wx.NewId()

class RedirectText:
    def __init__(self, aWxTextCtrl):
        self.out = aWxTextCtrl

    def write(self,string):
        self.out.WriteText(string)

class TestApp(wx.Frame):

    def __init__(self):
        # The main frame
        wx.Frame.__init__(self, None, ID_FRAME, "Testing App", size=(600,600))
 
        # Add a panel
        panel = wx.Panel(self, ID_PANEL)
        log = wx.TextCtrl(panel, ID_LOG, size=(600, 600), style = wx.TE_MULTILINE|wx.TE_READONLY)

        # Add the test run button
        start_btn = wx.Button(panel, ID_START, 'Run Tests')
        self.Bind(wx.EVT_BUTTON, self.onRun, start_btn)
        stop_btn = wx.Button(panel, ID_STOP, 'Stop Tests')
 
        # Add widgets to a sizer        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(log, 1, wx.ALL|wx.EXPAND, 5)

        # Add buttons to the GUI
        button_box = wx.BoxSizer(wx.HORIZONTAL)
        button_box.Add(start_btn, 0, wx.ALL|wx.LEFT, 10)
        button_box.Add(stop_btn, 0, wx.ALL|wx.RIGHT, 10)
        sizer.Add(button_box, 0, wx.ALL|wx.CENTER)

        # Adding the sizer to the panel
        panel.SetSizer(sizer)

        # Redirect text here
        sys.stdout = RedirectText(log)

    def onRun(self, event):
        self.commenceTests()

    def commenceTests(self):
        proc = subprocess.Popen("python -m app.tests.testEx -s --with-html-output",
                                shell=True,
                                stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE)
        while True:
            line = proc.stdout.readline()                        
            wx.Yield()
            if not line:
                break
            else:
                print line
        proc.wait()

# Run the program
if __name__ == "__main__":
    app = wx.App()
    frame = TestApp().Show()
    app.MainLoop()
