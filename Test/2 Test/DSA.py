
def sea_shell(shells):
    maxl = 0
    curr_letter, curr_length = None, 0
    for sea in shells:
        if not curr_letter or curr_letter != sea[0]:
            maxl = max(maxl, curr_length)
            curr_letter, curr_length = sea[0], 1
        else:
            curr_length += 1
    return max(maxl, curr_length)

shells = ["she","sells","seashells"]
print(sea_shell(shells))


