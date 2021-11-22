class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = []
        
        for i in range(numRows):
            arr.append([]) # Creates the row
            
            for j in range(i+1): # Creates the columns for each row.
                if j == 0 or j == i: # First and last element will always be 1
                    arr[i].append(1)
                else: 
				    # All other elements will be the sum of the element with the same index and the element before that in the previous row.
                    arr[i].append(arr[i-1][j-1] + arr[i-1][j]) 
                    
        return arr
