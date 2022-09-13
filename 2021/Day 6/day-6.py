input = open("input.txt", "r").read().split(",")
input = [int(x) for x in input]

def lanternfish(start, days):
    fish = {key: 0 for key in range(8+1)}
    for guys in start:
        fish[guys] += 1
    for _ in range(days):
        fish = simulate_day(fish, 6, 8)
    return sum([x for x in fish.values()])

def simulate_day(start, cooltime, birthtime):
    placeholder = start[0]
    start = {index: start[index+1] for index in range(len(start)-1)}
    start[cooltime] += placeholder
    start[birthtime] = placeholder
    return start

print(lanternfish(input, 80))
print(lanternfish(input, 256))