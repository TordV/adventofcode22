from aocd import get_data

def main():
  movements = get_data(day=9, year=2022)
  movements = movements.split("\n")

  """ Part 1 """
  visited = set()
  head_x = 0
  head_y = 0
  tail_x = 0
  tail_y = 0
  visited.add((tail_x, tail_y))

  for move in movements:
    direction, step = move.split()
    for _ in range(int(step)):
      if direction == "R":
        head_x += 1
      elif direction == "L":
        head_x -= 1
      elif direction == "U":
        head_y += 1
      elif direction == "D":
        head_y -= 1

      x_diff = head_x - tail_x
      y_diff = head_y - tail_y

      if abs(x_diff) <= 1 and abs(y_diff) <= 1:
        continue

      if abs(x_diff) > 1:
        if x_diff > 0: tail_x += 1
        else: tail_x -= 1

      if abs(y_diff) > 1:
        if y_diff > 0: tail_y += 1
        else: tail_y -= 1

      if abs(x_diff) == 1 and abs(y_diff) > 1:
        tail_x += x_diff

      if abs(y_diff) == 1 and abs(x_diff) > 1:
        tail_y += y_diff
      
      if (tail_x, tail_y) not in visited:
        visited.add((tail_x, tail_y))

  print(f"The tail of the rope visited {len(visited)} positions atleast once.")

  """ Part 2 """
  tail_visited = set()
  positions = [[0, 0] for _ in range(10)]
  tail_visited.add((positions[9][0], positions[9][1]))

  def move_recursively(i):
    if i == 10:
      return

    x_diff = positions[i - 1][0] - positions[i][0]
    y_diff = positions[i - 1][1] - positions[i][1]

    if abs(x_diff) <= 1 and abs(y_diff) <= 1:
      move_recursively(i + 1)
    else:
      if abs(x_diff) > 1:
        if x_diff > 0: positions[i][0] += 1
        else: positions[i][0] -= 1

      if abs(y_diff) > 1:
        if y_diff > 0: positions[i][1] += 1
        else: positions[i][1] -= 1

      if abs(x_diff) == 1 and abs(y_diff) > 1:
        positions[i][0] += x_diff

      if abs(y_diff) == 1 and abs(x_diff) > 1:
        positions[i][1] += y_diff

      move_recursively(i + 1)
      
    if i == 9 and (positions[9][0], positions[9][1]) not in tail_visited:
      tail_visited.add((positions[9][0], positions[9][1]))

  for move in movements:
    direction, step = move.split()
    for _ in range(int(step)):
      if direction == "R":
        positions[0][0] += 1
      elif direction == "L":
        positions[0][0] -= 1
      elif direction == "U":
        positions[0][1] += 1
      elif direction == "D":
        positions[0][1] -= 1
      move_recursively(1)  

  print(f"The tail of the large rope visited {len(tail_visited)} positions atleast once.")
          
if __name__=="__main__":
  main()