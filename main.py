#-*-coding: utf-8 -*-

import wx
from scheduling import *
#import analysis
from inputTask import *
from rm import *

#num_task=inputTask()

class FirstFrame(wx.Frame):
	def __init__(self,parent,id,title):
		wx.Frame.__init__(self,parent,id,title,size=(300,300))
		panel=wx.Panel(self)
		text="Please Select Option"
		font=wx.Font(20,wx.DEFAULT,wx.MODERN,wx.NORMAL,wx.BOLD)
		st1=wx.StaticText(panel,-1,text,(30,150),style=wx.ALIGN_CENTRE)
		st1.SetFont(font)

		menubar=wx.MenuBar()
		moption = wx.Menu()
		mfile = wx.Menu()
		mfile.Append(101, '&열기','파일열기')
		mfile.Append(102, '&저장','파일저장')
		mfile.AppendSeparator()
		moption.Append(101, '&Scheduling', 'Scheduling')
		moption.Append(102, '&Analisys', 'Scheduling')
		menubar.Append(mfile,'&File')
		menubar.Append(moption,'&Option')
		self.SetMenuBar(menubar)
		self.Center()
				
class MyApp(wx.App):
	def OnInit(self):
		frame=FirstFrame(frame,-1,'frame')
		frame.Show(True)
		return True

print "Scheduling Simulator = 1, Analysis Result = 2"
operation=input("원하는 작동을 선택하세요 :")

#app=MyApp()
#app.MainLoop()

if operation == 1:
	print "1.RM, 2.EDF, 3.User Priority"
	mode = input("원하는 Scheduling mode를 입력하세요 :")
	task_num = input("number of task :")
	rm_scheduling(task_num)

elif operation ==2:
	analysis()
