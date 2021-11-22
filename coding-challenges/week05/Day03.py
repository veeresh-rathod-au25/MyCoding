n = int(input("Enter a number: "))
for i in range(n):
    for j in range(n):
        print("Space Complexity")


print("Space Complexity is O(N)")

def incrementVector(a):
  
    n = len(a)
    a[n-1] += 1
    carry = a[n-1]/10
    a[n-1] = a[n-1] % 10
   
    for i in range(n-2,-1,-1):
        if (carry == 1):
           a[i] += 1
           carry = a[i]/10
           a[i] = a[i] % 10
          
    if (carry == 1):
      a.insert(0, 1)

vect=[1, 7, 8, 9]
  
incrementVector(vect)
  
for  i in range(0, len(vect)):
     print(vect[i] ,end= " ")

def rearrange(arr, n):

    temp = n*[None]
    small, large = 0, n-1

    flag = True

    for i in range(n):
        if flag is True:
            temp[i] = arr[large]
            large -= 1
        else:
            temp[i] = arr[small]
            small += 1

        flag = bool(1-flag)

    for i in range(n):
        arr[i] = temp[i]
    return arr


arr = [1, 2, 3, 4, 5, 6]
n = len(arr)
print("Original Array")
print(arr)
print("Modified Array")
print(rearrange(arr, n))