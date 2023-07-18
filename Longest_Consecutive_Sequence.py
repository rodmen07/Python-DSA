'''
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
You must write an algorithm that runs in O(n) time.
Example 1: Input: nums = [100,4,200,1,3,2] Output: 4 Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2: Input: nums = [0,3,7,2,5,8,4,6,0,1] Output: 9

Answer:
1. Create a set to store all the elements in the array
2. Create a variable to store the longest consecutive sequence
3. Iterate through the set
4. If the current element is not in the set, continue
5. Create a variable to store the current consecutive sequence
6. Create a variable to store the current element
7. While the current element is in the set, increment the current consecutive sequence and the current element
8. Update the longest consecutive sequence if the current consecutive sequence is greater than the longest consecutive sequence
9. Return the longest consecutive sequence
'''


def longestConsecutive(nums):
    nums = set(nums)
    longest = 0
    for i in nums:
        if i - 1 not in nums:
            curr = 1
            curr_num = i
            while curr_num + 1 in nums:
                curr += 1
                curr_num += 1
            longest = max(longest, curr)
    return longest


def longestConsecutiveOptimized(nums):
    nums = set(nums)
    longest = 0
    for i in nums:
        if i - 1 not in nums:
            curr = 1
            curr_num = i + 1
            while curr_num in nums:
                curr += 1
                curr_num += 1
            longest = max(longest, curr)
    return longest
