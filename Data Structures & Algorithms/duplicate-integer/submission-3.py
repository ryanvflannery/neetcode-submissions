# The input is a list of integers nums
# We want to return true if any value appears more than one time in this array
# Our output will be True or False

'''
nums = [1,2,3,3]

seen = [1,2,3,3]
'''

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        # We want to loop through nums list until its empty
        for number in nums:
            if number not in seen:
                seen.add(number)
            else:
                return True
        
        return False
        




        
         