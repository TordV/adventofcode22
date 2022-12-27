from aocd import get_data
from json import loads

""" This code produces wrong solution """

class WrongOrder(Exception): pass

def main():
  data = get_data(day=13, year=2022)
  pairs = data.split("\n\n")
  pairs_in_right_order = 0

  def compare_list(left, right):
    for i in range(len(left)):
      if i > len(right) - 1: raise WrongOrder
      if type(left[i]) == int and type(right[i]) == int:
        if left[i] < right[i]: return True
        elif left[i] > right[i]: raise WrongOrder
      else:
        if type(left[i]) == int: left[i] = [left[i]]
        if type(right[i]) == int: right[i] = [right[i]]
        if compare_list(left[i], right[i]):
          return True
    return True

  for idx, pair in enumerate(pairs):
    pair = pair.split("\n")
    left = loads(pair[0])
    right = loads(pair[1])
    try:
      for i in range(len(left)):
        if i > len(right) - 1: raise WrongOrder
        if type(left[i]) == int and type(right[i]) == int:
          if left[i] < right[i]: break
          elif left[i] > right[i]: raise WrongOrder
        else:
          if type(left[i]) == int: left[i] = [left[i]]
          if type(right[i]) == int: right[i] = [right[i]]
          if compare_list(left[i], right[i]):
            break
      pairs_in_right_order += (idx + 1)
    except WrongOrder:
      continue

  print(pairs_in_right_order)
          
if __name__=="__main__":
  main()