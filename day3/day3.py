from os import path, getcwd

def main():
  __location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))
  input_file = "day3_input"
  
  with open(path.join(__location__, input_file), "r", encoding='utf8') as f:
    priority_sum = 0
    badge_priority_sum = 0
    group = []
    for line in f:
      line = line.strip("\n")
      group.append(line)
      if len(group) == 3:
        badge = list(set(group[0]).intersection(set(group[1]).intersection(set(group[2]))))[0]
        if badge.islower(): badge_priority_sum += ord(badge) - 96
        else: badge_priority_sum += ord(badge) - 38
        group = []
      middle = len(line) // 2
      compartment_1 = line[:middle]
      compartment_2 = line[middle:]
      common_char = list(set(compartment_1).intersection(set(compartment_2)))[0]
      if common_char.islower(): priority_sum += ord(common_char) - 96
      else: priority_sum += ord(common_char) - 38
    print(f"Priority sum of all duplicate items: {priority_sum}")
    print(f"Priority sum of all group badges: {badge_priority_sum}")

if __name__=="__main__":
  main()