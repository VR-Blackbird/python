from collections import deque

dq = deque(range(10), maxlen=10)
dq.rotate(5)
print(dq)
dq.rotate(-6)
print(dq)
dq.appendleft(109)
print(dq)
dq.append(198)
print(dq)
dq.extendleft([11, 12])
print(dq)
