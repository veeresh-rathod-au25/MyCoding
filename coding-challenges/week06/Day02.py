def rev(string):
    if len(string)==0:
        return
    print(string[-1], end="")
    rev(string[:-1])

string = "ABCD"
rev(string)

____________________________________________________________________

def myAtoiRecursive(string, num):

    if len(string) == 1:
        return int(string) + (num * 10)

    num = int(string[0:1]) + (num * 10)

    return myAtoiRecursive(string[1:], num)


string = "112"
print(myAtoiRecursive(string, 0))
______________________________________________________________________

