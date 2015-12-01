#!/usr/local/bin/python
#-*-coding: utf-8 -*-

#task_num=input("task 수를 입력하세요: ")
inputFile=open("input.txt",'w')
def inputTask():
	return task_num

def rmInput():
	task_num=input("task 수를 입력하세요: ")
	for i in range(task_num):
		print "비주기적 task일 경우 0을 입력하세요"
		period = input("task %d의 주기를 입력하세요 :" %i)
		start = input("task %d의 시작 시간을 입력하세요 :" %i)
		executionTime = input("task %d의 실행시간을 입력하세요 :" %i)
		period = str(i)+" "+str(period)+" "+str(start)+" "+str(executionTime)+" "+"\n"
		inputFile.write(str(period))

inputFile.close()

