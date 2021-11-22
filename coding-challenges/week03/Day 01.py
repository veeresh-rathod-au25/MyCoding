a = int(input("Enter a number "))
b = int(input("Enter a number "))
c = int(input("Enter a number "))

if (a > b and c):
  print (a)
elif (b>a and c):
  print(b)
elif (c>b and a):
  print(c)
  
 
  
a = int(input("Enter a number "))
if a%2==0 and a%5==0:
  print("Fizz-Fuzz")
elif a%2==0:
  print ("Fizz")
elif a%5==0:
  print ("Fuzz")
