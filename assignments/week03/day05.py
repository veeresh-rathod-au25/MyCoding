a = int(input("Enter a no: "))
b = int(input("Enter a no: "))
if a>b and b<a:
  print(a)
elif b>a and a<b:
 print (b)

a = int(input("Enter a no: "))
if a%3==0 and a%5==0:
  print("FizzBuzz")
elif a%3==0:
  print("Fizz")
elif a%5==0:
  print("Buzz")
else:
  print(a)
  
a = int(input("Enter a no: "))
factor = 1
for i in range(1,a+1):
  factor = (factor * i)
print("The factorial of",a,"is",factor)

a = ("*")
for i in range(6):
  for j in range(i):
    print (a, end="")
  print()

  
