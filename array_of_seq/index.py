# Unpacking Function Calls and Sequence Literals with *

def main(x, y, z, *rest):
    return x, y, z, rest


r = main(*[1, 3], 5, *range(8, 21))
print(r)


a, *rest, b, c = range(6)
print(a, rest, b, c)
