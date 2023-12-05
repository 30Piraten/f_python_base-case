# Using list.sort and sorted

fruits = ["grape", "raspberry", "sardines", "apple", "banane"]

print(sorted(fruits))

print(sorted(fruits, reverse=True))
print(sorted(fruits, key=len))
print(sorted(fruits, key=len, reverse=True))

print()

others = ["orange", "watermelon", "grape", "sugar"]
print(others.sort())
print(others.sort(key=len, reverse=True))
