def get_power(number, exponent):
    if exponent == 0:
        return 1
    else:
        return number * get_power(number, exponent-1)


def power(number, exponent):
    pow = 1
    for i in range(1, exponent):
        pow = pow * number
    return pow


print(get_power(2, 3))
