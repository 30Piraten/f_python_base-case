# Unpacking mappings

def dump(**kwargs):
    return kwargs


# ** can be applied to multiple arguments
# no duplicate keys allowed
r = dump(**{"x": 1}, y=2, **{"z": 3})
print(r)

# **, can be used inside a dict literal
# also multiple times
# duplicates allowed. Later occurrence, overwrites
# previous ones!
r1 = {"a": 0, **{"x": 2}, "y": 4, **{"z": 11, "x": 7}}
print(r1)
