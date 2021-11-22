def selectionSort(arr, n):
   
    for stp in range(n):
        min = stp

        for i in range(stp + 1, n):
         
            if arr[i] < arr[min]:
                min = i
         
        (arr[stp], arr[min]) = (arr[min], arr[stp])


arr = [-2, 45, 0, 11, -9]
n = len(arr)
print('Elements before sorting:')
print(arr)
selectionSort(arr, n)
print('Elements after sorting:')
print(arr)