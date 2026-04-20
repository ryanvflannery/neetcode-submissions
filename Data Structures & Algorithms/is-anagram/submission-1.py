
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # Check length of strings s and t 
        if len(s) != len(t):
            return False

        # Empty hashmaps for strings s and t
        countS = defaultdict(int)
        countT = defaultdict(int)


        # Build hashmap
        # Order of characters can be different
        
        # We could loop through string s and compare each letter to string t

        for char in s:
            countS[char] += 1

        for char in t:
            countT[char] += 1
        
        if countS != countT:
            return False

        return True 
        