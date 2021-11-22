def Check_Vow (string, vowels):
    vowel = [each for each in string if each in vowels]
    print(vowel)
     
string = "Geeks for Geeks Lion Tiger Giraffe"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels);

num = int(input("Enter a number: "))  
sum = 0
while(num > 0): 
  sum = sum + num
  num = num - 1;
print("The sum is",sum)

num = int(input("Enter a number: "))  
for i in range(1, num + 1):
       if num % i == 0:
           print(i)



