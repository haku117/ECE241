
"""
UMass ECE 241 - Advanced Programming
Homework #2     Fall 2018
question5.py - 3 way merge sort

"""


## This is an example of code to merge two lists in a descending order
## You can directly call this function or write your own one

# The two lists "lefthalf" and "righthalf" are start from i and j
# The destination list "alist" start from the given position "pos"
# The function returns the number of comparisons during merge
def merge2List(alist, lefthalf, righthalf, i, j, pos):

    comparison = 0 # initial the comparison number as 0
    while i < len(lefthalf) and j < len(righthalf): 
        if lefthalf[i] < righthalf[j]:
            alist[pos] = righthalf[j]
            j += 1
        else:
            alist[pos] = lefthalf[i]
            i += 1
        comparison += 1
        pos += 1

    while i < len(lefthalf): # add the remained numbers in the lefthalf to alist
        alist[pos] = lefthalf[i]
        i = i + 1
        pos += 1

    while j < len(righthalf): # add the remained numbers in the righthalf to alist
        alist[pos]=righthalf[j]
        j=j+1
        pos += 1

    return comparison



## Implement 3 way merge sorting algorithm
## It takes a given list "alist" and return the number of comparison used 
def mergeSort_3_way(alist):

    comparison = 0

    #
    # Write your code here
    #

    return comparison




