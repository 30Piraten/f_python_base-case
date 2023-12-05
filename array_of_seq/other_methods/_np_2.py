from array import array
from random import random
# import numpy

floating_point_numbers = []
numbers = array("d", (random() for _ in range(10**7)))
numbers2 = array("d", (random() for _ in range(10**7)))

with open("floats-10M-lines.txt", "w") as floats:
    floats.write(str(numbers))
    floats.close()

with open("floats-10M-lines.txt", "r") as rd:
    x = rd.readlines()
    print(x)

fp = open("floats_10M-lines_2.txt", "wb")
numbers2.tofile(fp)
