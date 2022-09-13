import math
from os import error
my_file = open("input.txt", "r")
content = my_file.read()
cl = content.split("\n")[:-1]

rows = range(128)
columns = range(8)

def seat_ID(instr):
    row_instr = instr[:7]
    col_instr = instr[7:]
    row = find_row(row_instr)
    col = find_column(col_instr)
    return (row*8)+col

def find_row(instr):
    rowers = rows
    for index in range(len(instr)):
        go = instr[index]
        if go == "F":
            rowers = rowers[:(math.floor(len(rowers) / 2))]
        else:
            rowers = rowers[(math.ceil(len(rowers) / 2)):]
    return rowers[0]

def find_column(instr):
    callers = columns
    for index in range(len(instr)):
        go = instr[index]
        if go == "L":
            callers = callers[:(math.floor(len(callers) / 2))]
        else:
            callers = callers[(math.ceil(len(callers) / 2)):]
    return callers[0]

def highest_ID(ls):
    highest = 0
    for entry in ls:
        seat_id = seat_ID(entry)
        if seat_id > highest:
            highest = seat_id
    return highest

def find_seat(ls):
    seats = list(map(seat_ID, cl))
    seats.sort()
    expected = seats[0]
    missing = []
    for id in seats:
        if id != expected:
            missing.append(expected)
            expected += 1
        expected += 1
    return missing

(print(find_seat(cl)))