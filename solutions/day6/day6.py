with open("input.txt", "r") as f:
  lines = [line.rstrip() for line in f]


for line in lines:
  idx_p1 = -1
  idx_p2 = -1
  for i in range(len(line)):
    # part 1
    if len(set(line[i:i+4])) == 4 and idx_p1 == -1:
      idx_p1 = i+4
    # part 2
    if len(set(line[i:i+14])) == 14 and idx_p2 == -1:
      idx_p2 = i+14
      break
  print(idx_p1, idx_p2)