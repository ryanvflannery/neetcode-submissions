
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:


        # Check length of strings s and t 
        if len(s) != len(t):
            return False

        # Empty hashmaps for strings s and t
        # Key: Letter | Value: Count
        countS = defaultdict(int)
        countT = defaultdict(int)


        # Build hashmap
        # Do both strings have the same counts of each letter
        for char in s:
            countS[char] += 1

        for char in t:
            countT[char] += 1
        
        # Checking if its true or false
        return countS == countT
        