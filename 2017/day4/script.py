def importData(path):
    lines = []
    with open(path) as file:
        while line := file.readline():
            line = line.split()
            lines.append([sort_string(s) for s in line])

    return lines
def sort_string(str):
    return ''.join(sorted(str))

def processLine(line):
    tracker = {}
    for val in line:
        if tracker.get(val, False) == False:
            tracker[val] = True
        else:
            return False
    return True
def processLines(lines):
    count = 0
    for line in lines:
        if processLine(line):
            count += 1
    print(count)

if __name__ == "__main__":
    lines = importData("input.txt")
    processLines(lines)