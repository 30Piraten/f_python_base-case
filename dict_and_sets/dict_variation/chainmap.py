from collections import ChainMap

r1 = dict(a=2, b=4)
r2 = dict(a=17, b=-2, c=5, d=0)

chain = ChainMap(r1, r2)

print(chain["a"])
print(chain["c"])
