# The input is nums array 
# We want to sort the array in place from 0, 1, 2
# The output will be the sorted array 

# No extra space must be done in place


'''

left = next availible index for a 0 
mid = iterate through array for values to swap 
right = tell us next avaiblie index for a 2
               m
Input: nums = [1,0,1,2]
               l
                      r

Output: [0,1,1,2]


'''



class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        left = 0
        mid = 0
        right = len(nums) - 1

        while mid <= right:
            if nums[mid] == 2:
                # Swap the mid with the right pointer
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1
            elif nums[mid] == 0:
                # Swap the mid with the left
                nums[mid], nums[left] = nums[left], nums[mid]
                left += 1
                mid += 1
            else:
                # if at a element 1 
                mid += 1


        return nums
        