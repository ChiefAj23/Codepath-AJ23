# Problem 1: Final Costs After a Supply Discount
# You are managing the budget for a global expedition, where the cost of supplies is represented by an integer array costs, where costs[i] is the cost of the ith supply item.

# There is a special discount available during the expedition. If you purchase the ith item, you will receive a discount equivalent to costs[j], where j is the minimum index such that j > i and costs[j] <= costs[i]. If no such j exists, you will not receive any discount.

# Return an integer array final_costs where final_costs[i] is the final cost you will pay for the ith supply item, considering the special discount.

# def final_supply_costs(costs):
#   pass
# Example Usage:

# print(final_supply_costs([8, 4, 6, 2, 3]))
# print(final_supply_costs([1, 2, 3, 4, 5]))
# print(final_supply_costs([10, 1, 1, 6]))
# Example Output:

# [4, 2, 4, 2, 3]
# [1, 2, 3, 4, 5]
# [9, 0, 1, 6]

##################

# U: iter1 - 8-4 = 4
#    iter2 - 4-2=  2
#    iter3 - 6-2=  4
#    iter4 - as array[j] !< array[i] == 2
#    iter5 - 3

# P: As we are finding next smaller element and processing element from left to right so stack is the best DSA for this question.

# I: Intialize the empty Stack
#    final_costs == costs.copy()
#    for i from 0 to n-1:
#        while stack is not empty AND costs[stacks tops] >=costs[i]:
#             idx =stack.pop()

#             final_costs[idx] = costs[idx] - costs[i]
#         push i onto stack
#     return final_costs

#####Solution
def final_supply_costs(costs):
    n=len(costs)
    stack = []
    final_costs = costs[:]

    for i in range(n):
        while stack and costs[stack[-1]] >=costs[i]:
            idx = stack.pop()
            final_costs[idx] =costs[idx]-costs[i]
        stack.append(i)
    return final_costs

print(final_supply_costs([8, 4, 6, 2, 3]))
print(final_supply_costs([1, 2, 3, 4, 5]))
print(final_supply_costs([10, 1, 1, 6]))

#Time Complexity: O(n)
#Space Complexity: O(n)

""""
Problem 2: Find First Symmetrical Landmark Name
During your global expedition, you encounter a series of landmarks, each represented by a string in the array landmarks. Your task is to find and return the first symmetrical landmark name. If there is no such name, return an empty string "".

A landmark name is considered symmetrical if it reads the same forward and backward.


Example Usage:

Understand:

Plan:
    1. Loop through the entire landmars array
        1) for each landmanrk check
    2.
    3.

Implement:


print(first_symmetrical_landmark(["canyon","forest","rotor","mountain"]))
print(first_symmetrical_landmark(["plateau","valley","cliff"]))
Example Output:

rotor
"""""

def first_symmetrical_landmark(landmarks):
  pass