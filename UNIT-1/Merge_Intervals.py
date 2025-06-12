# Problem 6: Merge Intervals
# Write a function merge_intervals() that accepts an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

# def merge_intervals(intervals):
# 	pass
# Example Usage

# intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
# merge_intervals(intervals)

# intervals = [[1, 4], [4, 5]]
# merge_intervals(intervals)
# Example Output:

# [[1, 6], [8, 10], [15, 18]]
# [[1, 5]]
###################################################################################################

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    for current in intervals[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
    return merged

print(merge_intervals(intervals))

#Time Complexity: O(n log n)
#Space Complexity: O(n)