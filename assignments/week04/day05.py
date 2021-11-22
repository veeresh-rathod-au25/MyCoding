def countOccurrences(str, word):
    a = str.split(" ")
    count = 0
    for i in range(0, len(a)):
      if (word == a[i]):
        count = count + 1
    return count       
  
str ="AttainU AttainU e r tdsvvdsvsdv AttainU"
word ="AttainU"
print(countOccurrences(str, word))

class Speed:
    def __init__(self, kilometer):
        self.km = kilometer

    def convert(self):
        print("meter =", self.km/3.6)


kilometer = float(input("ENter the value : "))

rush = Speed(kilometer)
rush.convert()


