# The input is a sorted array of numbers and a target
# We want to find the elements in the array that add up to the target
# The output will be the indicies of the two elements that add up to target


'''

May not use the same element twice

1 + 4 = 5
1+3 = 4


Input: numbers = [1,2,3,4], target = 3
                  ^
                      ^
Output: [1,2]

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        

        left = 0
        right = len(numbers) - 1

        while left < right:

            current_sum = numbers[left] + numbers[right]
            # We want to check if numbers[left] + numbers[right] add up to the target 
            if current_sum == target:
                return [left + 1, right + 1]
            elif current_sum < target:
                left += 1
            else:
                right -= 1
                
        
