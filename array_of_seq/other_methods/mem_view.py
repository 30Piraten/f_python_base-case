# Handling 6 bytes of memory as 1x6, 2x3, and
# 3x2 views

from array import array

matrix = array("B", range(12))
m1 = memoryview(matrix)
m1.tolist()

m2 = m1.cast("B", [3, 4])
print(m2.tolist())


m3 = m1.cast("B", [4, 3])
print(m3.tolist())


m2[1, 1] = 22  # type: ignore
m3[1, 1] = 33  # type: ignore

print(matrix)
