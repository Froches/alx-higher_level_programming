#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div

    a = 10
    b = 5

    res_add = add(a, b)
    res_sub = sub(a, b)
    res_mul = mul(a, b)
    res_div = div(a, b)

    print("{} + {} = {}".format(a, b, res_add))
    print("{} - {} = {}".format(a, b, res_sub))
    print("{} * {} = {}".format(a, b, res_mul))
    print("{} / {} = {}".format(a, b, res_div))
