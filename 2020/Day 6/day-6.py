my_file = open("input.txt", "r")
content = my_file.read()
cl = content.split("\n\n")
cl = [x.replace("\n", " ") for x in cl]
cl = [x.split(" ") for x in cl]
bill = [["abc"], ["a", "b", "c"], ["ab", "ac"], ["a", "a", "a", "a"], ["b"]]

def any_yes(group):
    answers = set()
    for ans in group:
        for index in range(len(ans)):
            answers.add(ans[index])
    return answers

def all_yes(group):
    answers = set([entry for entry in group[0]])
    for ants in group:
        answers = set.intersection(answers, set([entry for entry in ants]))
    return answers

def count_yes(ls, func):
    return sum(map(len, map(func, ls)))

#part one
print(count_yes(cl, any_yes))

print(count_yes(cl, all_yes))

#part two
print(sum(len(set.intersection(*map(set, entry.split()))) for entry in open("input.txt").read().split("\n\n")))