class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.number_of_elements = 0
    self.storage = [None]*capacity

  def append(self, item):
    # save with index current
    self.storage[self.current] = item
    # increase current and loop if goes over capacity
    self.current += 1
    if self.current >= self.capacity:
      self.current = 0
    if self.number_of_elements < self.capacity:
      self.number_of_elements += 1

  def get(self):
    # return storage
    return self.storage[:self.number_of_elements]