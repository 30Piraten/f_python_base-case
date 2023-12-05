l = [28, "4", 10, -11, "19", "22", 30, 45]

# items are treated as an int or a str
# then sorted
r = sorted(l, key=int)
r1 = sorted(l, key=str)

print(r)
print(r1)
