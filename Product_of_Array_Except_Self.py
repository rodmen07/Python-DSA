'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.
Example 1: Input: nums = [1,2,3,4] Output: [24,12,8,6]
Example 2: Input: nums = [-1,1,0,-3,3] Output: [0,0,9,0,0]

Answer:
1. Create a list to store the product of all the elements to the left of the current element
2. Create a list to store the product of all the elements to the right of the current element
3. Create a list to store the product of all the elements except the current element
4. Return the list of products
'''

def productExceptSelf(nums):
    left = [1]
    right = [1]
    for i in range(len(nums)-1):
        left.append(left[-1] * nums[i])
        right.append(right[-1] * nums[-i-1])
    right.reverse()
    return [left[i] * right[i] for i in range(len(nums))]
