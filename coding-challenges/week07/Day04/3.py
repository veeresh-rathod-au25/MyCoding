# Take two inputs A and B as integers. => A = 5 , B = 3 Convert them to
# binary, => A = 101, B = 011 perform XOR operation, => A^B = 110 return
# resultant binary number as decimal number . => (110)2 =
# (6)1

a = int(input())
b = int(input())
x = bin(a)
y = bin(b)

i=0
j=0
result=""
while i<len(x) and j<len(y):
    if(x[i] != y[j]):
        result= result+"1"
    else :
        result = result+"0"

    i=i+1
    j=j+1
print(int(result))

