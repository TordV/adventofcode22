from aocd import get_data

class Directory:
  def __init__(self, name, parent=None):
    self.name = name
    self.children = None
    self.parent = parent

class File:
  def __init__(self, name, size, parent):
    self.name = name
    self.size = size
    self.parent = parent

class Tree:
  def __init__(self):
    self.root = None
    self.total_dir_sum_under_100000 = 0
    self.used_space = 0

  def add_dir(self, name, parent=None):
    if not self.root:
      self.root = Directory(name)
      return self.root

    if parent == None:
      return print("No parent given and root is full.")

    def dfs(node):
      if node == parent:
        child = Directory(name, node)
        if not node.children:
          node.children = [child]
        else:
          node.children.append(child)
        return child
      if node.children:
        for child in node.children:
          if isinstance(child, Directory):
            found_child = dfs(child)
            if found_child:
              return found_child
      return None
    current_node = self.root
    child = dfs(current_node) 
    return child

  def add_file(self, name, size, parent):
    def dfs(node):
      if node == parent:
        if not node.children:
          node.children = [File(name, size, parent)]
        else:
          node.children.append(File(name, size, parent))
        return True
      if node.children:
        for child in node.children:
          if isinstance(child, Directory):
            added_file = dfs(child)
            if added_file:
              return
      return False
    current_node = self.root
    dfs(current_node)

  def count_dir_sum(self):
    def dfs(node, level):
      dir_sum = 0
      if node:
        print(f"|{'  |' * level}- dir {node.name}")
        if node.children:
          for child in node.children:
            if isinstance(child, Directory):
              dir_sum += dfs(child, level + 1)
            else:
              print(f"|{'  |' * (level + 1)}- {child.name} (size: {child.size})")
              dir_sum += int(child.size)
        if dir_sum <= 100000:
          self.total_dir_sum_under_100000 += dir_sum
        return dir_sum
    
    current_node = self.root
    self.used_space = dfs(current_node, 0)

  def find_dir_to_delete(self, size_to_delete):
    options = []
    def dfs(node):
      dir_sum = 0
      if node:
        if node.children:
          for child in node.children:
            if isinstance(child, Directory):
              dir_sum += dfs(child)
            else:
              dir_sum += int(child.size)
        if dir_sum >= size_to_delete:
          options.append(dir_sum)
        return dir_sum
    current_node = self.root
    dfs(current_node)
    options.sort()
    print(f"The smallest directory that can be deleted to free up {size_to_delete} space has a size of {options[0]}.")

def main():
  commands = get_data(day=7, year=2022)
  commands = commands.split("\n")
  file_tree = Tree()
  current_dir = None
  for command in commands:
    words = command.split(" ")
    first = words.pop(0)
    second = words.pop(0)
    if first == "$" and second == "cd":
      directory = words.pop(0)
      if directory == "..":
        current_dir = current_dir.parent
      else:
        current_dir = file_tree.add_dir(directory, current_dir)
    elif first != "$" and first != "dir":
      file_size = first
      file_name = second
      file_tree.add_file(file_name, file_size, current_dir)

  file_tree.count_dir_sum()

  unused_space = 70000000 - file_tree.used_space
  to_delete = 30000000 - unused_space

  print(f"Total system size: 70 000 000. Needed space: 30 000 000. Unused space: {unused_space}. To delete: {to_delete}")

  file_tree.find_dir_to_delete(to_delete)
          
if __name__=="__main__":
  main()