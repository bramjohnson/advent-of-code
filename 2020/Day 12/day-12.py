cl = open("input.txt", "r").read().split("\n")

directions = ['N', 'E', 'S', 'W']

def part1(cl):
    facing = 'E'
    positions = {"x": 0, "y": 0}
    for instr in cl:
        action = instr[0]
        amount = int(instr[1:])
        if action in directions:
            positions = move_cardinal(action, amount, positions)
        elif action == "L" or action == "R":
            facing = translate(action, amount, facing)
        else:
            positions = move_cardinal(facing, amount, positions)
    return abs(positions["x"]) + abs(positions["y"])

def part2(cl):
    facing = 'E'
    waypoint = {"x": 10, "y": 1}
    ship = {"x": 0, "y": 0}
    for instr in cl:
        action = instr[0]
        amount = int(instr[1:])
        if action in directions:
            waypoint = move_cardinal(action, amount, waypoint)
        elif action == "R":
            holder = waypoint["x"]
            waypoint["x"] = waypoint["y"]
            waypoint["y"] = -1 * holder
        elif action == "L":
            holder = waypoint["y"]
            waypoint["y"] = waypoint["x"]
            waypoint["x"] = -1 * holder
        else:
            ship = move_ship(amount, ship, waypoint)
    return abs(ship["x"]) + abs(ship["y"])

def move_ship(amt, ship, way):
    for times in range(amt):
        ship["x"] += way["x"]
        ship["y"] += way["y"]
    return ship

def translate(dir, degrees, cur):
    index = directions.index(cur)
    new_index = (index + int(degrees/90) * (int(dir == 'R') - int(dir == 'L'))) % 4
    return directions[new_index]

def move_cardinal(dir, amt, pos):
    if dir == 'N':
        pos["y"] += amt
    elif dir == 'S':
        pos["y"] -= amt
    elif dir == 'E':
        pos["x"] += amt
    elif dir == 'W':
        pos["x"] -= amt
    return pos

print(part1(cl))
print(part2(cl))