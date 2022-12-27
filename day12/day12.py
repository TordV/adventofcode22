from aocd import get_data
from sys import maxsize

class Map:
  def __init__(self, height_map):
    self.height_map = height_map

  def search(self, start_pos):
    self.indexes = {}
    self.heap_capacity = 10
    self.heap = [None] * self.heap_capacity
    self.heap_size = 0

    start = {"pos": start_pos, "prev": None, "steps": 0}
    self.__add(start)
    current_pos = self.__pop()

    while current_pos:
      current_row = current_pos["pos"][0]
      current_column = current_pos["pos"][1]
      current_char = self.height_map[current_row][current_column]
      if current_char == "E":
        return current_pos["steps"]
      
      neighbours = []
      current_char_val = ord(current_char)
      if current_char_val == 83: current_char_val = 97
      
      if (current_row - 1 > -1): 
        up_char = ord(self.height_map[current_row - 1][current_column])
        if up_char == 69: up_char = 122
        if up_char <= current_char_val + 1: neighbours.append((current_row - 1, current_column))
      if (current_row + 1 < len(self.height_map)):
        down_char = ord(self.height_map[current_row + 1][current_column])
        if down_char == 69: down_char = 122
        if down_char <= current_char_val + 1: neighbours.append((current_row + 1, current_column))
      if (current_column - 1 > -1):
        left_char = ord(self.height_map[current_row][current_column - 1])
        if left_char == 69: left_char = 122
        if left_char <= current_char_val + 1: neighbours.append((current_row, current_column - 1))
      if (current_column + 1 < len(self.height_map[current_row])):
        right_char = ord(self.height_map[current_row][current_column + 1])
        if right_char == 69: right_char = 122
        if right_char <= current_char_val + 1: neighbours.append((current_row, current_column + 1))

      for n in neighbours:
        if n not in self.indexes:
          self.__add({"pos": n, "prev": None, "steps": maxsize})
        neighbour_idx = self.indexes[n]
        if neighbour_idx == None:
          continue
        neighbour = self.heap[neighbour_idx]
        new_distance = current_pos["steps"] + 1
        if new_distance < neighbour["steps"]:
          neighbour["steps"] = new_distance
          neighbour["prev"] = current_pos
          self.__heapify(neighbour_idx)
      current_pos = self.__pop()

  def __pop(self):
    if self.heap[0] == None:
      return None
    popped_pos = self.heap[0]
    if self.heap_size > 1:
      self.heap[0] = self.heap[self.heap_size - 1]
      self.indexes[self.heap[0]["pos"]] = 0
    self.heap_size -= 1
    self.indexes[popped_pos["pos"]] = None
    self.heap[self.heap_size] = None
    self.__heapify_down(0)
    return popped_pos

  def __add(self, pos):
    self.__ensure_heap_capacity()
    self.heap[self.heap_size] = pos
    self.indexes[pos["pos"]] = self.heap_size
    self.heap_size += 1

  def __ensure_heap_capacity(self):
    if self.heap_size == self.heap_capacity:
      added_capacity = [None] * self.heap_capacity
      self.heap_capacity = self.heap_capacity * 2
      self.heap = self.heap + added_capacity
    
  def __swap(self, idx_1, idx_2):
    pos_1, pos_2 = self.heap[idx_1]["pos"], self.heap[idx_2]["pos"]
    self.indexes[pos_1], self.indexes[pos_2] = idx_2, idx_1
    self.heap[idx_1], self.heap[idx_2] = self.heap[idx_2], self.heap[idx_1]

  def __heapify(self, idx):
    if idx == 0 or not self.heap[(idx - 1) // 2]["steps"] > self.heap[idx]["steps"]:
      self.__heapify_down(idx)
    else:
      self.__heapify_up(idx)

  def __heapify_down(self, idx):
    while (2 * idx) + 1 < self.heap_size:
      child_idx = (2 * idx) + 1
      if (2 * idx) + 2 < self.heap_size and self.heap[(2 * idx) + 2]["steps"] < self.heap[(2 * idx) + 1]["steps"]:
        child_idx = (2 * idx) + 2
      if self.heap[idx]["steps"] < self.heap[child_idx]["steps"]:
        break
      self.__swap(idx, child_idx)
      idx = child_idx

  def __heapify_up(self, idx):
    while (idx - 1) // 2 >= 0 and self.heap[(idx - 1) // 2]["steps"] > self.heap[idx]["steps"]:
      parent_idx = (idx - 1) // 2 
      self.__swap(parent_idx, idx)
      idx = parent_idx

def main():
  height_map = get_data(day=12, year=2022)
  height_map = height_map.split("\n")
  starting_positions = []
  for i, row in enumerate(height_map):
    for j, char in enumerate(row):
      if char == "S":
        start_pos = (i, j)
        starting_positions.append((i, j))
      elif char == "a":
        starting_positions.append((i, j))

  m = Map(height_map)
  """ Part 1 """
  steps = m.search(start_pos)
  print(f"Got to the location with the best signal in {steps} steps.")
  """ Part 2 """
  steps = []
  for pos in starting_positions:
    res = m.search(pos)
    if res: steps.append(res)
  print(f"Shortest path from one of the lowest points to the location with the best signal takes {min(steps)} steps.")
        
if __name__=="__main__":
  main()