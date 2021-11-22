n = int(input("Enter a number: "))
for i in range(n):
  i=("Hello World")
  print(i)
  
n = int(input("Enter a number: "))
for i in range(1, n+1):
 print(2 * i)

n = int(input("Enter a number: "))
for n in range(1, n+1):
  if n%3==0 and n%5==0:
     print("FizzFuzz")
     continue
  elif n%3==0:
      print("Fuzz")
      continue
  elif n%5==0:
      print("Fizz")
  print(n)
  
  
  

