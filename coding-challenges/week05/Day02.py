n = int(input(“Enter value of n”))
for i in range(n):
for j in range(n):
print(“Space complexity”)

O(n) is the complexity

n = int(input())
dict = {}
for i in range(n):
for j in range(n):
dict[j] = j

O(1) is the complexity 

class Solution:
def plusOne(self, digits: List[int]) -> List[int]:
    numStr=""
    for i in digits: 
        numStr+=str(i)
        
    newNum=int(numStr)+1
    newNumStr=str(newNum)
    l=len(newNumStr)
    
    for i in range(0,l):
        digits[i]=newNum%10
        print(digits[i])
        newNum=int(newNum/10)
        
    return digits[::-1]
