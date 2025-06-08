# Problem 5: Container with Most Honey
# Christopher Robin is helping Pooh construct the biggest hunny jar possible.
# Help his write a function that accepts an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most honey.

# Return the maximum amount of honey a container can store.

# Notice that you may not slant the container.

# def most_honey(height):
# 	pass

# Example Usage

# height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# most_honey(height)

# height = [1, 1]
# most_honey(height)
# Example Output:

# 49
# 1
#############################################################################################################################
#Solution
height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
def most_honey(height):
    left,right=0,len(height)-1
    max_honey=0
    while left<right:
        h=min(height[left],height[right])
        w=right-left
        max_honey=max(max_honey, h*w)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max_honey

print(most_honey(height))
#Time Complexity: O(n)
#Space Complexity: O(1)