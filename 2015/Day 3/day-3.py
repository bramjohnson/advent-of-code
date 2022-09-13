cl = [x for x in open("input.txt", "r").read()]

def deliver_presents(directions):
    x = 0
    y = 0
    houses = {(x,y): 1}
    for cardinal in directions:
        if cardinal == "v":
            y -= 1
        elif cardinal == ">":
            x += 1
        elif cardinal == "^":
            y += 1
        elif cardinal == "<":
            x -= 1
        if (x,y) in houses:
            houses[(x,y)] += 1
        else: houses[(x,y)] = 1
    return houses

def deliver_with_robo_santa(directions):
    x = 0
    y = 0
    rx = 0
    ry = 0
    turn = True
    houses = {(x,y): 2}
    for cardinal in directions:
        if turn: #santa moves
            if cardinal == "v":
                y -= 1
            elif cardinal == ">":
                x += 1
            elif cardinal == "^":
                y += 1
            elif cardinal == "<":
                x -= 1
            if (x,y) in houses:
                houses[(x,y)] += 1
            else: houses[(x,y)] = 1
        else:
            if cardinal == "v":
                ry -= 1
            elif cardinal == ">":
                rx += 1
            elif cardinal == "^":
                ry += 1
            elif cardinal == "<":
                rx -= 1
            if (rx,ry) in houses:
                houses[(rx,ry)] += 1
            else: houses[(rx,ry)] = 1
        turn = not turn
    return len(houses)

print(len(deliver_presents(cl)))
print(deliver_with_robo_santa(cl))