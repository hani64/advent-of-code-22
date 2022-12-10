with open("input.txt", "r") as f:
  lines = [line.rstrip('\n') for line in f]


notRead = True
wait = 0
cycle = 1
sum = 1
signal = 0
crt_line = ['.' for i in range(40)]


while lines:
  # part 1
  if cycle in [20, 60, 100, 140, 180, 220]:
    signal += cycle*sum
  # part 2
  if cycle in range(1,241):
    if (cycle - 1) % 40 in range(sum-1,sum+2):
      crt_line[(cycle - 1) % 40] = '#'
    if (cycle - 1) % 40 == 39:
      print(''.join(c for c in crt_line))
      crt_line = ['.' for i in range(40)]
  if notRead:
    ins = lines[0].split(' ')
    if ins[0] == 'addx':
      wait = 1
    notRead = False
  if wait == 0:
    ins = lines.pop(0).split(' ')
    if ins[0] == 'addx':
      sum += int(ins[1])
    notRead = True
  else:
    wait -=1
  cycle += 1
print(signal)