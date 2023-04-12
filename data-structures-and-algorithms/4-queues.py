from collections import deque

"""Queue data structure implementation in Python"""


class Queue:
  
  def __init__(self):
    self.queue = deque()
  
  def enqueue(self, item):
    self.queue.append(item)
  
  def dequeue(self):
    if len(self.queue) > 0:
      return self.queue.popleft()
    return None
  
  def get_size(self):
    return len(self.queue)
  
  def __str__(self):
    return str(self.queue)


my_queue = Queue()
my_queue.enqueue(1)
my_queue.enqueue(3)
# print(my_queue)
assert my_queue.dequeue() == 1
assert my_queue.get_size() == 1
assert my_queue.dequeue() == 3
assert my_queue.dequeue() == None
