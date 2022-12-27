from aocd import get_data
from copy import deepcopy

def main():
  notes = get_data(day=11, year=2022)
  notes = notes.split("\n")

  monkeys = []
  current_monkey = {"items": [], "operation": None, "test": None, "true": None, "false": None, "inspects": 0}

  for line in notes:
    if line == "":
      monkeys.append(current_monkey)
      current_monkey = {"items": [], "operation": None, "test": None, "true": None, "false": None, "inspects": 0}
    elif "Starting items" in line:
      items = line[18:].split(" ")
      for item in items:
        item = item.strip(",")
        current_monkey["items"].append(int(item))
    elif "Operation" in line:
      operation = line[19:]
      current_monkey["operation"] = operation
    elif "Test" in line:
      num = line[21:]
      current_monkey["test"] = int(num)
    elif "If true" in line:
      monkey = line[29:]
      current_monkey["true"] = int(monkey)
    elif "If false" in line:
      monkey = line[30:]
      current_monkey["false"] = int(monkey)
  monkeys.append(current_monkey)
  monkeys_copy = deepcopy(monkeys)

  """ Part 1 """
  for _ in range(20):
    for monkey in monkeys:
      while len(monkey["items"]) > 0:
        monkey["inspects"] += 1
        old = monkey["items"].pop(0)
        operation = monkey["operation"]
        new = eval(operation)
        new = new // 3
        if new % monkey["test"] == 0:
          monkeys[monkey["true"]]["items"].append(new)
        else:
          monkeys[monkey["false"]]["items"].append(new)

  inspections = []
  for monkey in monkeys:
    inspections.append(monkey["inspects"])
  inspections.sort()
  print(f"Level of Monkey Business after 20 rounds is {inspections.pop() * inspections.pop()}")

  """ Part 2 """
  monkeys = monkeys_copy

  mod = 1
  for monkey in monkeys:
    mod *= monkey["test"]

  for _ in range(10000):
    for monkey in monkeys:
      while len(monkey["items"]) > 0:
        monkey["inspects"] += 1
        old = monkey["items"].pop(0)
        operation = monkey["operation"]
        new = eval(operation)
        new %= mod
        if new % monkey["test"] == 0:
          monkeys[monkey["true"]]["items"].append(new)
        else:
          monkeys[monkey["false"]]["items"].append(new)

  inspections = []
  for monkey in monkeys:
    inspections.append(monkey["inspects"])
  inspections.sort()
  print(f"Level of Monkey Business after 10000 rounds is {inspections.pop() * inspections.pop()}")

if __name__=="__main__":
  main()