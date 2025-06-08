# Problem 4: Sort Array by Parity
# Given an integer array nums,
# write a function sort_by_parity() that moves all the even integers at the beginning of the array followed by all the odd integers.

# Return any array that satisfies this condition.

# def sort_by_parity(nums):
#     pass
# Example Usage

# nums = [3, 1, 2, 4]
# sort_by_parity(nums)

# nums = [0]
# sort_by_parity(nums)
# Example Output:

# [2, 4, 3, 1]
# [0]
# 💡 Remainders with Modulus Division
####################################################################################################################################################
#Solution
nums = [3, 1, 2, 4]
def sort_by_parity(nums):
    i,j=0,len(nums)-1
    while i < j:
        if nums[i]%2==0:
            i+=1
        elif nums[j]%2==1:
            j -=1
        else:
            nums[i],nums[j]=nums[j],nums[i]
            i+=1
            j-=1
    return nums
print(sort_by_parity(nums))

#Time Complexity: O(n)
#Space Complexity: O(1)