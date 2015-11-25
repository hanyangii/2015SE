#!/usr/local/bin/python
#-*-coding: utf-8 -*-

task_num=input("task 수를 입력하세요: ")
inputFile=open("input.txt",'w')

for i in range(task_num):
	print "비주기적 task일 경우 0을 입력하세요"
	period = input("task %d의 주기를 입력하세요 :" %i)
	period = str(i)+" "+str(period)+"\n"
	inputFile.write(str(period))

inputFile.close()

