#!/usr/bin/env python

import wx

guess = []

#------------I/O--------------
class StartFrame(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent)
		self.panel = wx.Panel(self)
		self.prompt1 = wx.StaticText(self.panel, label="How many colors are in the detonation abort sequence?", pos=(40,10))
		self.Resp1 = wx.TextCtrl(self.panel, pos=(40,40))
		self.prompt2 = wx.StaticText(self.panel, label="How many turns until detonation?", pos=(40,70))
		self.Resp1 = wx.TextCtrl(self.panel, pos=(40,100))
		self.btnSubmit = wx.Button(self.panel, label="Start attempt at disarmament of explosive", pos=(40,130), size=(1000,50))
		self.btnSubmit.Bind(wx.EVT_BUTTON, self.OnSubmit)

	def OnSubmit(self, e):
		NumOfColours = self.prompt1.GetValue()
		if self.prompt2.GetValue() >= 2:
			NumOfTurns= self.prompt2.GetValue()
		elif self.prompt2.GetValue() == "":
			NumOfTurns = -1
		else:
			wx.MessageBox("Enter the Number of turns before detonation, leave blank for unlimited turns.", "---WARNING---", wx.OK)
		StartPanel.Hide()
		InputPanel.Show()
		OutputPanel.Show()

class InputPanel(wx.Panel):

	def __init__(self, parent, size=(300,500)):
		wx.Panel.__init__(self, parent)
		for x in NumOfColours:
			self.Image = []
			self.imageFile = []
			self.btn = []
			self.btnClick = []
			image[x] = "../assets/" + str(x) + ".jpg"
			imageFile[x] = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
			self.btn[x] = wx.BitmapButton(self.InputPanel, id=-1, bitmap=image[x],pos=(10, 20 * x), size = (imageFile[x].GetWidth()+5, image[x].GetHeight()+5))
			self.btn[x].Bind(wx.EVT_BUTTON, self.btnClick)
			self.btn[x].Show()
	def btnClick(self, e):
		for x in range(4):
			currentGuess = []
			clickedButton = e.GetEventObject()
			currentGuess.append(clickedbutton)
			if currentGuess.len == 4:
				guess.append(currentGuess)
"""
		image1File = "../assets/1.jpg"
		image1 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.btn1 = wx.BitmapButton(self.InputPanel, id=-1, bitmap=image1,
			pos=(10, 20), size = (image1.GetWidth()+5, image1.GetHeight()+5))
		self.button1.Bind(wx.EVT_BUTTON, self.button1Click)
			
		image2 = "../assets/2.jpg"
		image2 = wx.Image(imageFile, wx.BITMAP_TYPE_ANY).ConvertToBitmap()
		self.btn2 = wx.BitmapButton(self.InputPanel, id=-1, bitmap=image2,
				pos=(10, 20), size = (image2.GetWidth()+5, image2.GetHeight()+5))
		self.button2.Bind(wx.EVT_BUTTON, self.button2Click)
				
		btn1.Hide
		btn2.Hide
		btn3.Hide
		btn4.Hide
		btn5.Hide
		btn6.Hide
		btn7.Hide
		btn8.Hide
		btn9.Hide
		btn10.Hide
		btn11.Hide
		btn12.Hide
		btn13.Hide
		btn14.Hide
		btn15.Hide
		btn16.Hide
		
		btnlist = [btn1, btn2, btn3, btn4, btn5.Show, btn6.Show, btn7.Show, btn8.Show, btn9.Show, btn10.Show, btn11.Show, btn12.Show, btn13.Show, btn14.Show, btn15.Show, btn16.Show]
		for x in NumOfColours:
			btnlist[x].Show()
"""
class Outputpanel(wx.Panel):

	def __init__(self, parent):
		wx.Panel.__init__(self, parent, size=(300,500))
#	def display


#-----------Main Prog-------------
app = wx.App(False)
asdf = wx.Frame(None)
asdf.Show(True)

Start = StartFrame(None)
Game = Frame()
Input = InputPanel()
#Output = OutputPanel

Start.Show()
GameFrame.Hide()
Input.Hide()
#Output.Hide()

app.MainLoop()

