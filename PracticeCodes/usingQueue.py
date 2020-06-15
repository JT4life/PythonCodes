#Queue : First in first out data structure
import queue

'''q = queue.Queue()
q.put("A")
q.put("B")
q.put("C")
q.put("D")
q.put("E")
q.put("F")

for i in range(q.qsize()):
    print(q.get())'''

#LifoQueue : Last in first out data structure

'''q = queue.LifoQueue()
q.put("A")
q.put("B")
q.put("C")
q.put("D")
q.put("E")
q.put("F")

for i in range(q.qsize()):
    print(q.get())'''

#Priority Queue : According to priority
'''q = queue.PriorityQueue()

q.put((1,"A"))
q.put((3,"B"))
q.put((2,"C"))

for i in range(q.qsize()):
    print(q.get())'''

#Python heapq
import heapq
q = []
heapq.heappush(q,(2,'B'))
heapq.heappush(q,(1,'A'))
heapq.heappush(q,(3,'C'))
while q:
    item = heapq.heappop(q)
    print(item)
