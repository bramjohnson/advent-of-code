input = [x.rstrip() for x in open("./input.txt", "r").readlines()]

alphabet_values = {}
alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
for idx in range(len(alphabet)):
    alphabet_values[alphabet[idx]] = idx + 1

def rucksack_common(rucksacks):
    rucksack_sets = [set(x) for x in rucksacks] # list of sets

    while(len(rucksack_sets) > 1):
        first = rucksack_sets.pop()
        second = rucksack_sets.pop()
        rucksack_sets.append(first.intersection(second))

    last_element = rucksack_sets[0]
    if len(last_element) > 1:
        raise ValueError("Too many elements, check for correct input (should only be 1).")

    return list(last_element)[0]

def part1(input):
    answers = []
    for line in input:
        midpoint = len(line) // 2

        left = line[:midpoint]
        right = line[midpoint:]

        left_set = set(left)
        right_set = set(right)

        answers.append(rucksack_common([left_set, right_set]))
    return sum([alphabet_values[ans] for ans in answers])

def part2(input):
    answers = []
    for idx in range(0, len(input), 3):
        first = input[idx]
        second = input[idx+1]
        third = input[idx+2]
        
        answers.append(rucksack_common([set(first), set(second), set(third)]))
    return sum([alphabet_values[ans] for ans in answers])


print(part1(input))
print(part2(input))