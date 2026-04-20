# The input is string s
# We want to check if s is valid 
# - Every open bracket must be closed by the same type of bracket, 
# - Open brackets closed in correct order, 
# - Every closed bracket must have a open bracket of same type

# Our output will be true if valid and false if not

class Solution:
    def isValid(self, s: str) -> bool:

        store_opening = []
        openings = {"(", "{", "["}

        # Key = close : value = open
        closing_to_open = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for char in s:
            
            if char in openings:
                store_opening.append(char)
            else:
                if not store_opening:
                    return False

                if store_opening[-1] == closing_to_open[char]:
                    store_opening.pop()
                else:
                    return False                        
            

        return not store_opening




        