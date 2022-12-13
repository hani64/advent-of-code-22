with open("input.txt", "r") as f:
  lines = [line.rstrip('\n') for line in f]


grid = []
target = (0, 0)
start = (0, 0)
a_cells = []
prev_cell = {}
for i, line in enumerate(lines):
  row = []
  for j, c in enumerate(line):
    row.append(c)
    prev_cell[(i,j)] = ''
    if c == 'S':
      start = (i, j)
      a_cells.append((i,j))
    if c == 'E':
      target = (i, j)
    if c == 'a':
      a_cells.append((i,j))
  grid.append(row)


def bfs(prev_cell, start, target):
  queue = []
  queue.append(start)
  visited = {start}

  while queue:
    # print(queue)
    curr = queue.pop(0)
    curr_elevation  = ord('a') if grid[curr[0]][curr[1]] == 'S' else ord(grid[curr[0]][curr[1]])
    up = (curr[0] - 1 , curr[1])
    down = (curr[0] + 1 , curr[1])
    left = (curr[0], curr[1] - 1)
    right = (curr[0] , curr[1] + 1)

    def valid_neighbour(n):
      if n not in prev_cell:
        return False
      diff = (ord('z') if grid[n[0]][n[1]] == 'E' else ord(grid[n[0]][n[1]])) - curr_elevation
      return diff <= 1

    neighbours = filter(valid_neighbour, [up, down, left, right])

    for n in neighbours:
      if n == target:
        prev = curr
        count = 0
        while prev != 'start':
          prev = prev_cell[prev]
          count += 1
        return count
      if n not in visited:
        visited.add(n)
        queue.append(n)
        prev_cell[n] = curr
  return float('inf')

# Part 1
p1 = dict(prev_cell)
p1[start] = 'start'
print(bfs(p1, start, target))

# Part 2
# This could be optimized by using a modified bfs
# to find the shortest path from 'E' to the first 'a' found
# I'm to lazy to implement this though :(
min = float('inf')
for a in a_cells:
  p2 = dict(prev_cell)
  p2[a] = 'start'
  path = bfs(p2, a, target)
  min = path if path < min else min
print(min)