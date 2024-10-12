from queue import PriorityQueue

priorityQ= PriorityQueue()

priorityQ.put((3, (10,2)))
priorityQ.put((2, (8,2)))
priorityQ.put((10, (7,3)))

prio, cors = priorityQ.get()
print(prio)
print(cors)

