with open("input.txt", "r") as f:
  lines = [line.rstrip('\n') for line in f]


cur_path = ['/']
dir = {'/': {}}
# {'/' : {} }
for i, line in enumerate(lines[1:]):
  if line[:4] == '$ cd':
    # remove dir to cur_path
    if line[-2:] == '..':
      cur_path.pop()
    # add dir to cur_path
    else:
      cur_path.append(line.split(' ')[2])
  if line[:4] == '$ ls':
    cur_dir = dir
    # get cur_dir
    for d in cur_path:
      cur_dir = cur_dir[d]
    # populate cur_dir
    for inner_line in lines[i+2:]:
      if inner_line[0] == '$':
        break
      # add empty dir
      if inner_line[:3] == 'dir':
        cur_dir[inner_line.split(' ')[1]] = {}
      # add file with size
      else:
        cur_dir[inner_line.split(' ')[1]] = int(inner_line.split(' ')[0])
# print(dir,'\n')

#part 1
def solve_p1(dir):
  if type(dir) == int:
    return (dir, 0)
  else:
    size, ans = 0,0
    for child in dir.values():
      child_size, child_ans = solve_p1(child)
      size += child_size
      ans += child_ans
    if size <= 100000:
      ans += size
    return (size, ans)
sol1 = solve_p1(dir)
    
size_needed = 30000000 - (70000000 - sol1[0])
def solve_p2(dir):
  if type(dir) == int:
    return (dir,0)
  else:
    size, ans = 0, float('inf')
    for child in dir.values():
      child_size, child_ans = solve_p2(child)
      size += child_size
      if child_ans >= size_needed and child_ans <= ans:
        ans = child_ans
    if size >= size_needed and size <= ans:
      ans = size
    return (size,ans)

sol2 = solve_p2(dir)
print(sol1[1])
print(sol2[1])



