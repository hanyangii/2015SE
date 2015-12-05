import math
import os

tasks = []
result=""

class Task:
	def __init__(self,cpuId,start,period,executiontime):
		self.cpuId=cpuId
		self.period=period
		self.start=start
		self.executiontime=executiontime
		self.cur=0
	
	def __repr__(self):
		return '<{} {} {} {}>'.format(self.cpuId, self.start, self.period, self.executiontime)

def ispossible(tasks):
	task_num = len(tasks)
	print str((1/float(task_num)))
	U = float(task_num) * ((2**(1/float(task_num)))-1)
	Usum = 0
	for i in tasks:
		Usum += float(i.executiontime)/float(i.period)
	
	print str(U)+' '+str(Usum)

	if float(U)>Usum : return True
	else: return False

def save_rm(inputFile):
	outputFileName=inputFile.name.split(".")
	outputFile = open(outputFileName[0]+"_result.txt", "w")
	outputFile.write(result)
	outputFile.close()


def rm(tasks, inputFile):
	print "rm scheduling"
	tasks.sort(key=lambda Task:Task.start)
	print tasks
	working=[]
	time=0
	i=0
	curCPU=0
	startTask=0
	#outputFileName=os.path.basename(inputFile)
	if ispossible(tasks) == False :
		print 'it is impossible scheduling'
		return 

	while True:
		#print tasks[i] 
		print time
		#print tasks[i].start
		if len(working)>0 and working[0].cur == working[0].executiontime:
			working.pop(0)
		while i<len(tasks) and int(tasks[i].start) == int(time):
			working.append(tasks[i])
			startTask+=1
			i+=1
		
		if len(working)>0:
			working.sort(key=lambda Task:Task.period)
			working[0].cur+=1
			curCPU = working[0].cpuId

			result_cur=str(working[0]) + ' ' + str(curCPU)
			print result_cur
			result+=(result_cur+'\n')
		
		time+=1
		if time>200: break



def rm_scheduling(task_num, inputFile):
	print "rmrm"
#	filename = input("please write filename: ")
#	filename = str(filename)+'.txt'
#	filename = 'input.txt'
#	inputFile=open(filename,'w')

	for i in range(task_num):
		line = inputFile.readline()
		if not line: break
		line=line.split(' ')
		task=Task(line[0], line[1], line[2], line[3])
		tasks.append(task)
	
	rm(tasks, inputFile)


