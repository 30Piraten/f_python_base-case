import numpy as np

a = np.arange(12)

print(a)

r = a.shape
print(r)

r = 3, 4
# print(r)

print(a[2])

print(a[2, 1])

print(a[:, 1])

print(a.transpose())
