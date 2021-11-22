def find_max_sum(arr):
    incl = 0
    excl = 0
    for i in arr:
        new_excl = excl if excl>incl else incl
        incl = excl + i
        excl = new_excl
    return (excl if excl>incl else incl)
 
arr = [5, 5, 10, 100, 10, 5]
print (find_max_sum(arr))