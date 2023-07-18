'''
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
Example 1: Input: strs = ["eat","tea","tan","ate","nat","bat"] Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2: Input: strs = [""] Output: [[""]]
Example 3: Input: strs = ["a"] Output: [["a"]]

Answer:
1. Create a dictionary to store the sorted string as the key and the original string as the value
2. Return the values of the dictionary
'''

def groupAnagrams(strs):
    anagrams = {}
    for i in strs:
        sorted_str = ''.join(sorted(i))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(i)
        else:
            anagrams[sorted_str] = [i]
    return anagrams.values()
