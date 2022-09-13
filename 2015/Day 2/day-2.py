cl = [[int(y) for y in x.split("x")] for x in open("input.txt").read().split("\n")]

def surface_area(length, width, height):
    return 2*length*width + 2*width*height + 2*length*height 

def wrap_slack(length, width, height):
    return min(length*width, width*height, length*height)

def distance(length, width, height):
    return length*width*height

def ribbon_slack(length, width, height):
    return min(2*length + 2*width, 2*width + 2*height, 2*length + 2*height)

def compute_areas(dimensions): 
    return sum([wrap_slack(x,y,z) + surface_area(x, y, z) for x, y, z in dimensions])

def compute_ribbon(dimensions):
    return sum([ribbon_slack(x,y,z) + distance(x,y,z) for x,y,z in dimensions])

print(surface_area(1,1,10))
print(compute_areas(cl))
print(compute_ribbon(cl))