from time import perf_counter as pc
import numpy

floats = numpy.loadtxt("floats-10M-lines.txt")
print(floats[-3:])

floats *= .5
print(floats[-3:])

t0 = pc()
floats /= 3
r1 = pc() - t0
print(r1)

numpy.save("floats-10", floats)
floats_2 = numpy.load("floats-10M.npy", "r+")
floats_2 *= 6
print(floats_2[-3:])
