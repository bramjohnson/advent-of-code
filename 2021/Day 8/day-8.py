cl = [x.split(" | ") for x in open("input.txt", "r").read().split("\n")]

original = {0: set(["a", "b", "c", "e", "f", "g"]), 1: set(["c", "f"]), 2: set(["a", "c", "d", "e", "g"]),
3: set(["a", "c", "d", "f", "g"]), 4: set(["b", "c", "d", "f"]), 5: set(["a", "b", "d", "f", "g"]),
6: set(["a", "b", "d", "e", "f", "g"]), 7: set(["a", "c", "f"]), 8: set(["a", "b", "c", "d", "e", "f", "g"]),
9: set(["a", "b", "c", "d", "f", "g"])}

def find_output(signal, output):
    splitup = signal.split(" ")
    number = {0 : None, 1 : None, 2 : None, 3 : None, 4 : None, 5 : None, 6 : None, 7 : None, 8 : None, 9 : None}
    key = {"a": None, "b": None, "c": None, "d": None, "e": None, "f": None, "g": None}
    number[1] = set([y for y in [x for x in splitup if len(x) == 2][0]])
    number[7] = set([y for y in [x for x in splitup if len(x) == 3][0]])
    number[4] = set([y for y in [x for x in splitup if len(x) == 4][0]])
    number[8] = set([y for y in [x for x in splitup if len(x) == 7][0]])
    key["a"] = str(list(number[7] - number[1])[0])

    fun = {count_to_signal(signal.count(x)) : x for x in key.keys() if signal.count(x) in [4, 6, 9]}
    for foo in fun:
        key[foo] = fun[foo]
    
    key["d"] = str(list(number[4] - number[1] - set(key["b"]))[0])
    key["g"] = [x for x in key.keys() if signal.count(x) == 7 and x != key["d"]][0]
    key["c"] = str(list(set([x for x in key.keys()]) - set([key["a"], key["b"], key["d"], key["e"], key["f"], key["g"]]))[0])

    for foo in number.keys():
        parts = []
        for part in original[foo]:
            parts.append(key[part])
        number[foo] = set(parts)

    out = ""
    for thing in output.split(" "):
        for foo in number:
            if number[foo] == set([x for x in thing]):
                out += str(foo)

    return int(out)

def count_to_signal(num):
    if num == 4:
        return "e"
    elif num == 6:
        return "b"
    elif num == 9:
        return "f"

print(sum([find_output(s,o) for s,o in cl]))