s = [1, 5, 6]
print(id(s))

s *= 2
print(s)
# for the mutable sequence, both IDs remain
# the same with new items appended
print(id(s))

t = (1, 8, 9)
print(id(t))

t *= 2
print(t)
# a new copy of the tuple is created
# from the first, and appended to "t"
# with a new ID
print(id(t))
