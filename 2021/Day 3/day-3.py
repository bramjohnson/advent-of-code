my_file = open("input.txt", "r")
content = my_file.read()
cl = content.split("\n")
bill = ['00100',
'11110',
'10110',
'10111',
'10101',
'01111',
'00111',
'11100',
'10000',
'11001',
'00010',
'01010']

# if 1:
#     print("hi")

most = ''
# print(range(len(cl[0])-1))
for x in range(len(cl[0])):
    ones = 0
    zeros = 0
    for line in cl:
        if line[x] == "1":
            ones+=1
        else: zeros+=1
    if ones > zeros:
        most += "1"
    else:
        most += "0"
# print(most)
# print(int(most, base=2))
least = most.replace("0", "2")
least = least.replace("1", "0")
least = least.replace("2", "1")
# print(least)
# print(int(least, base=2))
# print(int(least, base=2) * int(most, base=2))

def find_most(bin, index):
    ones = 0
    zeros = 0
    for line in bin:
        if line[index] == "1":
            ones+=1
        else: zeros+=1
    if ones >= zeros:
        return 1
    else:
        return 0

def find_least(bin, index):
    ones = 0
    zeros = 0
    for line in bin:
        if line[index] == "1":
            ones+=1
        else: zeros+=1
    if ones < zeros:
        return 1
    else:
        return 0

def oxygen(bin, index):
    if len(bin) == 1:
        return int(bin[0], base=2)
    most = find_most(bin, index)
    newbin = [x for x in bin if str(most) in x[index]]
    return oxygen(newbin, index+1)

def co2(bin, index):
    if len(bin) == 1:
        return int(bin[0], base=2)
    least = find_least(bin, index)
    newbin = [x for x in bin if str(least) in x[index]]
    return co2(newbin, index+1)

# print(oxygen(cl, 0))
# print(co2(cl, 0))
print(oxygen(bill, 0))
print(co2(bill, 0))
print(oxygen(cl, 0) * co2(cl, 0))