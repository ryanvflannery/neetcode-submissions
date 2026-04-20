class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        m = len(matrix)
        n = len(matrix[0])
        # t = total number of elements in the matrix
        t = m * n

        # first element 
        l = 0
        # last element
        r = t - 1

        while l <= r:
            m = (l + r) // 2
            # row index i
            i = m // n
            # column index j 
            j = m % n 

            midNum = matrix[i][j]

            if target == midNum:
                return True
            # search left side
            elif target < midNum:
                r = m - 1
            # search right side
            else:
                l = m + 1
        return False


        # Time Complexity O(log(m * n))
        # Space: O(1)


        