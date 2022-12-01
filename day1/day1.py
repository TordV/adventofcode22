from os import path, getcwd

def main():
  """ Day 1 - Part 1 """
  __location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))
  input_file = "day1_input"
  elf = 1
  current_elf_calories = 0
  max_calories = 0
  max_elf = None
  top_3_elves = [0, 0, 0]
  with open(path.join(__location__, input_file), "r", encoding='utf8') as f:
    for line in f:
      if len(line) == 1:
        if current_elf_calories > max_calories:
          max_calories = current_elf_calories
          max_elf = elf
        if current_elf_calories > top_3_elves[0]:
          top_3_elves[0] = current_elf_calories
        elf += 1
        current_elf_calories = 0
        top_3_elves.sort()
      else:
        current_elf_calories += int(line)
  top_3_elves_sum = top_3_elves[0] + top_3_elves[1] + top_3_elves[2]
  print(f"Elf #{max_elf} is carrying the most calories ({max_calories}).")
  print(f"The top three elves is carrying {top_3_elves_sum} calories.")

if __name__=="__main__":
  main()