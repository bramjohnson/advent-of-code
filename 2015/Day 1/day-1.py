cl = [char for char in open("input.txt", "r").read()]

print(cl.count("(") - cl.count(")"))

floor = 0
for index in range(len(cl)):
    if cl[index] == "(":
        floor += 1
    else: floor -= 1
    if floor < 0:
        print(index+1)
        break