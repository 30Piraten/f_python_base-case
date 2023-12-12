from types import MappingProxyType

dt = {1: "F"}

dt_proxy = MappingProxyType(dt)

print(dt_proxy)

print()

print(dt_proxy[1])

print()

# this throws an error as changes cannot
# be made through dt_proxy instance
# --> dt_proxy[2] = "X"

case = dt[2] = "X"

print()

print(dt_proxy)

print(dt_proxy[2])
