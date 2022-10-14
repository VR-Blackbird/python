#!/usr/bin/python3

import heapq


class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index+=1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

q = PriorityQueue()
q.push('bob', 10)
q.push('loaf', 12)
q.push('loath', 8)
q.push('ball', 11)
q.push('bat', 11)

for i in range(5):
   print(q.pop())
