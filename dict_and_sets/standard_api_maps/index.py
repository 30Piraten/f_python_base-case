# Common mapping methods

# a tuple
tp = (1, 2, 3, (30, 45))
r = hash(tp)

print(r)

# a list in a tuple
# this tuple is not hashable because
# the elements inside it are of diff type.
# --> list*
tp_1 = (1, 2, 3, [45, 23])
r1 = hash(tp_1)

print(r1)

# using a frozenset, we can turn the latter
# into a hashable code
tp_2 = (1, 2, 3, frozenset([23, 45]))
r2 = hash(tp_2)
print(r2)
