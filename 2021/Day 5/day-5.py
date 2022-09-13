cl = open("input.txt", "r").read().split("\n")

def solve(ls):
    positions = {}
    for instr in ls:
        left = instr.split(" -> ")[0]
        right = instr.split(" -> ")[1]
        x1 = int(left.split(",")[0])
        y1 = int(left.split(",")[1])
        x2 = int(right.split(",")[0])
        y2 = int(right.split(",")[1])
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                if (x1, y) in positions:
                    positions[(x1, y)] += 1
                else: positions[(x1, y)] = 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                if (x, y1) in positions:
                    positions[(x, y1)] += 1
                else: positions[(x, y1)] = 1
    count = 0
    for key in positions.keys():
        if positions[key] >= 2:
            count += 1
    return count

print(solve(cl))

def solve2(ls):
    positions = {}
    for instr in ls:
        left = instr.split(" -> ")[0]
        right = instr.split(" -> ")[1]
        x1 = int(left.split(",")[0])
        y1 = int(left.split(",")[1])
        x2 = int(right.split(",")[0])
        y2 = int(right.split(",")[1])
        if x1 == x2:
            for y in range(min(y1, y2), max(y1, y2)+1):
                if (x1, y) in positions:
                    positions[(x1, y)] += 1
                else: positions[(x1, y)] = 1
        if y1 == y2:
            for x in range(min(x1, x2), max(x1, x2)+1):
                if (x, y1) in positions:
                    positions[(x, y1)] += 1
                else: positions[(x, y1)] = 1
        if abs(x2-x1) == abs(y2-y1):
            for x, y in zip(ranger(x1, x2), ranger(y1, y2)):
                if (x, y) in positions:
                    positions[(x, y)] += 1
                else: positions[(x, y)] = 1
    count = 0
    for key in positions:
        if positions[key] >= 2:
            count += 1
    return count

def ranger(x1, x2):
    if x1 >= x2:
        return range(x1, x2-1, -1)
    if x1 < x2:
        return range(x1, x2+1)

print(solve2(cl))