# Assigning to Slices

# Created a list
x = list(range(2, 16))
print(x)

# Assigning values
x[2:5] = [20, 30]

# del
del x[5:7]

# other
x[3::2] = [23, 44]
x[3::1] = [12, 15]
x[2::1] = [10, 22]

# x[2:5] = 100  # this throughs a TypeError. Value on the right must be iterable -->
x[2:5] = [100]
