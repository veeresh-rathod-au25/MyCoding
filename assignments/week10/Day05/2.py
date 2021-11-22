class Solution:
    def getRow(self, n: int) -> List[int]:
        n=n+1
        arr = [1]
        a=1
        b=1
        for i in range (1,n):
            a=a*(n-i)
            b=b*(i)
            res=a//b
            arr.append(res)
        return arr
