cl = open("input.txt", "r").read().split("\n")
cl = [int(x) for x in cl]

def xmas_init(preamble_number, ls):
    preamble = ls[:preamble_number]
    rest = ls[preamble_number:]
    return xmas(preamble, rest)

def xmas(preamble, rest):
    target = rest[0]
    for first in preamble:
        for second in preamble:
            if first + second == target:
                preamble.append(target)
                return xmas(preamble[1:], rest[1:])
    return target

def encryption_weakness(pivot, ls):
    for index in (range(len(ls))):
        smallest = ls[index]
        largest = ls[index]
        count = 0
        for number in ls[index:]:
            count += number
            if number > largest:
                largest = number
            if number < smallest:
                smallest = number
            if count == pivot and smallest != largest:
                return smallest + largest
    return False

xmas_number = xmas_init(25, cl)
print(xmas_number)
print(encryption_weakness(xmas_number, cl))