import math

tasks = []

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

def rm(tasks):
	print "rm scheduling"
	tasks.sort(key=lambda Task:Task.start)
	print tasks
	working=[]
	time=0
	i=0
	curCPU=0
	startTask=0
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

			print str(working[0]) + ' ' + str(curCPU)
		
		time+=1
		if len(working)==0 and startTask==len(tasks): break



def rm_scheduling(task_num):
	print "rmrm"
#	filename = input("please write filename: ")
#	filename = str(filename)+'.txt'
	filename = 'input.txt'
	inputFile=open(filename,'w')

	for i in range(task_num):
		start = input("start %d: " %i)
		period = input("period %d :" %i)
		executiontime = input("execution time %d: " %i)
		
		tasks.append(Task(i,start,period,executiontime))
		start = str(i)+" "+str(start)+" "+str(period)+" "+str(executiontime)+" "+"\n"
		inputFile.write(str(start))
	inputFile.close()
	rm(tasks)


