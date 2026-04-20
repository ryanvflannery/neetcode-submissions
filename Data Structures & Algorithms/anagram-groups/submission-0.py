# The input is an array of strings strs
# We want to grou all anagrams together with sublists
# We want to return the output in any order

# - An anagram is a string that contains the exact same characters as another string but order of char can be different 

# Example 1
'''
Input:
strs = ["act","pots","tops","cat","stop","hat"] list of strings

Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

We notice that act has and cat have the same 3 characters / stop, pots, and tops all have the same 4 characters
We could create a hashmap to group words by their sorted letters

key: sorted letters (act) / Value: a list of words that match this key

sort letters then match the key (act) : cat same 3 letters
'''

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # BrainStorm
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_letters = "".join(sorted(s)) # sort characters in the string s word by word
            anagram_map[sorted_letters].append(s)

        return list(anagram_map.values())

            


        
        