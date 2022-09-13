cl = open("test.txt", "r").read().split("\n")

def gameboy(ls):
    for index in (range(len(ls))):
        modify = []
        for index2 in (range(len(ls))):
            if index == index2:        
                if ls[index].split(" ")[0] == "jmp":
                    modify.append("nop " + ls[index].split(" ")[1])
                elif ls[index].split(" ")[0] == "nop":
                    modify.append("jmp " + ls[index].split(" ")[1])
                else: 
                    modify.append(ls[index])
            else: 
                modify.append(ls[index2])
        print(modify)
        result = helper(modify, [], 0, 0)
        print(result)
        if result: return result

def helper(ls, visited, index, acc):
    if index == len(ls) - 1:
        return acc
    if index in visited:
        return False
    action = ls[index].split(" ")[0]
    inc = int(ls[index].split(" ")[1])
    visited.append(index)
    if action == "acc":
        return helper(ls, visited, index+1, acc + inc)
    if action == "jmp":
        return helper(ls, visited, index+inc, acc)
    if action == "nop":
        return helper(ls, visited, index+1, acc)

print(gameboy(cl))
