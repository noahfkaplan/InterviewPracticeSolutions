class Queue:
  def __init__(self):
    # Fill this in.
    self.stack1 = []
    self.stack2 = []
    self.stack1Active = True

  def enqueue(self, val):
    # Fill this in.
    if self.stack1Active:
        self.stack1.append(val)
    else:
        self.stack2.append(val)

  def dequeue(self):
    # Reverse the list and get the last value
    value = None
    if len(self.stack1) == 0:
        return value
    for i in range(0, len(self.stack1)): 
        self.stack2.append(self.stack1.pop())
    value = self.stack2.pop()
    # Reverse the list

    for i in range(0, len(self.stack2)):
        self.stack1.append(self.stack2.pop()) 
        
    return value