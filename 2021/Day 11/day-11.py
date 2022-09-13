tl = [[int(y) for y in x] for x in open("test.txt", "r").read().split("\n")]
cl = [[int(y) for y in x] for x in open("input.txt", "r").read().split("\n")]

def octosex(octopussy, steps):
    sex = octopussy
    flashes = 0
    for _ in range(steps):
        out = step(sex)
        sex = out["sex"]
        flashes += out["flashes"]
    return {"sex":sex, "flashes":flashes}

def octosex2(octopussy):
    sex = octopussy
    steps = 0
    while(True):
        out = step(sex)
        steps += 1
        sex = out["sex"]
        if out["flashes"] == len(octopussy)*len(octopussy[0]):
            return steps


def step(octopussy):
    counting_pussy = [[y+1 for y in x] for x in octopussy]
    visited = []
    while(len(find_nines(counting_pussy, visited)) > 0):
        nine_positions = find_nines(counting_pussy, visited)
        for pos in nine_positions:
            counting_pussy[pos[1]][pos[0]] = 0
            visited.append(pos)
            for y in range(-1, 2):
                for x in range(-1, 2):
                    if pos[1]+y in range(len(counting_pussy)) and pos[0]+x in range(len(counting_pussy[y])) and (pos[0]+x,pos[1]+y) not in visited:
                        counting_pussy[pos[1]+y][pos[0]+x] += 1
    return {"sex":counting_pussy, "flashes":len(visited)}
        
def find_nines(pussy, visited):
    nines = []
    for y in range(len(pussy)):
        for x in range(len(pussy[y])):
            spot = pussy[y][x]
            if spot > 9 and spot not in visited:
                nines.append((x,y))
    return nines

print(octosex(cl, 100)["flashes"])
print(octosex2(cl))