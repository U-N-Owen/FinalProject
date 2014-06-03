import wx


class StartFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent)
		self.panel = wx.Panel(self)
		self.prompt1 = wx.StaticText(self.panel, label="How many colors are in the detonation abort sequence?", pos=(40,10))
		self.Resp1 = wx.TextCtrl(self.panel, pos=(40,40))
		self.prompt2 = wx.StaticText(self.panel, label="How many turns until detonation?", pos=(40,70))
		self.Resp2 = wx.TextCtrl(self.panel, pos=(40,100))
		self.btnSubmit = wx.Button(self.panel, label="Start attempt at disarmament of explosive", pos=(40,130), size=(200,50))
		self.btnSubmit.Bind(wx.EVT_BUTTON, self.OnSubmit)
	
	def OnSubmit(self, e):
		if self.Resp1.GetValue() >= 1 and self.Resp1.GetValue() <= 16:
			NumOfColours = self.Resp1.GetValue()
		else:
			wx.MessageBox("Enter the number of colors that the code contains.", "---WARNING---", wx.OK)
		if self.Resp2.GetValue() >= 2:
			NumOfTurns = self.Resp2.GetValue()
		elif self.Resp2.GetValue() == "":
			NumOfTurns = -1
		else:
			wx.MessageBox("Enter the Number of turns before detonation, leave blank for unlimited turns.", "---WARNING---", wx.OK)

app = wx.App(False)
Frame = StartFrame(None)
Frame.Show()
app.MainLoop()