with open("input.txt", "r") as f:
  lines = [line.rstrip() for line in f]

subsets = 0
overlaps = 0
for line in lines:
  a,b = int(line.split(',')[0].split('-')[0]), int(line.split(',')[0].split('-')[1])
  c,d = int(line.split(',')[1].split('-')[0]), int(line.split(',')[1].split('-')[1])
  # part 1
  if (a <= c and b >= d) or (a >= c and b <= d):
    subsets += 1
  # part 2
  if a <= d and b >= c:
    overlaps +=1
print(subsets, overlaps)
