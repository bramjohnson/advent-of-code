my_file = open("input.txt", "r")
content = my_file.read()
cl = content.split("\n")[:-1]

total_height = len(cl) - 1
total_width = len(cl[0])

def toboggan(xmod, ymod):
    x = 0
    y = 0
    trees_hit = 0
    while(y != total_height):
        x += xmod
        x = x%total_width
        y += ymod
        if cl[y][x] == "#":
            trees_hit += 1
    return trees_hit

# Part One
print(toboggan(3, 1))

# Part Two
print(toboggan(1, 1))
print(toboggan(5, 1))
print(toboggan(7, 1))
print(toboggan(1, 2))

print(toboggan(1, 1)*toboggan(3, 1)*toboggan(5, 1)*toboggan(7, 1)*toboggan(1, 2))