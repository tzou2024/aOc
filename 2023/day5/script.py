with open("input.txt") as file:
    for ind, val in enumerate(file):
        val = val.strip()
        print(len(val))