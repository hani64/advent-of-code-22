from functools import cmp_to_key

with open("input.txt", "r") as f:
  lines = [line.rstrip('\n') for line in f]


def compare(left, right):
    for i in range(min(len(left), len(right))):
        if type(left[i]) == int and type(right[i]) == int:
            if left[i] < right[i]:
                return True
            if left[i] > right[i]:
                return False
        elif type(left[i]) == list and type(right[i]) == list:
            if compare(left[i], right[i]) != None:
                return compare(left[i], right[i])
        else:
            if type(left[i]) == int:
                 if compare([left[i]], right[i]) != None:
                    return compare([left[i]], right[i])
            if type(right[i]) == int:
                if compare(left[i], [right[i]]) != None:
                    return compare(left[i], [right[i]])
    if len(left) == len(right):
        return None
    return len(left) < len(right)

sum = 0
packets = []
for i in range (0, len(lines), 3):
    l1, l2 = eval(lines[i]), eval(lines[i+1])
    packets.append(l1)
    packets.append(l2)
    if compare(l1, l2):
        sum += (i // 3) + 1
print(sum)

packets.append([2])
packets.append([6])
sorted_packet = sorted(packets, key=cmp_to_key(lambda l1, l2: -1 if compare(l1, l2) else 1))
print( (sorted_packet.index([2]) + 1) * (sorted_packet.index([6]) + 1) )
