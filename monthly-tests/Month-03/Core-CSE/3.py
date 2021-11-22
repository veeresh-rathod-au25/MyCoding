def minsum(arr,n,x):
    Sum = 0
    largestDivisble, minimum = -1, arr[0]
    for i in range(0,n):

        Sum += arr[i]

        if(arr[i] % x == 0 and largestDivisble < arr[i]):
            largestDivisble = arr[i]
        if arr[i] < minimum:
            minimum = arr[i]
    
    if largestDivisble == -1:
        return Sum

    sumafteroperation = (Sum - minimum - largestDivisble + (x * minimum) + (largestDivisble // x))
    return min(Sum, sumafteroperation)

