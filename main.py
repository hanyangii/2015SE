#-*-coding: utf-8

import wx
from wxPython.wx import *
from scheduling import *
#import analysis
from inputTask import *
from rm import *
from edf import *
from usr import *


#GUI 
#main frame
class MainFrame(wxApp):
	def OnInit(self):
		frame=wxFrame(NULL, -1, "CPU Scheduling Simulator")
		frame.Show(False)
		self.SetTopWindow(frame)
		return true

#edit component
class MainWindow(wxFrame):
	

	def OnOpen(self, e):
		dlg=wxFileDialog(self, "Choose a file", self.dirname, "", "*.*", wxOPEN)
		if dlg.ShowModal() == wxID_OK:
			self.filename=dlg.GetFilename()
			self.dirname=dlg.GetDirectory()
			f=open(self.dirname+"/"+self.filenae, "r")
			self.control.SetValue(f.read())
			f.close()
		dlg.Destroy()


	def OnSave(self, e):
		dlg=wxFileDialog(self, "Save a file", self.dirname,"","*.*",wxOPEN)
		dlg.ShowModal()
		if dlg.ShowModal()==wxID_OK:
			self.filename=dlg.GetFilenam()
			self.dirname=dlg.GetDirectory()
			f=open(self.dirname+"/"+self.filename,"w")
			f.write(self.control.GetValue())
			f.close
		dlg.Destroy()



	def __init__(self,parent,id, title):
		wxFrame.__init__(self,parent,-4,title,size=(200, 100),
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
								  
								  #"이 프로그램에 대여", wxOK|wxICON_INFORMATION)

		#d.ShowModal()
		#d.Destroy()

		EVT_MENU(self, 101, self.OnOpen)
		EVT_MENU(self, 110, self.OnSave)
		
		self.Show(true)

app=wxPySimpleApp()
frame=MainWindow(None, -1, "CPU Scheduling Simulator")
frame.Show(1)
app.MainLoop()

#num_task=inputTask()
print "Scheduling Simulator = 1, Analysis Result = 2"
operation=input("원하는 작동을 선택하세요 :")


if operation == 1:
	print "1.RM, 2.EDF, 3.User Priority"
	mode = input("원하는 Scheduling mode를 입력하세요 :")
	task_num = input("number of task :")
	if mode ==1:
		rm_scheduling(task_num)
	elif mode==2:
		edf_scheduling(task_num)
	elif mode==3:
		usr_scheduling(task_num)

elif operation ==2:
	analysis()
