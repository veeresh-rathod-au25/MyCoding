# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         dp = [[0]*(len(text1)+1) for _ in range(len(text2)+1)]
#         for i in range(1,len(text2)+1):
#             for j in range(1,len(text1)+1):
#                 dp[i][j] = max(dp[i-1][j],dp[i][j-1])
#                 if text2[i-1] == text1[j-1]:
#                     dp[i][j] = dp[i-1][j-1] + 1
#         return dp[-1][-1]

# n=int(input())
# a = list(map(int,input().strip().split()))[:n]
# increasing=a.sort()
# decreasing=a.sort(reverse=True)
# print(increasing)

n=int(input())
a = list(map(int,input().strip().split()))[:n]
increasing=sorted(a)
decreasing=sorted(a,reverse=True)

for i in range (n):
    temp=a.pop()
    a.append(temp)
    print(a)
    flag=0    
    for j in range (n):
        if(a[j]!=increasing[j]):
            flag=1
            break
    for j in range (n):
        if(a[j]!=decreasing[j]):
            flag=1
            break
        
    if(flag==0):
        print("Yes")
        break
if(flag==1):
    print("NO")

        
        
  

        
        
        
            