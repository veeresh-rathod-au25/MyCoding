class Solution:
    def average(self, salary: List[int]) -> float:
        max = -1
        sum=0
        count=0
        min = float('inf')
        for i in range(len(salary)):
            if salary[i] > max:
                max = salary[i]
            if salary[i] < min:
                min = salary [i]
        
        for i in range(len(salary)):
            if salary[i] != max and salary [i] != min:
                count=count+1
                sum=sum+salary[i]
        return sum/count
                