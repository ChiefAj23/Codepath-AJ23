# Problem 3: Remove Duplicates
# Write a function remove_dupes() that accepts a sorted array items, and removes the duplicates in-place such that each element appears only once.
# Return the length of the modified array. You may not create another array; your implementation must modify the original input array items.

# def remove_dupes(items):
#     pass
# Example Usage

# items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
# remove_dupes(items)

# items = ["extract of malt", "haycorns", "honey", "thistle"]
# remove_dupes(items)
# Example Output:

# 4
# 4
#################################################################################################################################################################
#Solution
items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
def remove_dupes(items):
    i=0
    while i< len(items)-1:
        if items[i] == items[i+1]:
            items.pop(i)
        else:
            i+=1
    return len(items)

print(remove_dupes(items))