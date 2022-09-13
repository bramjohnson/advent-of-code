my_file = open("input.txt", "r")
content = my_file.read()
cl = content.split("\n\n")

# Part One
def check_passports(ls):
    return len([x for x in map(valid_passport, ls) if x])

def valid_passport(passport):
    passport = passport.replace("\n", " ")
    passport = passport.split(" ")
    passport = list(map(lambda f: f.split(":")[0], passport))
    if "cid" in passport: return len(passport) == 8
    else: return len(passport) == 7

print(check_passports(cl))