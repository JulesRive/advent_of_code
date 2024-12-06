# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:11:14 2024

@author: jrive
"""

f = open("input.txt", "r")
array1 = []
array2 = []

for line in f:
    tokens = line.split("   ")
    array1.append(int(tokens[0]))
    array2.append(int(tokens[1]))
    
array1.sort()
array2.sort()

similarity = 0
for value in array1:
    try: 
        index = array2.index(value)
        while (array2[index] == value):
            similarity += value
            index+=1
    except:
        pass
   
        
print(similarity)