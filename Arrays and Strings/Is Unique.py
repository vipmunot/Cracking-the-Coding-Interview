# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?

def uniquechars(string):
    return len(set(string)) == len(string)
    
# without using additional data structures
def uniquechars_no_structures(string):
    for char in string:
        if string.count(char) > 1: return False
        else:
             return True
print('\nUnqiue: ',uniquechars('abcd'))
print('\nUnqiue w/o Data Structures: ',uniquechars_no_structures('abcd'))
print('\nUnqiue: ',uniquechars('abcdaa'))
print('\nUnqiue w/o Data Structures: ',uniquechars_no_structures('abcaad'))
              