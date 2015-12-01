#-*-coding: utf-8 -*-

#task generation and scheduling

from rm import *

tasks=[]

class Task:
	def __init__(self,period,start,deadline):
		self.period=period
		self.start=start
		self.deadline=deadline

	def __repr__(self):
		return '<{} {} {}>'.format(self.period, self.start, self.deadline)

def makeTaskClass():
	taskFile=open("input.txt","r")
	i=0
	while True:
		line = taskFile.readline()
		if not line: break
		line=line.split(' ')
		task=Task(line[1],line[2],line[3])
		tasks.append(task)
		i+=1
	taskFile.close()

def getKey(Task):
	return Task.start

def scheduling(mode,num_task):
	makeTaskClass()
	print tasks
	tasks.sort(key=lambda Task:Task.start)
	print '--------------------------------------------------'
#				irint str(i) + '--------------'
	print tasks
	if mode==1: #RM
		rm(tasks)
	elif mode==2: #EDF
		edf()
	elif mode==3: #user priority
		usrPriority()
	else: #wrong input
		print "잘못된 입력값입니다."
