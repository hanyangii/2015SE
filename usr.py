import math

tasks = []

class Task:
	def __init__(self,cpuId,start,period, executiontime, priority):
		self.cpuId=cpuId
		self.start=start
		self.period=period
		self.deadline=period
		self.executiontime=executiontime
		self.priority=priority
		self.isend=False
		self.cur=0
	
	def __repr__(self):
		return '<{} {} {} {}>'.format(self.cpuId, self.start, self.period, self.priority)

def ispossible(tasks):
	return True

def user(tasks):
	print "usr scheduling"
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
		
		if len(working)>0:
			if curCPU.executiontime == curCPU.cur:
				curCPU.isend=True
				curCPU.cur=0
		
		while i<len(tasks) and int(tasks[i].start) == int(time):
			working.append(tasks[i])
			startTask+=1
			i+=1
		
		if len(working)>0:
			for j in working:
				if j.deadline== time:
					j.deadline+=j.period
					j.isend=False
					
			working.sort(key=lambda Task:Task.priority)
			
			for k in working:
				if k.isend==False:
					curCPU=k
					break

			print str(curCPU) + ' ' + str(curCPU.cpuId)
		
		time+=1
		if time > 20: break



def usr_scheduling(task_num, inputFile):
	print "usrusr"
#	filename = input("please write filename: ")
#	filename = str(filename)+'.txt'
#	filename = 'input.txt'
#	inputFile=open(filename,'w')

	for i in range(task_num):
		line = inputFile.readline()
		if not line: break
		line=line.split(' ')
		task=Task(line[0], line[1], line[2], line[3], line[4])
		tasks.append(task)
	
	user(tasks)

