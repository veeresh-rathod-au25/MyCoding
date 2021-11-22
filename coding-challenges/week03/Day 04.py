def printMax(a, b):
  if a > b:
    print(a, 'is maximum')
  elif a == b:
   print(a, 'is equal to', b)
  else:
    print(b, 'is maximum')

printMax(3, 4)

# 4 is maximum

x = 50
def func(x):
  print('x is', x)
  x = 2
  print('Changed local x to', x)
  
func(x)
print('x is now', x)

# X is now 50

def rem_vowel(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)
 

string = "ABCDEFG"
rem_vowel(string)
