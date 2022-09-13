import os

my_file = open("input.txt", "r")
content = my_file.read()
cl = content.split("\n")[:-1]
integer_map = map(int, cl)
cl = list(integer_map)

def find_2020(ls):
    for num in ls:
        for num2 in ls:
            if (2020 - num - num2) in ls:
                return (2020-num-num2)*num*num2

print(find_2020(cl))