# The input is an array nums 
# We want to return the longest consecutive sequence - Where each element in nums is 1 great than the pervious element
# The output will be the longest consec sequence 

# Must be O(n) Time 

'''
Input: nums = [2,20,4,10,3,4,5]

Output: 4

When should we start a sequence 
'''

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        nums_set = set(nums)

        # Loop through nums
        for n in nums_set:

            # Start of a sequence 
            if (n - 1) not in nums_set:
                length = 1
                current = n       
                
                # If next number exists keep growing
                while current + 1 in nums_set:
                    current += 1
                    length += 1
                longest = max(longest, length)

        return longest







        