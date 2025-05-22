def sumproduct(a, b, percent=False):
    total = sum(x * y for x, y in zip(a, b))
    return total / 100 if percent else total
