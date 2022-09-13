cl = open("input.txt", "r").read().split("\n\n")

def plot_and_fold(cords, folds):
    points = plot_points(cords)
    for fold in folds:
        direction = fold.split(" ")[2].split("=")[0]
        line = int(fold.split(" ")[2].split("=")[1])
        points = fold_paper(points, direction, line)
    return points

def plot_points(points):
    paper = []
    for x,y in [[int(a) for a in b.split(",")] for b in points]:
        paper.append((x, y))
    return paper

def fold_paper(points, direction, line):
    if direction == "x":
        saved = set([point for point in points if point[0] < line])
        for folder in [point for point in points if point[0] > line]:
            saved.add(((line - (folder[0] - line)), folder[1]))
        return list(saved)
    if direction == "y":
        saved = set([point for point in points if point[1] < line])
        for folder in [point for point in points if point[1] > line]:
            saved.add((folder[0], line - (folder[1] - line)))
        return list(saved)

def draw_points(points):
    height = max([z[1] for z in points])
    width = max([z[0] for z in points])
    array = [["." for i in range(width+1)] for j in range(height+1)]
    for point in points:
        array[point[1]][point[0]] = "#"
    for y in array:
        print(y)
    return array
    

print(plot_points(cl[0].split("\n")))

# Part 1
fold_once = plot_and_fold(cl[0].split("\n"), [cl[1].split("\n")[0]])
print(fold_once)
print(len(fold_once))

# Part 2
fold_all = plot_and_fold(cl[0].split("\n"), cl[1].split("\n"))
print(fold_all)
print(len(fold_all))
print(draw_points(fold_all))