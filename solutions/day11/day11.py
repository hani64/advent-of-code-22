import re

with open("input.txt", "r") as f:
  lines = [line.rstrip('\n') for line in f]

p1 = False
monkey_items = []
monkey_ops = []
monkey_tests = []
for i in range(0,len(lines),7):
  monkey_items.append([int(item) for item in re.findall(r'\d+', lines[i+1])])
  monkey_ops.append(lines[i+2].split('=')[-1].lstrip())
  monkey_tests.append([int(re.findall(r'\d+', lines[i+3])[0]), int(re.findall(r'\d+', lines[i+4])[0]), int(re.findall(r'\d+', lines[i+5])[0])])


monkey_inspects = [0 for i in range(len(monkey_items))]
lcm = 1
for l in monkey_tests:
  lcm *= l[0]
for r in range(20 if p1 else 10000):
  for m in range(len(monkey_items)):
    while monkey_items[m]:
      monkey_inspects[m] += 1
      item = eval(monkey_ops[m].replace('old', str(monkey_items[m].pop(0))))
      # Part 1
      if p1:
        item = item // 3
      # Part 2
      else:
        item = item - (item // lcm) * lcm
      if item % monkey_tests[m][0] == 0:
        monkey_items[monkey_tests[m][1]].append(item)
      else:
        monkey_items[monkey_tests[m][2]].append(item)

sorted_inspects = sorted(monkey_inspects, reverse=True)
print(sorted_inspects[0] * sorted_inspects[1])