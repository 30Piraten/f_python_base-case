# Merge Mapping


r1 = {"x": 4, "y": 7}
r2 = {"x": 0, "y": 8, "z": 11}

# the "|" creates a new mapping
r3 = r1 | r2
print(r3)

# to update an existing mapping
# we use the |=

# r = r1 |= r3
# print(r, "rice")
