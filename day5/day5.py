from os import path, getcwd

class Crate:
  def __init__(self, value):
    self.value = value
    self.next_crate = None

class Stack:
  def __init__(self):
    self.head = None

  def add_crate(self, value):
    if self.head == None:
      self.head = Crate(value)
    else:
      current_head = self.head
      self.head = Crate(value)
      self.head.next_crate = current_head

  def remove_crate(self):
    popped_crate = self.head
    self.head = self.head.next_crate
    return popped_crate.value
  
  def peek(self):
    return self.head.value

def main():
  __location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))
  input_file = "day5_input"
  stacks = [Stack() for _ in range(9)]
  stack_lines = [] 

  with open(path.join(__location__, input_file), "r", encoding='utf8') as f:
    line = f.readline()
    line = line.strip("\n")
    
    while line != "":
      stack_lines.append(line)
      line = f.readline()
      line = line.strip("\n")
    stack_lines.reverse()
    stack_lines.pop(0)

    for line in stack_lines:
      for i in range(9):
        crate = line[i+(3*i):(4*i)+3]
        if crate != "   ":
          stacks[i].add_crate(crate)

    """ Task 1 """
    # for line in f:
    #   line = line.strip("\n")
    #   _, num_crates, _, from_crate, _, to_crate = line.split(" ")
    #   num_crates, from_crate, to_crate = int(num_crates), int(from_crate), int(to_crate)
    #   for _ in range(num_crates):
    #     crate = stacks[from_crate - 1].remove_crate()
    #     stacks[to_crate - 1].add_crate(crate)

    """ Task 2 """
    for line in f:
      line = line.strip("\n")
      _, num_crates, _, from_crate, _, to_crate = line.split(" ")
      num_crates, from_crate, to_crate = int(num_crates), int(from_crate), int(to_crate)
      crates = []
      for _ in range(num_crates):
        crates.append(stacks[from_crate - 1].remove_crate())
      crates.reverse()
      for crate in crates:
        stacks[to_crate - 1].add_crate(crate)

    top_of_stacks = ""
    for stack in stacks:
      top_of_stacks += stack.peek()[1:2]
    
    print(top_of_stacks)

if __name__=="__main__":
  main()