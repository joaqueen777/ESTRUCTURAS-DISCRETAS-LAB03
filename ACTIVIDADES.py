def division(a, b):
    # division entera por restas sucesivas
    if b > a:
        return 0
    return division(a - b, b) + 1
