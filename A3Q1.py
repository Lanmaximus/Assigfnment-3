def sum(*a):
    total = 0
    for i in a:
        total += i
    return total
print(sum(8, 2, 3, 0, 7))