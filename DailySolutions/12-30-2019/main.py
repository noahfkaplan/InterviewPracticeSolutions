import Queue

queue = Queue.Queue()
values = [1, 2, 3]
queue = Queue.Queue()
queue.enqueue(values[0])
queue.enqueue(values[1])
queue.enqueue(values[2])
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())