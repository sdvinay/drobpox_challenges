#!/usr/bin/python

# http://www.dropbox.com/jobs/challenges#the-dropbox-diet

# This program doesn't meet the interface of the challenge, but is instead a more generalized interface (that can choose subsets of the data input, run many iterations, etc).  It would be trivial to write a wrapper script around this to meet the interface for the challenge.

# We'll get a list of activities with caloric impact on stdin (some are food, with positive calories; some are exercise, with negative calories.  Doesn't matter).  Need to find a set of them that sums to zero.  


import sys
import random

# this function yields subsets of activities that sum to 0
# takes a list of caloric impacts
# yields sets, each set denoted by an integer bitmask
def matchGenerator(activityCalories) : 
	numItems = len(activityCalories)
	for i in range(2, 2**numItems):
		calTotal = sum (map (lambda digit: ((2**digit)&i) and activityCalories[digit], range(0, numItems)))
		if calTotal == 0:
			yield i

# given a bitmask and a set of names, print the matching names
def printActivitiesFromBitset(bitSetNum, activityNames) :
	numItems = len(activityNames)
	for digit in range(0, numItems):
		mask = 2**digit
		if (mask & bitSetNum): print activityNames[digit]

# run an iteration, given a dataset (lines) and number of those lines to use
# randomizes the input set, and picks the correct number of lines
# finds one set that zeroes out, and prints the bitset for that set
def doIteration (lines, numItems) :
	activityNames = dict()
	activityCalories = dict()

	random.shuffle(lines)

# the following line sorts the items by absolute value of calories
# comment/uncomment it to disable/enable sorting
	lines = sorted(lines[0:numItems], key=lambda line: abs(int(line.split(" ")[1])))

	for i in range (0, numItems):
		line = lines[i]
		(name, dummy, calories) = line.partition(" ")
		activityNames[i] = name
		activityCalories[i] = int(calories)

	matches = matchGenerator(activityCalories)
	try:
		firstMatch = matches.next()
		if firstMatch>0: 
			print firstMatch
			#printActivitiesFromBitset(numItems, match, activityNames)
	except StopIteration:
		pass



#numItems = int(sys.stdin.readline())
numItems = int(sys.argv[1])
numIterations = int(sys.argv[2])

lines = sys.stdin.readlines()

for iter in range (0, numIterations) : 
	doIteration(lines, numItems)

#print activityNames
#print activityCalories





