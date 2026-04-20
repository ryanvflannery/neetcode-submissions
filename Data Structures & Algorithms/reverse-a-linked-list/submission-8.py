# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


# The input is a singly linked list head
# We want to reverse this list 
# Our output will be the new beginning of the list

# - can be an empty list

# Example 1
'''
We have our head which is a list of elements
We want to reverse the linked list 
We know that in a linked list the current node points to the next node 1 way
0 -> 1 -> 2 -> 3

and we want that the opposite way

0 <- 1 <- 2 <- 3

'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Brain Storm 
        # singly linked list always have a curent node and points to the next node

        curr = head
        previous = None
        # previous = 0 <- 1 <- 2 <- 3

        while curr:
            temp = curr.next             # 1
            curr.next = previous         # first pass previous = 1
            previous = curr              # new current = 1 
            curr = temp                  # Grab next number in list curr = 1

                                        # 2nd pass 
                                        # temp = 2
                                        # previos = 2
                                        # curr = 2
                                        # 2

                                        # 0, 1, 2, 3
                                        

        return previous                  
                                

            

        
             
        
        
        


