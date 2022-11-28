a = int(input(""))
b = int(input(""))
def getFPB(a, b):
    if (b == 0):
        return a
    else:
        return getFPB(b, a% b)

print(f'FPB ({a}, {b}) = {getFPB(a, b)}')
getFPB(a, b)