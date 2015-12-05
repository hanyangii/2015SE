#-*-coding: utf-8

import os, sys
import wx
from wxPython.wx import *
from scheduling import *
#import analysis
from inputTask import *
from rm import *
from edf import *
from usr import *

operation =0

#GUI 
#main frame
class MainFrame(wxApp):
	def OnInit(self):
		frame=wxFrame(NULL, -1, "CPU Scheduling Simulator")
		frame.Show(False)
		self.SetTopWindow(frame)
		return true

#dialog
class AppendTaskDialog(wx.Dialog):
	def __init__(self, parent, id, title,sizer):
		wx.Dialog.__init__(self, parent, id, title, size=sizer)

		start_sizer=wx.BoxSizer(wx.HORIZONTAL)
		start_lbl=wx.StaticText(self, label='Start time:')
		start_sizer.Add(start_lbl, 0, wx.ALL|wx.CENTER,5)
		self.start=wx.TextCtrl(self)
		start_sizer.Add(self.start, 0, wx.ALL, 5)

		period_sizer=wx.BoxSizer(wx.HORIZONTAL)
		period_lbl=wx.StaticText(self, label='Period:')
		period_sizer.Add(period_lbl, 0, wx.ALL|wx.CENTER,5)
		self.period=wx.TextCtrl(self)
		period_sizer.Add(self.period, 0, wx.ALL, 5)

		execute_sizer=wx.BoxSizer(wx.HORIZONTAL)
		execute_lbl=wx.StaticText(self, label='Execute time:')
		execute_sizer.Add(execute_lbl, 0, wx.ALL|wx.CENTER,5)
		self.execute=wx.TextCtrl(self)
		execute_sizer.Add(self.execute, 0, wx.ALL, 5)
		
		sizer=wx.BoxSizer(wx.VERTICAL)
		sizer = self.CreateTextSizer('Please Append Task for Scheduling')
		sizer.Add(wx.Button(self, 22, 'Append'), 0, wx.ALL, 5)
		sizer.Add(start_sizer, 0, wx.ALL, 5)
		sizer.Add(period_sizer, 0, wx.ALL, 5)	
		sizer.Add(execute_sizer, 0, wx.ALL, 5)
		self.SetSizer(sizer)
		

		self.Bind(wx.EVT_BUTTON, self.Append, id=22)
	
	def Append(self, event):
		start = self.start.GetValue()
		period = self.period.GetValue()
		execute = self.execute.GetValue()
		
		self.start = str(start)+" "+str(period)+" "+str(execute)
		
		self.Close()

#dialog
class AppendUSRTaskDialog(wx.Dialog):
	def __init__(self, parent, id, title,sizer):
		wx.Dialog.__init__(self, parent, id, title, size=sizer)

		start_sizer=wx.BoxSizer(wx.HORIZONTAL)
		start_lbl=wx.StaticText(self, label='Start time:')
		start_sizer.Add(start_lbl, 0, wx.ALL|wx.CENTER,5)
		self.start=wx.TextCtrl(self)
		start_sizer.Add(self.start, 0, wx.ALL, 5)

		period_sizer=wx.BoxSizer(wx.HORIZONTAL)
		period_lbl=wx.StaticText(self, label='Period:')
		period_sizer.Add(period_lbl, 0, wx.ALL|wx.CENTER,5)
		self.period=wx.TextCtrl(self)
		period_sizer.Add(self.period, 0, wx.ALL, 5)

		execute_sizer=wx.BoxSizer(wx.HORIZONTAL)
		execute_lbl=wx.StaticText(self, label='Execute time:')
		execute_sizer.Add(execute_lbl, 0, wx.ALL|wx.CENTER,5)
		self.execute=wx.TextCtrl(self)
		execute_sizer.Add(self.execute, 0, wx.ALL, 5)

		priority_sizer=wx.BoxSizer(wx.HORIZONTAL)
		priority_lbl=wx.StaticText(self, label='User Priority:')
		priority_sizer.Add(priority_lbl, 0, wx.ALL|wx.CENTER,5)
		self.priority=wx.TextCtrl(self)
		priority_sizer.Add(self.priority, 0, wx.ALL, 5)
		
		sizer=wx.BoxSizer(wx.VERTICAL)
		sizer = self.CreateTextSizer('Please Append Task for Scheduling')
		sizer.Add(wx.Button(self, 22, 'Append'), 0, wx.ALL, 5)
		sizer.Add(start_sizer, 0, wx.ALL, 5)
		sizer.Add(period_sizer, 0, wx.ALL, 5)	
		sizer.Add(execute_sizer, 0, wx.ALL, 5)
		sizer.Add(priority_sizer, 0, wx.ALL, 5)
		self.SetSizer(sizer)
		

		self.Bind(wx.EVT_BUTTON, self.Append, id=22)
	
	def Append(self, event):
		start = self.start.GetValue()
		period = self.period.GetValue()
		execute = self.execute.GetValue()
		priority = self.priority.GetValue()
		
		self.start = str(start)+" "+str(period)+" "+str(execute)+" "+str(priority)
		
		self.Close()



#edit component
class MainWindow(wxFrame):
	


	def OnOpen(self, e):
		dlg=wxFileDialog(self, "Open a inputfile", os.getcwd(),"","*.*",wxOPEN)
		if dlg.ShowModal()==wxID_OK:
			path = dlg.GetPath()
			self.mypath = os.path.basename(path)
			self.inputfile=open(self.mypath,"w")
			self.readfile=open(self.mypath, "r")
			#print mypath
			#self.control.SetValue(f.read())
			self.SetStatusText("Selected input file : %s" %self.mypath)
			#f.close()
		dlg.Destroy()

	def OnScroll(self,event):
		y=evt.GetPosition()
		self.st.SetLabel(str(y))

	def AppendTask(self, event):
		#print self.f
	 	dia=AppendTaskDialog(self, 1, 'Append Task', (300,300))
		#print str(dia.start.GetValue())
		dia.ShowModal()
		dia.start = str(self.curnum)+ " " + dia.start
		#print str(self.curnum)
		self.listbox.Append(dia.start)
		self.curnum+=1
		dia.Destroy()

	def AppendUSRTask(self, event):
		#print self.f
	 	dia=AppendUSRTaskDialog(self, 1, 'Append Task', (300,300))
		#print str(dia.start.GetValue())
		dia.ShowModal()
		dia.start = str(self.curnum)+ " " + dia.start
		#print str(self.curnum)
		self.listbox.Append(dia.start)
		self.curnum+=1
		dia.Destroy()
	
	def StartRM(self, event):
		for i in range(self.listbox.GetCount()):
			tmp = self.listbox.GetString(i)
			print tmp
			tmp += " \n"
			self.inputfile.write(tmp)
		self.inputfile.close()
		rm_scheduling(self.listbox.GetCount(), self.readfile)

	def StartEDF(self, event):
		for i in range(self.listbox.GetCount()):
			tmp = self.listbox.GetString(i)
			print tmp
			tmp += " \n"
			self.inputfile.write(tmp)
		self.inputfile.close()
		edf_scheduling(self.listbox.GetCount(), self.readfile)

	def StartUSR(self, event):
		for i in range(self.listbox.GetCount()):
			tmp = self.listbox.GetString(i)
			print tmp
			tmp += " \n"
			self.inputfile.write(tmp)
		self.inputfile.close()
		usr_scheduling(self.listbox.GetCount(), self.readfile)
	
	def SaveRMResult(self,event):
		save_rm(self.readfile)

	def RM(self, event):	
		
		#panel=wx.Panel(self, -1)
		self.curnum=0
		self.mypath="None"
		
		self.SetStatusText("Selected input file : None")
		btn=wx.Button(self, 1, 'Append Task',(20,20))

		self.listbox=wx.ListBox(self, -1, (25,100),(200,300))
		self.listbox.Bind(wx.EVT_SCROLLWIN,self.OnScroll)
		self.listbox.SetScrollbar(wx.VERTICAL, 0,6,50)
		self.listbox.Clear()
		
		wx.Button(self, 2, 'Start RM', (20, 420))
		wx.Button(self, 3, 'Save Result', (60, 420))

		self.Bind(wx.EVT_MENU, self.OnOpen, id=101)
		self.Bind(wx.EVT_BUTTON,self.AppendTask, id=1)
		self.Bind(wx.EVT_BUTTON,self.StartRM, id=2)
		self.Bind(wx.EVT_BUTTON,self.SaveRMResult, id=3)

	def EDF(self, event):	
		
		#panel=wx.Panel(self, -1)
		self.curnum=0
		self.mypath="None"
		
		self.SetStatusText("Selected input file : None")
		btn=wx.Button(self, 1, 'Append Task',(20,20))

		self.listbox=wx.ListBox(self, -1, (25,100),(200,300))
		self.listbox.Bind(wx.EVT_SCROLLWIN,self.OnScroll)
		self.listbox.SetScrollbar(wx.VERTICAL, 0,6,50)
		self.listbox.Clear()
		
		wx.Button(self, 2, 'Start EDF', (20, 420))

		self.Bind(wx.EVT_MENU, self.OnOpen, id=101)
		self.Bind(wx.EVT_BUTTON,self.AppendTask, id=1)
		self.Bind(wx.EVT_BUTTON,self.StartEDF, id=2)

	def USR(self, event):	
		
		#panel=wx.Panel(self, -1)
		self.curnum=0
		self.mypath="None"
		
		self.SetStatusText("Selected input file : None")
		btn=wx.Button(self, 1, 'Append Task',(20,20))

		self.listbox=wx.ListBox(self, -1, (25,100),(200,300))
		self.listbox.Bind(wx.EVT_SCROLLWIN,self.OnScroll)
		self.listbox.SetScrollbar(wx.VERTICAL, 0,6,50)
		self.listbox.Clear()
		
		wx.Button(self, 2, 'Start USR Priority', (20, 420))

		self.Bind(wx.EVT_MENU, self.OnOpen, id=101)
		self.Bind(wx.EVT_BUTTON,self.AppendUSRTask, id=1)
		self.Bind(wx.EVT_BUTTON,self.StartUSR, id=2)

	def __init__(self,parent,id, title):
		wxFrame.__init__(self,parent,-4,title,size=(500,500),
						 style=wxDEFAULT_FRAME_STYLE|wxNO_FULL_REPAINT_ON_RESIZE)
		#self.control=wxTextCtrl(self,1,style=wxTE_MULTILINE)
		self.CreateStatusBar()

		optionmenu = wxMenu()
		optionmenu.Append(301, "&RM", "RM")
		optionmenu.AppendSeparator()
		optionmenu.Append(310, "&EDF", "EDF")
		optionmenu.AppendSeparator()
		optionmenu.Append(311, "&User Priority", "User Priority")

		filemenu1 = wxMenu()
		filemenu1.Append(101, "&Open", "Open")
		filemenu1.AppendSeparator()
		filemenu1.Append(110, "&Save", "Save")
		
		analysismenu = wxMenu()
		analysismenu.Append(401, "&Graph", "Graph")
		analysismenu.AppendSeparator()
		analysismenu.Append(410, "&Calculate", "Calculate")

		filemenu2 = wxMenu()
		filemenu2.AppendMenu(201, "&Scheduling", optionmenu)
		filemenu2.AppendSeparator()
		filemenu2.AppendMenu(210, "&Analysis", analysismenu)

		menuBar = wxMenuBar()
		menuBar.Append(filemenu1, "&File")
		menuBar.Append(filemenu2, "&Option")
		self.SetMenuBar(menuBar)
		
		#d = wxMessageDialog(self, "샘플 프로그램\n"
		                          #"Made in wxPython",     
								          #EVT_MENU(self, 110, self.OnSave)

								  #"이 프로그램에 대여", wxOK|wxICON_INFORMATION)

		#d.ShowModal()
		#d.Destroy()

		#self.Bind(wx.EVT_MENU, self.OnOpen, id=101)
		self.Bind(wx.EVT_MENU, self.RM, id=301)
		self.Bind(wx.EVT_MENU, self.EDF, id=310)
		self.Bind(wx.EVT_MENU, self.USR, id=311)
		#EVT_MENU(self, 110, self.OnSave)

		self.Show(true)

app=wxPySimpleApp()
frame=MainWindow(None, -1, "CPU Scheduling Simulator")
frame.Show(1)
app.MainLoop()


