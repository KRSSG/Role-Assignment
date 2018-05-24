
"""
This is a test case file
Test cases are generated using "random"
The functions in this file have the same structures as in optimal_assignment.py 
"""


from itertools import combinations
from itertools import permutations
import random

min_val = 99999
sum_of_val = 0

botL = [1,2,3,4,5]
taskD = { 't1': [], 't2': [], 't3': [] }
Mat = {}
for x in botL:
	Mat[x] = {}
	#botPos = Vector2D(state.homePos[x].x, state.homePos[x].y)
	for y in taskD.keys():
		Mat[x][y] = random.randint(1,50)#botPos.dist(taskD[y])

def decider( botL, taskD):
	no_of_bot = len(botL)
	no_of_task = len(taskD)
	# no_of_bot >= no_of_task .... inherent assumption in the STOx's paper
	# thus exhaustion is optimal as no_of_bot <= 6
	bot_Comb = list(combinations(botL, no_of_task))
	task_Comb = list(permutations(taskD.keys(), no_of_task))
	global min_val, sum_of_val
	same = []
	for x in bot_Comb:
		for y in task_Comb:
			comb = zip(x, y)
			comb.sort( key = lambda a : Mat[a[0]][a[1]] )
			print "comb: ", comb, "value: ", Mat[comb[-1][0]][comb[-1][1]]
			if min_val > Mat[comb[-1][0]][comb[-1][1]]:
				min_val = Mat[comb[-1][0]][comb[-1][1]]
				bot_comb_index = bot_Comb.index(x)
				task_comb_index = task_Comb.index(y)
				s = 0
				for t in comb:
					s = s + Mat[t[0]][t[1]]
				sum_of_val = s
			elif min_val == Mat[comb[-1][0]][comb[-1][1]]:
				s = 0
				for t in comb:
					s = s + Mat[t[0]][t[1]]
				if s < sum_of_val:
					bot_comb_index = bot_Comb.index(x)
					task_comb_index = task_Comb.index(y)
					sum_of_val = s
				print "min_sum: ", sum_of_val, "sum: ", s
			else:
				pass
	print zip( bot_Comb[bot_comb_index], task_Comb[task_comb_index] )
	
print "bot_no    weights_for_each_task"
for a in Mat:
	print a, "   : ", Mat[a]
print "\n\n"
print "COMBINATIONS                             values_of_maximum_weights_in_each_combination"
decider(botL, taskD)
print min_val
print sum_of_val
