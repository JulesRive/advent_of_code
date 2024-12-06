# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 20:25:07 2024

@author: jrive
"""


# Correctly ordered = follows every rule

class Rule:
    def __init__(self, first, second):
        self.first = first
        self.second = second

def OrderUpdate(update, rules):
    brokeRule = True
    while brokeRule:
        brokeRule = False
        for index in range(len(update)):
            page = update[index]
            for rule in rules: # If page is part of a rule and breaks it, swap the pages
                if page == rule.first:
                    try:
                        secondIndex = update.index(rule.second)
                        if secondIndex < index:
                            brokeRule = True
                            tmp = update[index]
                            update[index] = update[secondIndex]
                            update[secondIndex] = tmp
                    except:
                        pass
    return update[int(len(update)/2)] 
                    
def CheckUpdateWorks(update, rules):
    for index in range(len(update)):
        page = update[index]
        for rule in rules: # If page is part of a rule and breaks it, return false
            if page == rule.first:
                try:
                    secondIndex = update.index(rule.second)
                    if secondIndex < index:
                        print(f"Update {update} breaks rule {rule.first}|{rule.second}")
                        return OrderUpdate(update, rules)
                except:
                    pass              
    return 0
    #return update[int(len(update)/2)]            

rules = []
updates = []
f = open("input.txt", "r")
for line in f:
    values = line.split('|')
    if len(values) == 2:
        rules.append(Rule(int(values[0]), int(values[1])))
        continue
    values = line.split(',')
    if len(values) >= 2:
        update = []
        for value in values:
            update.append(int(value))
        updates.append(update)

total = 0
for update in updates:
    total += CheckUpdateWorks(update, rules)

print(total)