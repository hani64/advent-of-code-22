with open("input.txt", "r") as f:
  lines = [line for line in f]

stackNum = 9
stacks = [ [] for i in range(stackNum) ]
stacks_p2 = [ [] for i in range(stackNum) ]
stackInput = True
for line in lines:
  if stackInput:
    i = 1
    for j in range(stackNum):
      if len(line) == 1:
        stackInput = False
        break
      if line[1] == '1':
        break
      if line[i] == ' ':
        pass
      else:
        stacks[j].append(line[i])
        stacks_p2[j].append(line[i])
      i += 4
  else:
    line = line.split(' ')
    q,f,t = int(line[1]), int(line[3]), int(line[5])
    # part 1
    for c in range(q):
      stacks[t-1].insert(0,stacks[f-1].pop(0))
    # part 2
    if q == 1:
      stacks_p2[t-1].insert(0,stacks_p2[f-1].pop(0))
    else:
      stacks_p2[t-1] = stacks_p2[f-1][0:q] + stacks_p2[t-1]
      stacks_p2[f-1] = stacks_p2[f-1][q:]
for i in range(stackNum):
  print(stacks[i][0],end='')
print()      
for i in range(stackNum):
  print(stacks_p2[i][0],end='')
print()