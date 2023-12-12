#  Given an integer array arr, find the contiguous subarray (containing at least one number) which
# has the largest sum and returns its sum and prints the subarray.

# Examples
# Example 1:

# Input: arr = [-2,1,-3,4,-1,2,1,-5,4] 

# Output: 6 

# Explanation: [4,-1,2,1] has the largest sum = 6. 

# Examples 2: 

# Input: arr = [1] 

# Output: 1 

# Explanation: Array has only one element and which is giving positive sum of 1.

import sys

def kadane(arr)->int:
    sum=0
    maxi = -sys.maxsize - 1
    for i in range(len(arr)):
        sum += arr[i]
        maxi =  max(maxi,sum)
        if sum <0:
            sum = 0    
    return maxi

if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    maxSum = kadane(arr)
    print("The maximum subarray sum is:", maxSum)