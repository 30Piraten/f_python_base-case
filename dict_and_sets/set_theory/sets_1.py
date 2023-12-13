# check the number of occurrence of x in y

# here both values must be a set
colors = {'red', 'green', 'blue', 'yellow', 'orange'}
container = {"red", "white", "blue", "red", "green", "orange", "orange"}
number_of_occurrence = len(colors & container)

print(number_of_occurrence)

# without using a set
# this works for any iterable
found = 0
for n in colors:
    if n in container:
        found += 1

print(found)

# rewriting with set comprehension
case = {f for f in colors if f in container}
print(len(case))


# working without sets
x = ["a", "b", "c"]
y = ("a", "b", "d", "e")

case_2 = len(set(x) & set(y))
print(case_2)

print()

case_3 = len(set(x).intersection(y))
print(case_3)
