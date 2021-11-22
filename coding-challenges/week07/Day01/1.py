NumList = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

i = 0
while(i < Number):
    j = i + 1
    while(j < Number):
        if(NumList[i] > NumList[j]):
            temp = NumList[i]
            NumList[i] = NumList[j]
            NumList[j] = temp
        j = j + 1
    i = i + 1

print("Element After Sorting List in Ascending Order is : ", NumList)