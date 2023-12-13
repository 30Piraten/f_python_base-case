case = ["spam", "spam", "eggs", "bacon", "banana", "corn"]
c = set(case)
print(c)

print()

c0 = list(c)
print(c0)

print()
# to retain the order of the first
# occurrence of each item, and remove
# duplicates:

case1 = dict.fromkeys(case).keys()
print(case1)

print()

case2 = list(dict.fromkeys(case).keys())
print(case2)
