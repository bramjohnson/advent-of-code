import math

cl = [[int(y) for y in x] for x in open("input.txt", "r").read().split("\n")]

yrange = range(len(cl))
xrange = range(len(cl[0]))

def get_neighbors(x, y):
    neighbors = []
    if y + 1 in yrange:
        neighbors.append({"x": x, "y": y+1})
    if y - 1 in yrange:
        neighbors.append({"x": x, "y": y-1})
    if x + 1 in xrange:
        neighbors.append({"x": x+1, "y": y})
    if x - 1 in xrange:
        neighbors.append({"x": x-1, "y": y})
    return neighbors

def lowest_neighbor(val, neighbors):
    return val < min(neighbors)

def find_low_points(map):
    lowests = [[{"x":x, "y":y} for x in range(len(map[y])) if lowest_neighbor(map[y][x], [map[z["y"]][z["x"]] for z in get_neighbors(x, y)])] for y in range(len(map))]
    lowests = [x for x in lowests if len(x) != 0]
    return [x for l in lowests for x in l]

def find_basins(lows, map):
    def navigate_basins(x, y):
        visited = set([(x,y)])
        for neighbor in get_neighbors(x, y):
            if map[neighbor["y"]][neighbor["x"]] > map[y][x] and map[neighbor["y"]][neighbor["x"]] != 9:
                visited = visited.union(navigate_basins(neighbor["x"], neighbor["y"]))
        return visited
        
    highs = [navigate_basins(low_point["x"], low_point["y"]) for low_point in lows]
    return math.prod(sorted([len(x) for x in highs])[-3:])

print(find_basins(find_low_points(cl), cl))