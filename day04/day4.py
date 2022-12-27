from os import path, getcwd

def main():
  __location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))
  input_file = "day4_input"
  fully_contains_count = 0
  overlap_count = 0
  with open(path.join(__location__, input_file), "r", encoding='utf8') as f:
    for line in f:
      line = line.strip("\n")
      line = line.replace("-", ",")
      sections = [int(n) for n in line.split(",")]
      start_1, end_1, start_2, end_2 = sections[0], sections[1], sections[2], sections[3]
      if (start_1 <= start_2 and end_1 >= end_2) or (start_2 <= start_1 and end_2 >= end_1):
        fully_contains_count += 1
      if end_1 >= start_2 and start_1 <= end_2: 
        overlap_count += 1
  print(f"Number of pairs where one assignment fully contains the other: {fully_contains_count}")
  print(f"Number of pairs where assignments overlap at all: {overlap_count}")

if __name__=="__main__":
  main()