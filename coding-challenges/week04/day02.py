{
Even : 5,
Odd : 5
}

a_string = "envelope"
lowercase = a_string.lower()
vowel_counts = {}
for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count
print(vowel_counts)
