my_file = open("input.txt", "r")
content = my_file.read()
content_list = content.split("\n")
integer_map = map(int, content_list)
integer_list = list(integer_map)

bruh = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]

def increasers(lis):
    increases = 0
    for _ in range(len(lis) - 1):
        if lis[_] < lis[_+1]:
            increases+=1
    return increases
print(increasers(integer_list))

def triplets(lis):
    increases = 0
    for _ in range(len(lis) - 3):
        setA = lis[_] + lis[_+1] + lis[_+2]
        setB = lis[_+1] + lis[_+2] + lis[_+3]
        if setA < setB:
            increases+=1
    return increases
print(triplets(integer_list))