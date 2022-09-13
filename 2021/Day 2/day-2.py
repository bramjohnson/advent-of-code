my_file = open("Day 2\input.txt", "r")
content = my_file.read()
cl = content.split("\n")[:-1]

def submarine(lis):
    horizontal = 0
    depth = 0
    for instr in lis:
        uct = instr.split(" ")[0]
        tion = int(instr.split(" ")[1])
        if uct == "forward":
            horizontal+=tion
        if uct == "down":
            depth+=tion
        if uct == "up":
            depth-=tion
    return horizontal*depth

print(submarine(cl))

def complicated_submarine(lis):
    horizontal = 0
    depth = 0
    aim = 0
    for instr in lis:
        uct = instr.split(" ")[0]
        tion = int(instr.split(" ")[1])
        if uct == "forward":
            horizontal+=tion
            depth+=aim*tion
        if uct == "down":
            aim+=tion
        if uct == "up":
            aim-=tion
    return horizontal*depth

print(complicated_submarine(cl))