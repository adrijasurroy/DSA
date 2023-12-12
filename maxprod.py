# Problem Statement: Given an array that contains both negative and positive integers, find the maximum product subarray.

# Examples
# Example 1:
# Input:
#  Nums = [1,2,3,4,5,0]
# Output:
#  120
# Explanation:
#  In the given array, we can see 1×2×3×4×5 gives maximum product value.


# Example 2:
# Input:
#  Nums = [1,2,-3,0,-4,-5]
# Output:
#  20
# Explanation:
#  In the given array, we can see (-4)×(-5) gives maximum product value.

def max_prod(arr)->int:
    pre,suff=1,1
    product=float("-inf")
    n=len(arr)
    for i in range(n):
        if pre == 0:
            pre=1
        if suff == 0:
            suff =1
        pre *=arr[i]
        suff *= arr[n-i-1]
        product = max(product, max(pre,suff))
    
    return product

arr = [1, 2, -3, 0, -4, -5]
print("The maximum product subarray is:", max_prod(arr))