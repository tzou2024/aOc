from pprint import pprint as pp

def load_data(path):
    with open(path) as file:
        platforms = list(file.readline().strip())
        while line := file.readline().strip():
            for ind, val in enumerate(line):
                platforms[ind] += val
        # print(platforms)
    return platforms

def leftshift(platform):
    platform_segments = platform.split("#")
    # print(platform_segments)
    adjusted = []
    for seg in platform_segments:
        seg_len = len(seg)
        filtered = [x for x in seg if x != "."]
        filtered = "".join(filtered)
        rightfill = "." * (seg_len - len(filtered))
        shifted = filtered + rightfill
        adjusted.append(shifted)
    # print("#".join(adjusted))
    return "#".join(adjusted)
def score(column):
    score = 0
    flipped = list(reversed(column))
    for multiplier in range(1,len(flipped) + 1):
        if flipped[multiplier - 1] == "O":
            score += multiplier
    return score

if __name__ == "__main__":
    data = load_data("input.txt")
    north = []
    grand_score = 0
    for column in data:
        north.append(leftshift(column))
    for column in north:
        grand_score += score(column)
    pp(data)
    pp(north)
    pp(grand_score)
    