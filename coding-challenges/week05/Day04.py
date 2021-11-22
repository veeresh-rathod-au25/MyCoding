def row_sum(arr):
    sum = 0
    print("Finding Sum of each row:")

m = 5
n = 5
arr = 0

for i in range(m):
    for j in range(n):
        sum += arr[i][j]
        print("Sum of the row", i, "=", sum)
        sum = 0
