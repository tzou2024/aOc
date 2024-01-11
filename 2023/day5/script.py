from pprint import pprint
def importData(path:str):
    #process the input as list of strings
    # print(input)
    lines = []
    with open(path) as file:
        while line := file.readline():
            lines.append(line.strip())
    return lines

def get_seed_list(line):
    parts = line.split(": ")
    seeds = parts[1].split()
    seeds = [int(x) for x in seeds]
    return seeds

class Mapping:
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
        self.translations = []
    def load_set(self, dest_numb, source_numb, range_len):
        self.translations.append((source_numb, source_numb + range_len - 1, dest_numb - source_numb))
    def load_sets(self, lines):
        for i in lines:
            i = [int(x) for x in i.split()]
            self.load_set(i[0], i[1], i[2])



def processMapLines(lines):
    label = lines[0].split(" map:")
    label = "".join(label).strip()
    [source, _, dest] = "".join(label).split("-")
    newMap = Mapping(source, dest)
    newMap.load_sets(lines[1:])
    return newMap
    

def process_map_listings(lines):
    map_listings = []
    i = 0
    while i < len(lines):
        if len(lines[i]) <= 0:
            i += 1
        else:
            # start a grouping
            grouping = []
            while len(nextline := lines[i]) > 0:
                grouping.append(nextline)

                if i+1 >= len(lines):
                    break
                i+= 1
            map_listings.append(grouping)
            i += 1
        # 

    return map_listings

def processInput(lines):
    seeds = get_seed_list(lines[0])
    maps = process_map_listings(lines[1:])
        
    return seeds,maps

def seed_map(seed, map):
    for min, max, offset in map.translations:
        if min <= seed <= max:
            return seed + offset
    return seed

def seed_maps(seed, convertedMaps):
    for map in convertedMaps:

        seed = seed_map(seed, map)

    #     print(map.dest)
    #     print(seed)

    # print("++++++")
    return seed


if __name__ == "__main__":
    lines = importData("input.txt")
    seeds, maps = processInput(lines)
    # print(seeds, maps)
    convertedMaps = [processMapLines(mapper) for mapper in maps]
    # print("53-> ",convertedMaps[2].dest,seed_map(53, convertedMaps[2]))
    # pprint(convertedMaps[2].translations)
    finals = [seed_maps(seed, convertedMaps) for seed in seeds]
    print(finals)
    print(min(finals))