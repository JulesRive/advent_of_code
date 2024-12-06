# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:52:25 2024

@author: jrive
"""

def isSafeWithDampener(array):
    if isSafe(line):
        return True
    
    for index in range(len(array)):
        if isSafe(array[:index] + array[index+1:]):
            return True
        
    return False
    
    
def isSafe(array):
    diffs = [array[index+1] - array[index] for index in range(len(array)-1)]
    
    decreasing = all(diff < 0 for diff in diffs)
    increasing = all(diff > 0 for diff in diffs)

    valid_diffs = all(1<=abs(diff)<=3 for diff in diffs)    
    
    return valid_diffs and (decreasing or increasing)
    
f = open("day2_input.txt", "r")
inputData = []

for line in f:
    tokens = line.split(" ")
    for index in range(len(tokens)):
        tokens[index] = int(tokens[index])
    inputData.append(tokens)



totalSafes = 0
unsafe = 0
for line in inputData:
    if isSafeWithDampener(line):
        totalSafes+=1

print(totalSafes)