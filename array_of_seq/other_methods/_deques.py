from collections import deque

dq = deque(range(10), maxlen=10)
print(dq)

dq.rotate(3)
print(dq)
dq.rotate(-4)
print(dq)
dq.appendleft(-9)
print(dq)
dq.extend([11, 14, 98])
print(dq)
dq.append(23)
print(dq)
dq.pop()
print(dq)
dq.popleft()
print(dq)
dq.extendleft([10, 45, 35, 19])
print(dq)


# print(dq)
