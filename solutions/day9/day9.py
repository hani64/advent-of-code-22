with open("input.txt", "r") as f:
  lines = [line.rstrip('\n') for line in f]

p1 = 2
p2 = 10
knots = [(0,0) for i in range(p2)]
visited = {(0, 0)}

for line in lines:
  dir, step = line.split(" ")

  for i in range(int(step)):
    if dir == 'R':
      knots[0] = (knots[0][0] + 1 , knots[0][1])
    if dir == 'L':
      knots[0] = (knots[0][0] - 1 , knots[0][1])
    if dir == 'U':
      knots[0] = (knots[0][0], knots[0][1] + 1)
    if dir == 'D':
      knots[0] = (knots[0][0], knots[0][1] - 1)

    for j in range(1, len(knots)):
      dx = knots[j-1][0] - knots[j][0]
      dy = knots[j-1][1] - knots[j][1]
      if abs(dx) > 1:
        move = 1 if dx > 0 else -1
        knots[j] = (knots[j][0] + move, knots[j][1])
        if abs(dy) == 1:
          knots[j] = (knots[j][0], knots[j][1] + dy)
      if abs(dy) > 1:
        move = 1 if dy > 0 else -1
        knots[j] = (knots[j][0] , knots[j][1] + move)
        if abs(dx) == 1:
          knots[j] = (knots[j][0] + dx, knots[j][1])
      if (j == len(knots) - 1):
        visited.add(knots[j])
print(len(visited))