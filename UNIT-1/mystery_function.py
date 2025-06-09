# What is the output of the function code snippet?

def mystery_function(word):
    start=0
    end=len(word)-1
    while start < end:
        if word[start] != word[end]:
            return False
        start += 1
        end -= 1
    return True

word ="kayak"
print(mystery_function(word))
# Output: True

# What is the output of the function code snippet?

def mystery_function(nums):
    count = 0
    max_count = 0
    for i in range(len(nums)):
        if nums[i] > 0:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    return max_count

result = mystery_function([1, 2, -3, 4, 5, -6, 7, 8, 9])
print(result)
# Output: 3
