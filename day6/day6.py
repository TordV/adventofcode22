from os import path, getcwd

def main():
  __location__ = path.realpath(path.join(getcwd(), path.dirname(__file__)))
  input_file = "day6_input"

  with open(path.join(__location__, input_file), "r", encoding='utf8') as f:
    datastream = f.readline()
    datastream = datastream.strip("\n")
    packet_marker = None
  
    for i, _ in enumerate(datastream):
      if len(set(datastream[i-3:i+1])) == 4 and not packet_marker: 
        packet_marker = i + 1
      if len(set(datastream[i-13:i+1])) == 14: 
        message_marker = i + 1
        break

  print(f"Found start-of-packet marker after {packet_marker} characters.")
  print(f"Found start-of-message marker after {message_marker} characters.")
          
if __name__=="__main__":
  main()