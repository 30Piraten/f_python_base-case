# Creating, saving and loading an array
# of 10 million floating point random numbers


from array import array
from random import random

# create an array of double precision floating point numbers
floats = array("d", (random() for _ in range(10**7)))
# print(floats)

# inspect the last item in the array
result = floats[-1]
print(result)

# save the array in a binary file
fp = open("floats.bin", "wb")
floats.tofile(fp)
fp.close()

# create an empty array of doubles || floats
floats_2 = array("d")
fp = open("floats.bin", "rb")

# read 10 million numbers from the binary file
floats_2.fromfile(fp, 10**7)
fp.close()

# inspect the last item in the array
result_1 = floats_2[-1]
print(result_1)

# verify if content of both arrays match
print(floats_2 == floats)
