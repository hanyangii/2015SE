import scheduling
import analysis
import input 

print "Scheduling Simulator = 1, Analysis Result = 2"
operation=input("원하는 작동을 선택하세요 :")

if operation == 1:
	print "1.RM, 2.EDF, 3.User Priority"
	mode = input("원하는 Scheduling mode를 입력하세요 :")
	scheduling(mode)

elif operation ==2:
	analysis()
