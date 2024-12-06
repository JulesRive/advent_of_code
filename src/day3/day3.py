# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 17:52:25 2024

@author: jrive
"""

import re

with open('input.txt', 'r') as file:
    contents = file.read()

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
doPattern = r"do\(\)"
dontPattern = r"don't\(\)"

total = 0
do = True

while len(contents) > 0:
    if do:
        matchDont = re.search(dontPattern, contents)
        matchMul = re.search(pattern, contents)
        if not matchMul: # no more multiplications to do
            break
        if matchDont and matchDont.start() < matchMul.start():
            contents = contents[matchDont.end():]
            do = False
            continue
        else:
            total += int(matchMul.group(1)) * int(matchMul.group(2))
            contents = contents[matchMul.end():]
    else:
        match = re.search(doPattern, contents)
        if match:
            do = True
            contents = contents[match.end():]
        else: # disabled and no more do's
            break

            

    
print(total)