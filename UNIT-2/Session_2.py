# Problem 1: Balanced Art Collection
# As the curator of an art gallery, you are organizing a new exhibition.
# You must ensure the collection of art pieces are balanced to attract the right range of buyers.
# A balanced collection is one where the difference between the maximum and minimum value of the art pieces is exactly 1.

# Given an integer array art_pieces representing the value of each art piece, write a function find_balanced_subsequence() that returns the length of the longest balanced subsequence.

# A subsequence is a sequence derived from the array by deleting some or no elements without changing the order of the remaining elements.

# def find_balanced_subsequence(art_pieces):
#     pass
# Example Usage:

# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces2 = [1,2,3,4]
# art_pieces3 = [1,1,1,1]

# print(find_balanced_subsequence(art_pieces1))
# print(find_balanced_subsequence(art_pieces2))
# print(find_balanced_subsequence(art_pieces3))
# Example Output:

# 5
# Example 1 Explanation:  The longest balanced subsequence is [3,2,2,2,3].

# 2
# 0

'''

'''
# def find_balanced_subsequence(art_pieces):
#     freq = {}
#     for i in art_pieces:
#         freq[i] = freq.get(i, 0) + 1

#     print(freq)
#     max_sub=0
#     for j in freq:
#         if j+1 in freq:
#             max_sub = max(max_sub,freq[j]+freq[j+1])
#     return max_sub

# art_pieces1 = [1,3,2,2,5,2,3,7]
# art_pieces2 = [1,2,3,4]
# print(find_balanced_subsequence(art_pieces2))
#Time Complexity: O(n)
#Space Complexity: O(n)

# Problem 2: Verifying Authenticity
# Your art gallery has just been shipped a new collection of numbered art pieces, and you need to verify their authenticity.
# The collection is considered "authentic" if it is a permutation of an array base[n].

# The base[n] array is defined as [1, 2, ..., n - 1, n, n], meaning it is an array of length n + 1 containing the integers from 1 to n - 1 exactly once, and the integer n twice. For example, base[1] is [1, 1] and base[3] is [1, 2, 3, 3].

# Write a function is_authentic_collection that accepts an array of integers art_pieces and returns True if the given array is an authentic array, and otherwise returns False.

# Note: A permutation of integers represents an arrangement of these numbers. For example [3, 2, 1] and [2, 1, 3] are both permutations of the series of numbers 1, 2, and 3.

# def is_authentic_collection(art_pieces):
#     pass
# Example Usage:

# collection1 = [2, 1, 3]
# collection2 = [1, 3, 3, 2]
# collection3 = [1, 1]

# print(is_authentic_collection(collection1))
# print(is_authentic_collection(collection2))
# print(is_authentic_collection(collection3))
# Example Output:

# False
# Example 1 Explanation: Since the maximum element of the array is 3, the only
# candidate n for which this array could be a permutation of base[n], is n = 3.
# However, base[3] has four elements but array collection1 has three. Therefore,
# it can not be a permutation of base[3] = [1, 2, 3, 3]. So the answer is false.

# True
# Example 2 Explanation:  Since the maximum element of the array is 3, the only
# candidate n for which this array could be a permutation of base[n], is n = 3.
# It can be seen that collection2 is a permutation of base[3] = [1, 2, 3, 3]
# (by swapping the second and fourth elements in nums, we reach base[3]).
#  Therefore, the answer is true.

# True
# Example 3 Explanation; Since the maximum element of the array is 1,
# the only candidate n for which this array could be a permutation of base[n],
# is n = 1. It can be seen that collection3 is a permutation of base[1] = [1, 1].
#  Therefore, the answer is true.

# def is_authentic_collection(art_pieces):
#     freq = {}
#     #print(freq)
#     for i in art_pieces:
#         freq[i] = freq.get(i, 0) + 1
#     # max1 = max(freq, key=freq.get)
#     max1 = max(freq.keys())
#     # print(freq)
#     for j in range(1, max1):
#         if freq.get(j) != 1:
#             return False
#     if freq.get(max1) != 2:
#         return False
#     return True

# collection1 = [2, 1, 3]
# collection2 = [1, 3, 3, 2]
# collection3 = [1, 1]

# print(is_authentic_collection(collection1)) # False
# print(is_authentic_collection(collection2)) # True
# print(is_authentic_collection(collection3)) # True

# ''''''
# Authentic array = [1, 2, n-1, n, n] last number appears twice
# freq = {}
#     for i in art_pieces:
#         freq[i] = freq.get(i, 0) + 1
# ''''''

# Problem 3
# Problem 3: Gallery Wall
# You are tasked with organizing a collection of art prints represented by a list of strings collection.
#  You need to display these prints on a single wall in a 2D array format that meets the following criteria:

# The 2D array should contain only the elements of the array collection.
# Each row in the 2D array should contain distinct strings.
# The number of rows in the 2D array should be minimal.
# Return the resulting array. If there are multiple answers, return any of them.
# Note that the 2D array can have a different number of elements on each row.

# def organize_exhibition(collection):
#     pass
# Example Usage:

# collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol",
#               "Kahlo", "O'Keefe"]
# collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

# print(organize_exhibition(collection1))
# print(organize_exhibition(collection2))
# Example Output:

# [
#   ["O'Keefe", "Kahlo", "Picasso", "Warhol"],
#   ["O'Keefe", "Kahlo"],
#   ["O'Keefe"]
# ]
# Example 1 Explanation:
# All elements of collections were used, and each row of the 2D array contains
# distinct strings, so it is a valid answer.
# It can be shown that we cannot have less than 3 rows in a valid array.

# [["Kusama", "Monet", "Ofili", "Banksy"]]
# Example 2 Explanation:
# All elements of the array are distinct, so we can keep all of them in the first
# row of the 2D array.


def organize_exhibition(collection):
    pass

# Example Usage:

collection1 = ["O'Keefe", "Kahlo", "Picasso", "O'Keefe", "Warhol",
              "Kahlo", "O'Keefe"]
collection2 = ["Kusama", "Monet", "Ofili", "Banksy"]

print(organize_exhibition(collection1))
print(organize_exhibition(collection2))