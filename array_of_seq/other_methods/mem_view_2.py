# Changing the value of a 16-bit integer array
# item by poking one of its bytes

from array import array

digits = array("h", [-2, -1, 0, 1, 2])
memory_view = memoryview(digits)

print(len(memory_view))
print(memory_view[0])

memory_view_oct = memory_view.cast("B")
r = memory_view_oct.tolist()
print(r)

memory_view_oct[5] = 4
print(digits)
