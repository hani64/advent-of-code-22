with open("input.txt", "r") as f:
  lines = [line.rstrip('\n') for line in f]

visible = len(lines[0]) + len(lines[-1])
max_dist = 0
for i, line in enumerate(lines[1:-1]):
  visible += 2
  for j, tree in enumerate(line[1:-1]):
    # check top
    top_visible = True
    top_dist = 0
    for l in lines[i::-1]:
      top_dist += 1
      if int(l[j+1]) >= int(tree):
        top_visible = False
        break
    # check bottom
    bottom_visible = True
    bottom_dist = 0
    for l in lines[i+2:]:
      bottom_dist += 1
      if int(l[j+1]) >= int(tree):
        bottom_visible = False
        break
    # check right
    right_visible = True
    right_dist = 0
    for t in lines[i+1][j+2:]:
      right_dist += 1
      if int(t) >= int(tree):
        right_visible = False
        break
    # check left
    left_visible = True
    left_dist = 0
    for t in lines[i+1][j::-1]:
      left_dist +=1
      if int(t) >= int(tree):
        left_visible = False
        break
    curr_dist = top_dist * bottom_dist * right_dist * left_dist
    if curr_dist > max_dist:
      max_dist = curr_dist
    visible += top_visible or bottom_visible or right_visible or left_visible
print(visible)
print(max_dist)