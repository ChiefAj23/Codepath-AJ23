# Problem 1: Hunny Hunt
# Write a function linear_search() to help Winnie the Pooh locate his lost items. The function accepts a list items and a target value as parameters. The function should return the first index of target in items, and -1 if target is not in the lst. Do not use any built-in functions.

# def linear_search(lst, target):
# 	pass
# Example Usage:

# items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
# target = 'hunny'
# linear_search(items, target)

# items = ['bed', 'blue jacket', 'red shirt', 'hunny']
# target = 'red balloon'
# linear_search(items, target)
# Example Output:
# 3
# -1
###########################################################################################################################################################################################################################
#Solution

# items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
# target = 'hunny'
items = ['bed', 'blue jacket', 'red shirt', 'hunny']
target = 'red balloon'
def linear_search(lst, target):
    for i,item  in enumerate(lst):
        if item == target:
            return i
    return -1

print(linear_search(items,target))
#Time Complexity: O(n)
#Space Complexity: O(1)

