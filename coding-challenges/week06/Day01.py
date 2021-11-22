  
arr = [1,23,45,56,65,78,85,98]
target = 99
def bin_search(arr,x):
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = (low+high)//2
        if arr[mid]<x:
            low = mid+1
        elif arr[mid]>x:
            high = mid - 1
        else:
            return mid
    return -1

if __name__=="__main__":
    res = bin_search(arr,target)
    if res == -1:
        print("Target not present")
    else:
        print("Element is present at index",res)


number = int(input("enter a number: "))
res = number ** 0.5
print("square root:", int(res))

def findPeakElement(A, left, right):
    mid = (left + right) // 2
    if ((mid == 0 or A[mid - 1] <= A[mid]) and
            (mid == len(A) - 1 or A[mid + 1] <= A[mid])):
        return mid
    if mid - 1 >= 0 and A[mid - 1] > A[mid]:
        return findPeakElement(A, left, mid - 1)
    return findPeakElement(A, mid + 1, right)


if __name__ == '__main__':
    A = [8, 9, 10, 2, 5, 6]
    index = findPeakElement(A, 0, len(A) - 1)
    print("The peak element is", A[index])

values = input("Input some comma seprated numbers : ")
list = values.split(",")
print('List : ',list)

