import collections

counter = collections.Counter("abbcdeeffg")
print(counter)

print()

counter.update("aaaabeedff")

print()

ctr_common = counter.most_common(4)
print(ctr_common)
