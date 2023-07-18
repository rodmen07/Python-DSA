'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
Example 1: Input: nums = [1,1,1,2,2,3], k = 2 Output: [1,2]
Example 2: Input: nums = [1], k = 1 Output: [1]

Answer:
1. Create a dictionary to store the frequency of each element in the array
2. Sort the dictionary by the frequency of each element in descending order
3. Return the first k elements in the sorted dictionary
'''

class Solution:
    def topKFrequencyElements(self, nums, k):
        freq = {}
        for i in nums:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1

        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [sorted_freq[i][0] for i in range(k)]
