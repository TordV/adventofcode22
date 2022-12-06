from aocd import get_data

def main():

  datastream = get_data(day=6, year=2022)

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