file = open('input.txt', 'r')
numblist = []

numbdict = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}

def parseLine(line):
    digits = [x for x in line if x.isdigit()]
    # print(digits, line)
    return int(digits[0] + digits[-1])


def transformline(line):
    for i in range(len(line)):
        for j in range(len(line) - i):
            # print(line[i:j + 1])
            # print(line[i:i+j])
            if line[i:i+j] in numbdict.keys():
                saved = line[i:i+j]
                line = line.replace(saved, str(numbdict[saved]))
    return line
    

while True:
    line = file.readline()
    if not line:
        break
    line = transformline(line)
    print(line, parseLine(line))
    print()
    numblist.append(parseLine(line))
    print(sum(numblist))




