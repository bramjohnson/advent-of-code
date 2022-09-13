import math

cl = open("input.txt", "r").read().split("\n")

opening = ["[", "{", "(", "<"]
closing = ["]", "}", ")", ">"]
scores = {")": 3, "]": 57, "}": 1197, ">": 25137}
scores2 = {")": 1, "]": 2, "}": 3, ">": 4}

def part1(lines):
    return sum([get_score(line) for line in lines])

def get_score(line):
    next_expected = []
    for char in line:
        if char in opening:
            next_expected.append(char)
        if char in closing:
            next = next_expected.pop()
            if char != closing[opening.index(next)]:
                return scores[char]
    return 0

def get_expected(line):
    next_expected = []
    for char in line:
        if char in opening:
            next_expected.append(char)
        if char in closing:
            next_expected.pop()
    return reversed([closing[opening.index(expect)] for expect in next_expected])

def part2(lines):
    scores = sorted([find_closers(line) for line in lines if not_corrupted(line)])
    scores = [score for score in scores if score != 0]
    middleIndex = math.floor((len(scores))/2)
    return scores[middleIndex]

def not_corrupted(line):
    return get_score(line) == 0

def find_closers(line):
    expected = get_expected(line)
    score = 0
    for char in expected:
        score *= 5
        score += scores2[char]
    return score

print(part1(cl))

print(part2(cl))
