# The inputs are an integer array
# We want to choose a day to buy and a different day to sell 
# Our output will be the max_profit from prices

# - no negatives
# Example 1 

'''
prices = [10,1,5,6,7,1]

First step is going to be 
buying at prices[0] = 10



and we want to check if this is our minimum price 

since its our only price so far we would have it as our minimum

we would then check the rest of the list for a new min and if there is no new min
we can return min as our max profit also could be 0 

profit = price[i] - min 
'''

# Step 1 : 10 < inf = true #
# Step 2 : 1 < 10 = true # new_min
# Step 3 : 5 < 1 = false # profit = 5 - 1 = 4
# profit = 4  etc..

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Brain storming solution
        min_price = float('inf')
        max_profit = 0

        for num in prices:
            if num < min_price:     # Step 1 : 10 < inf = true #
                min_price = num 

            # Get the profit 
            profit = num - min_price 

            # We now want to return our max profit
            # Checks if the new profit from above is greater then the current max
            if profit > max_profit:
                max_profit = profit

        return max_profit

        # Time: O(n)
        # Space: O(1)
        

            

         

    
            