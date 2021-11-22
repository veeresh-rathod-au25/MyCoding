def isPalindrome(num):
     n = num
     rev = 0
     while n:
        r = n % 10
        rev = rev * 10 + r
        n = n // 10
     return num == rev
 
 
if __name__ == '__main__':
 
    n = 1451
 
    if isPalindrome(n):
        print("Palindrome")
    else:
        print("Not Palindrome")