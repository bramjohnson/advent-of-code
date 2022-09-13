cl = open("input.txt", "r").read().split("\n\n")
draws = [int(x) for x in cl[0].split(",")]
cards = [[[int(z) for z in y.split(" ") if z != ''] for y in x.split("\n")] for x in cl[1:]]

def first_winner(ls):
    draws = [int(x) for x in ls[0].split(",")]
    cards = [[[int(z) for z in y.split(" ") if z != ''] for y in x.split("\n")] for x in ls[1:]]
    called = set()
    for number in draws:
        called.add(number)
        for card in cards:
            if winning_card(card, called):
                return card_score(card, called) * number

def last_winner(ls):
    draws = [int(x) for x in ls[0].split(",")]
    cards = [[[int(z) for z in y.split(" ") if z != ''] for y in x.split("\n")] for x in ls[1:]]
    called = set()
    last_won = 0
    for number in draws:
        called.add(number)
        for card in cards:
            if winning_card(card, called):
                last_won = card_score(card, called) * number
                cards.remove(card)
    return last_won
        
def winning_card(card, numbers):
    for index in range(5):
        if len(numbers.intersection(set([card[0][index], card[1][index], card[2][index], card[3][index], card[4][index]]))) == 5:
            return True
    for row in card:
        if len(numbers.intersection(set(row))) == 5:
            return True
    return False

def card_score(card, numbers):
    all = 0
    for row in card:
        for num in row:
            if num not in numbers:
                all += num
    return all

print(something(cl))
print(last_winner(cl))