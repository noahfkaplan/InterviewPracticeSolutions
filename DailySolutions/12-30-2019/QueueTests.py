import unittest
import Queue

class QueueTests(unittest.TestCase):

    def test_returnsNone_WhenNoValuesEnqueued(self):
        queue = Queue.Queue()
        self.assertEqual(queue.dequeue(), None)
    def test_returnsOnlyValue_WhenOneValueEnqueued(self):
        value = 1
        queue = Queue.Queue()
        queue.enqueue(value)
        self.assertEqual(queue.dequeue(), value)

    def test_containsNoValues_WhenAllValuesDequeued(self):
        value = 1
        queue = Queue.Queue()
        queue.enqueue(value)
        queue.dequeue()
        self.assertEqual(queue.dequeue(), None)

    def test_returnsValuesInFIFOOrder_WhenValuesDequeued(self):
        values = [1, 2, 3]
        queue = Queue.Queue()
        queue.enqueue(values[0])
        queue.enqueue(values[1])
        queue.enqueue(values[2])
        self.assertEqual(queue.dequeue(), values[0])
        self.assertEqual(queue.dequeue(), values[1])
        self.assertEqual(queue.dequeue(), values[2])