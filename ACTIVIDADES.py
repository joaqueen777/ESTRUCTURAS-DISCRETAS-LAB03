def division(a, b):
    if b > a:
        return 0
    return division(a - b, b) + 1
