
# /*
# # Sliding Window Maximum
# # You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.
# # Return the max sliding window.
# # Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# # Output: [3,3,5,5,6,7]
# # */
from collections import deque 

def slidingwindow(nums,k):
    #base
    if k==0:
        return nums
    deq=deque()
    res=[]
    for i in range(k):
        while deq and nums[i]>nums[deq[-1]]:
            deq.pop()
        deq.append(i)
    
    res.append(nums[deq[0]])
    
    for i in range(k, len(nums)):
        if deq and deq[0]<i-k+1:
            deq.popleft()
        
        while deq and nums[i]>nums[deq[-1]]:
            deq.pop()
        
        deq.append(i)
        res.append(nums[deq[0]])
    return res
    
nums = [1,3,-1,-3,5,3,6,7]
k = 3
print(slidingwindow(nums,k))