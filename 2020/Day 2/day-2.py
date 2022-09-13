my_file = open("input.txt", "r")
content = my_file.read()
cl = content.split("\n")[:-1]

def parse(ls):
    count = 0
    for entry in ls:
        print(entry)
        low = int(entry.split(" ")[0].split("-")[0])
        high = int(entry.split(" ")[0].split("-")[1])
        char = entry.split(" ")[1][:1]
        password = entry.split(" ")[2]
        if valid_password(low, high, char, password):
            count+=1
    return count

def farse(ls):
    count = 0
    for entry in ls:
        print(entry)
        low = int(entry.split(" ")[0].split("-")[0])
        high = int(entry.split(" ")[0].split("-")[1])
        char = entry.split(" ")[1][:1]
        password = entry.split(" ")[2]
        if valid_hashword(low, high, char, password):
            count+=1
    return count

def valid_password(policy_low, policy_high, policy_char, password):
    count = password.count(policy_char)
    return (count >= policy_low) and (count <= policy_high)

def valid_hashword(first, second, char, password):
    return (password[first-1] + password[second-1]).count(char) == 1

print(farse(cl))