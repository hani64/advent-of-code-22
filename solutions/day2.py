with open("input.txt", "r") as f:
  lines = [line.rstrip() for line in f]

# Part 1
score = 0
for line in lines:
  p1 = ord(line[0]) - ord('A')
  p2 = ord(line[2]) - ord('X')
  if p1 == p2:                         # Draw
      score += 3 + ord(line[2]) - ord('X') + 1
  elif p2 == (p1 + 1) % 3:             # You Win
      score += 6 + ord(line[2]) - ord('X') + 1
  else:                                # You Lose
      score += 0 + ord(line[2]) - ord('X') + 1
print(score)

# Part 2
score = 0
for line in lines:
  if line [2] == 'Y':                 # Draw
      score += 3 + ord(line[0]) - ord('A') + 1
  elif line[2] == 'Z':                # You Win
      score += 6 + (ord(line[0]) - ord('A') + 1) % 3 + 1
  else:                               # You Lose
      score += 0 + (ord(line[0]) - ord('A') + 2) % 3 + 1
print(score)
