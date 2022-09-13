cl = [int(x) for x in open("input.txt", "r").read().split(",")]

def lowest_cost(ls):
    return min([find_fuel_cost(ls, num) for num in range(max(ls))])
        

def find_fuel_cost(ls, align):
    return sum([sum(range(1, abs(pos - align)+1)) for pos in ls])

print(lowest_cost(cl))