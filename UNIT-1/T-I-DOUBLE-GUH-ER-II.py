# Problem 3: T-I-Double Guh-Er II
# T-I-Double Guh-Er: That spells Tigger!
# Write a function tiggerfy() that accepts a string word
# and returns a new string that removes any substrings t, i, gg, and er from word.
# The function should be case insensitive.

# def tiggerfy(word):
# 	pass
# Example Usage:

# word = "Trigger"
# tiggerfy(word)

# word = "eggplant"
# tiggerfy(word)

# word = "Choir"
# tiggerfy(word)
# Example Output:

# "r"
# "eplan"
# "Chor"
#############################################################################################################################################################################################################################
#Solution
word = "eggplant"
def tiggerfy(word):
    result = []
    i= 0
    n=len(word)
    while i < n:
        if i+1 < n and word[i:i+2].lower()=="gg":
            i +=2
        elif i+1 < n and word[i:i+2].lower() =="er":
            i += 2
        elif word[i].lower() in ("t","i"):
            i += 1
        else:
            result.append(word[i])
            i += 1
    return "".join(result)

print(tiggerfy(word))
