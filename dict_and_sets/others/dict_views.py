dt = dict(x=22, y=14, z=12, i=0)

# .values()
v = dt.values()
print("1", v)

length = len(v)
print("2", length)

lt = list(v)
print("3", lt)

rv = reversed(v)
print("4", rv)

# throws an error. Can't use []
# to get individual items from a view
# --> v0 = v[0]

dt["r"] = 9
print("5", dt)

print("6", v)

# .keys()
key = dt.keys()
print("7", key)

length0 = len(key)
print("8", length0)

# .items()
item = dt.items()
print("9", item)

rv0 = reversed(item)
print("10", rv0)
