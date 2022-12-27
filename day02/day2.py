from os import path, getcwd

def main():
  __location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))
  input_file = "day2_input"
  letter_to_shape = {"A": "rock", "B": "paper", "C": "scissors", "X": "rock", "Y": "paper", "Z": "scissors"}
  points_per_shape = {"rock": 1, "paper": 2, "scissors": 3}
  shape_to_win_against = {"rock": "paper", "paper": "scissors", "scissors": "rock"}
  shape_to_lost_against = {"rock": "scissors", "paper": "rock", "scissors": "paper"}
  
  strategy_1_score = 0
  with open(path.join(__location__, input_file), "r", encoding='utf8') as f:
    for line in f:
      line.strip("\n")
      opponent, player = line.split()
      opponent_shape = letter_to_shape[opponent]
      player_shape = letter_to_shape[player]
      strategy_1_score += points_per_shape[player_shape]
      if shape_to_win_against[opponent_shape] == player_shape:
        strategy_1_score += 6
      elif player_shape == opponent_shape:
        strategy_1_score += 3
  print(f"Total score following the first strategy: {strategy_1_score}")

  strategy_2_score = 0
  with open(path.join(__location__, input_file), "r", encoding='utf8') as f:
    for line in f:
      line.strip("\n")
      opponent, result = line.split()
      opponent_shape = letter_to_shape[opponent]
      if result == "Y":
        strategy_2_score += 3
        strategy_2_score += points_per_shape[opponent_shape]
      elif result == "Z":
        strategy_2_score += 6
        strategy_2_score += points_per_shape[shape_to_win_against[opponent_shape]]
      else:
        strategy_2_score += points_per_shape[shape_to_lost_against[opponent_shape]] 
  print(f"Total score following the second strategy: {strategy_2_score}")

if __name__=="__main__":
  main()