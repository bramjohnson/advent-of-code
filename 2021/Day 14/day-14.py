import copy

cl = open("test.txt", "r").read().split("\n\n")
# cl = [int(x) for x in cl]
# cl = [x.split(",") for x in cl]

def make_dict(instructions):
    table = {}
    for instr in instructions:
        table[instr.split(" -> ")[0]] = instr.split(" -> ")[1]
    return table

def polymerization(start, instructions, loop):
    current = start
    table = make_dict(instructions)
    for _ in range(loop):
        new = current
        index = 0
        added = 0
        for index in range(len(current)-1):
            pair = current[index] + current[index+1]
            if pair in table:
                new = insert(new, index+added+1, table[pair])
                added += 1
            else: 
                new += current[index]
        current = new
    return current

def insert(cur, index, ins):
    return cur[:index] + ins + cur[index:]

def high_minus_low(ls):
    counts = []
    for letter in set(ls):
        counts.append(ls.count(letter))
    counts.sort()
    return counts[-1] - counts[0]

def supermerization(start, instructions, loop):
    ## Initalize the current dict
    current = {}
    for index in range(len(start)-1):
        current[start[index] + start[index+1]] = 1

    ## Initialize the count dict
    count = {}
    for index in range(len(start)):
        try: count[start[index]] += 1
        except: count[start[index]] = 1

    ## Initalize the instructions dict
    instr_table = make_dict(instructions)

    ## Loop the instructed amount of times
    for _ in range(loop):
        new = copy.deepcopy(current)
        for key in list(current):
            if key in instr_table and current[key] != 0:
                placeholder = current[key]
                if key[0] + instr_table[key] in new:
                    new[key[0] + instr_table[key]] += current[key] 
                else: new[key[0] + instr_table[key]] = current[key]
                if instr_table[key] + key[1] in new:
                    new[instr_table[key] + key[1]] += current[key] 
                else: new[instr_table[key] + key[1]] = current[key]
                if instr_table[key] in count:
                    count[instr_table[key]] += current[key]
                else: count[instr_table[key]] = current[key]
                new[key] -= placeholder
        current = new
    return count

part_1 = supermerization(cl[0], cl[1].split("\n"), 10)
print(max(part_1.values()) - min(part_1.values()))
part_2 = supermerization(cl[0], cl[1].split("\n"), 40)
print(max(part_2.values()) - min(part_2.values()))