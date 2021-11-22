n=int(input())
a = list(map(int,input().strip().split()))[:n]
firstmax=0
secondmax=0
for i in range(n):
    if a[i]>firstmax:
        secondmax=firstmax
        firstmax=a[i]
    elif a[i]>secondmax:
        secondmax=a[i]
if firstmax <= 2*secondmax:
    print("NO")
else:
    print("YES")