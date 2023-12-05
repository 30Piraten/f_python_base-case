import dis

t = (5, 6, [23, 55, 44])

# displays actual result with
# a Traceback error! -->
# tuple object does not support item
# assignment
# --> t[2] += [56, 12]

# this can be rectified with
t[2].extend([56, 12])
print(t)

print()
# Bytecode for the expression: s[a] += b
dis.dis("s[a] += b")
