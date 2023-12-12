# A new hashing approach that takes in the original string and a seed number. engnineers decided that the sed can be a generated from the same input string by counting the number of times a reverse of a substring of length k makes the new string lexicographically smaller. you are deployed with the task of developing a service that takes in a string s and an integer k, and returns the number of ways to reverse the substring of length k such that the resulting string is lexicographically smaller than the original string. 
# Notes:
# -a substring is a contiguous sequence of characters within a string. For example , the string "zon" is a substring of "amazon","zone",etc. but is not a substring of "aoin","zozo",etc.
# -a string "a" is lexicographically smaller than string "b" if a[i]<b[i] at the first index where a and b differ. For example, "amazon" is lexicographically smaller than "amazan".

# Example:
# s="amazon"
# k=3
# Consider all substrings of length k = 3. These are the possible ways to perform the given operation are:
# - Reverse the substring "ama" , results in "amazon", thus lexicographically equal, thus unsuccessful
# - Reverse the substring "maz" , results in " azamon", lexicographically greater, thus unsuccessful
# -Reverse the substring "azo", results in "amozan", lexicographically greater, thus unsuccessful
# -Reverse the substring "zon", results in "amanoz", lexicographically smaller, thus successful
# Only one way is possible, so return 1.

# Function Description:
# Complete the function countNumWays 
# countNumWays  has the following parameters:
# string s: the original string
# int k: the algorithm parameter

# Returns:
# int: the number of possible ways to perform the operation ensuring the given constraint

# Constraints:
# 2<= |s| <= 10^6
# 1<= k <= min(|s|,20)

def countNumWays(s, k):
    n = len(s)
    result = 0
    
    # Helper function to check if a substring is lexicographically smaller
    def is_smaller(sub):
        rev_sub = sub[::-1]
        return rev_sub < sub
    
    # Iterate through all substrings of length k
    for i in range(n - k + 1):
        substring = s[i:i + k]
        
        # Check if reversing the substring makes the string lexicographically smaller
        if is_smaller(substring):
            result += 1
    
    return result

# Example usage
s = "amazon"
k = 3
print(countNumWays(s, k))
