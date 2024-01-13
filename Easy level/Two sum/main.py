numbers = [2, 2, 3, 5 , 9]

def two_sum(numbers, target):
    res = []
    for x in range(len(numbers)):
        for y in range(1, len(numbers)):
            if numbers[x] + numbers [y] == target:
                res.append(x)
                res.append(y)
            else:
                pass
    for z in range(len(res)-1, 1, -1):
        res.remove(res[z])        
    return res

print(two_sum(numbers, 8))