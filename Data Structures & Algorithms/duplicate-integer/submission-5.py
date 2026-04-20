# The input is an array nums
# We want to check if any value appeats more than once in the nums array
# The output will be return true if any value appears more then once otherwise return false



class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()

        for n in nums:
            if n not in seen:
                seen.add(n)
            else:
                return True

        return False

        
