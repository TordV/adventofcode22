from aocd import get_data

def main():
  instructions = get_data(day=10, year=2022)
  instructions = instructions.split("\n")

  cycle = 0
  x = 1
  signal_strengt_cycles = [20, 60, 100, 140, 180, 220]
  signal_strengt_sum = 0

  for instruction in instructions:
    cycle += 1
    if cycle in signal_strengt_cycles:
      signal_strengt_sum += (cycle * x)
    if len(instruction) > 4:
      _, value = instruction.split()
      cycle += 1
      if cycle in signal_strengt_cycles:
        signal_strengt_sum += (cycle * x)
      x += int(value)

  print(f"The sum of the signal strength values is: {signal_strengt_sum}")

  crt = ["." for _ in range(240)]

  cycle = 0
  crt_pos = 0
  sprite_pos = 1

  for instruction in instructions:
    sprite_coords = list(range(sprite_pos, sprite_pos + 3))
    cycle += 1
    crt_pos = cycle % 40
    if crt_pos in sprite_coords:
      crt[cycle - 1] = "#"
    if len(instruction) > 4:
      _, value = instruction.split()
      cycle += 1
      crt_pos = cycle % 40
      if crt_pos in sprite_coords:
        crt[cycle - 1] = "#"
      sprite_pos += int(value)

  print(f"Image rendered by the CRT:")
  for i in range(40, len(crt) + 1, 40):
    print("".join(crt[i-40:i]))
          
if __name__=="__main__":
  main()