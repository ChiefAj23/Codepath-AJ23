# Problem 2: Bouncy, Flouncy, Trouncy, Pouncy
# Tigger has developed a new programming language Tiger with only four operations and one variable tigger.

# bouncy and flouncy both increment the value of the variable tigger by 1.
# trouncy and pouncy both decrement the value of the variable tigger by 1.
# Initially, the value of tigger is 1 because he's the only tigger around! Given a list of strings operations containing a list of operations, return the final value of tigger after performing all the operations.

# def final_value_after_operations(operations):
# 	pass
# Example Usage:

# operations = ["trouncy", "flouncy", "flouncy"]
# final_value_after_operations(operations)

# operations = ["bouncy", "bouncy", "flouncy"]
# final_value_after_operations(operations)
# Example Output:

# 2
# 4
###########################################################################################################################################################################################################################
#Solution

# operations = ["trouncy", "flouncy", "flouncy"]
# operations = ["bouncy", "bouncy", "flouncy"]
#operations = [] #edge case
def final_value_after_operations(operations):
	tigger=1
	for i,item in enumerate(operations):
		if item=="bouncy" or item=="flouncy":
			tigger+=1
		elif item=="trouncy" or item=="pouncy":
			tigger-=1
	return tigger

print(final_value_after_operations(operations))
#Time Complexity: O(n)
#Space Complexity: O(1)
# Example Usage: