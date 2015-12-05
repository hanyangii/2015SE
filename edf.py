import math

tasks = []

class Task:
	def __init__(self,cpuId,start, period, executiontime):
		self.cpuId=cpuId
		self.start=start
		self.period = period
		self.tmp = period
		self.executiontime=executiontime
		self.cur=0
		self.isend=False
	
	def __repr__(self):
		return '<{} {} {} {}>'.format(self.cpuId, self.start, self.period, self.executiontime)

def ispossible(tasks):
	cpuUse=0
	for i in tasks:
		cpuUse = float(i.executiontime)/float(i.period)
		
	if cpuUse<1: return True
	else: return False

def edf(tasks):
	outputFile=open("output.txt",'w')
	print "edf scheduling"
	tasks.sort(key=lambda Task:Task.start)
	print tasks
	working=[]
	time=0
	i=0
	curCPU= Task(0,0,0,0)
	startTask=0
	if ispossible(tasks) == False :
		print 'it is impossible scheduling'
		return 

	while True:
		print time

		while i<len(tasks) and int(tasks[i].start) == int(time):
			working.append(tasks[i])
			startTask+=1
			i+=1
		
		for x in working :
			if x.isend==True and x.period==time:
				x.isend=False
				x.cur=0
				x.period += x.tmp
				print 'it is' + str(x) 

		if len(working)>0:
			if curCPU.cur == curCPU.executiontime:
				curCPU.isend=True

		if len(working)>0:
			working.sort(key=lambda Task:Task.period)
			for j in working:
				if j.isend==False:
					curCPU=j
					break
			curCPU.cur+=1

			print str(curCPU) + ' ' + str(curCPU.cpuId)
			outputFile.write(str(curCPU)+'\n')
		
		time+=1
		if time > 200: break



def edf_scheduling(task_num, inputFile):
	print "edf"
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
	
	edf(tasks)


