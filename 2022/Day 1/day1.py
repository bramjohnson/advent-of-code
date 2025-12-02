input = [[int(y) for y in x.rstrip().split("\n")] for x in open("input.txt", "r").read().split("\n\n")]
print(input)

class Elf:
    def __init__(self, calories) -> None:
        self.calories = calories
        self.sum = sum(calories)

elves = [Elf(x) for x in input]

def part1(elves):
    elfsums = [elf.sum for elf in elves]
    return max(elfsums)

def part2(elves):
    elves = elves.copy()

    elfsums = [elf.sum for elf in elves]

    elfsorted = elfsums.copy()
    elfsorted.sort()
    elfsorted.reverse()

    return elfsorted[0] + elfsorted[1] + elfsorted[2]

print(part1(elves))
print(part2(elves))