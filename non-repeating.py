# First Non-Repeating CharacterProblem
# Given a string s, return the index of the first non-repeating character.
# If it doesn't exist, return -1.
# Example 1
# Input:
# s = "leetcode"

# Output:
# 0
# Because 'l' appears only once.
# Example 2
# Input:
# s = "loveleetcode"

# Output:
# 2
# First unique character is 'v'.
# Example 3
# Input:
# s = "aabb"

# Output:
# -1

def firstnonrepeatingchar(s: str) -> int:
    freq={}
    for char in s:
        freq[char]=freq.get(char,0)+1
    for i, char in enumerate(s):
        if freq[char]==1:
            return i
    return -1

# Valid ParenthesesProblem
# Given a string containing only:
# '(', ')', '{', '}', '[' and ']'
# Determine if the input string is valid.
# A string is valid if:
# Every opening bracket has a matching closing bracket.
# Brackets are closed in the correct order.
# Example 1
# Input:
# s = "()"
# 
# Output:
# true
# Example 2
# Input:
# s = "()[]{}"
# 
# Output:
# true
# Example 3
# Input:
# s = "(]"
# 
# Output:
# false
# Example 4
# Input:
# s = "([)]"
# 
# Output:
def isvalid