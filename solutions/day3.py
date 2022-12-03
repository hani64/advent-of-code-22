with open("input.txt", "r") as f:
  lines = [line.rstrip() for line in f]

# part1 
sum = 0
for line in lines:
  p1 = line[0:len(line)//2]
  p2 =  line[len(line)//2:]

  found = []
  for c in p1:
    if c in p2 and c not in found:
      if c.isupper():
        sum+= ord(c) - 38
      else:
        sum+= ord(c) - 96
      found.append(c)
print(sum)

#part 2
sum = 0
for i in range(0, len(lines), 3):
  l1, l2, l3 = lines[i], lines[i+1], lines[i+2]
  found = []
  for c in l1:
    if c in l2 and c in l3 and c not in found:
      if c.isupper():
        sum+= ord(c) - 38
      else:
        sum+= ord(c) - 96
      found.append(c)
print(sum)
