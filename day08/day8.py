from aocd import get_data

# messy code today, O(n^4)?

def main():
  tree_grid = get_data(day=8, year=2022)
  tree_grid = tree_grid.split("\n")

  visible_trees = 0
  visible_trees += len(tree_grid[0]) * 2
  visible_trees += (len(tree_grid) - 2) * 2
  max_scenic_score = -1

  for i, row in enumerate(tree_grid):
    if i == 0 or i == len(tree_grid) - 1:
      continue

    for j, tree in enumerate(row):
      if j == 0 or j == len(row) - 1:
        continue

      tree = int(tree)
      left = [int(n) for n in row[:j]]
      right = [int(n) for n in row[j+1:]]
      up = [int(row[j]) for row in tree_grid[:i]]
      down = [int(row[j]) for row in tree_grid[i+1:]]
                
      if tree > max(left) or tree > max(right) or tree > max(up) or tree > max(down):
        visible_trees += 1

      left_score, right_score, up_score, down_score = 0, 0, 0, 0
      left_idx = -1
      t = left[left_idx]
      while t <= tree:
        left_score += 1
        if t == tree or left_idx == (len(left) * -1):
          break
        left_idx -= 1
        t = left[left_idx]

      right_idx = 0
      t = right[right_idx]
      while t <= tree:
        right_score += 1
        if t == tree or right_idx == (len(right) - 1):
          break
        right_idx += 1
        t = right[right_idx]

      up_idx = -1
      t = up[up_idx]
      while t <= tree:
        up_score += 1
        if t == tree or up_idx == (len(up) * -1):
          break
        up_idx -= 1
        t = up[up_idx]

      down_idx = 0
      t = down[down_idx]
      while t <= tree:
        down_score += 1
        if t == tree or down_idx == (len(down) - 1):
          break
        down_idx += 1
        t = down[down_idx]
      
      scenic_score = left_score * right_score * up_score * down_score

      if scenic_score > max_scenic_score:
        max_scenic_score = scenic_score

  print(f"Total number of visible trees: {visible_trees}")
  print(f"The tree with the highest scenic score has a scenic score of: {max_scenic_score}")
          
if __name__=="__main__":
  main()