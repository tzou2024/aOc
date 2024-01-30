def load_data(path:str):
    mapping = []
    with open(path, mode="r", encoding="utf-8") as file:
        while line := file.readline():
            mapping.append(line.strip())
    row_add = []
    col_add = []
    for ind  in range(len(mapping)):
        if check_empty_row(mapping, ind):
            row_add.append(ind)

    for ind in range(len(mapping[0])):
        if check_empty_column(mapping, ind):
            col_add.append(ind)
    adder = 0
    # print(len(row_add), len(col_add))
    for row in row_add:
        mapping = insert_row(mapping, row + adder)
        adder += 1

    adder = 0
    for col in col_add:
        mapping = insert_col(mapping, col + adder)
        adder += 1

    # print(len(mapping), len(mapping[0]))

    return mapping

def load_data_two(path):
    mapping = []
    with open(path, mode="r", encoding="utf-8") as file:
        while line := file.readline():
            mapping.append(line.strip())
    row_add = []
    col_add = []
    for ind  in range(len(mapping)):
        if check_empty_row(mapping, ind):
            row_add.append(ind)

    for ind in range(len(mapping[0])):
        if check_empty_column(mapping, ind):
            col_add.append(ind)

    galaxies = []
    for row_ind, row_val in enumerate(mapping):
        for col_ind, col_val in enumerate(row_val):
            if col_val == "#":
                galaxies.append((row_ind, col_ind))

    adjusted_galaxies = []
    for (row, col) in galaxies:
        adj_row = len([x for x in row_add if x < row])
        adj_col = len([x for x in col_add if x < col])
        adjusted_galaxies.append((row + adj_row, col + adj_col))

    return adjusted_galaxies

def process_mapping(mapping):
    '''
    return a list of galaxy coordinates from a mapping
    '''
    galaxies = []
    for row_ind, row_val in enumerate(mapping):
        for col_ind, col_val in enumerate(row_val):
            if col_val == "#":
                galaxies.append((row_ind, col_ind))
    return galaxies
    
def check_empty_row(mapping, ind):
    for val in mapping[ind]:
        if val != ".":
            return False
    return True

def check_empty_column(mapping, ind):
    for val in mapping:
        if val[ind] != ".":
            return False
    return True

def insert_row(mapping, ind):
    row_len = len(mapping[0])
    row = "." * row_len
    new_map = mapping[:ind] + [row] + mapping[ind:]
    return new_map

def insert_col(mapping, ind):
    new_map = []
    for val in mapping:
        new_map.append(val[:ind] + "." + val[ind:])
    return new_map

def hamilton_distance(point1, point2):
    (y1, x1) = point1
    (y2, x2) = point2

    x_dist = abs(x2 - x1)
    y_dist = abs(y2 - y1)

    # print("hor_dist", x_dist, x2, x1)
    # print('vert_dst', y_dist)

    return x_dist+y_dist

def sum_distances(galaxies):
    distances = 0
    pairs = 0 
    for ind1 in range(len(galaxies)):
        for ind2 in range(ind1 + 1, len(galaxies)):
            distance = hamilton_distance(galaxies[ind1], galaxies[ind2])
            # print(ind1 + 1, ind2+1, distance)
            # print(galaxies[ind1], galaxies[ind2])
            # print("+++++++++++++++++++++")
            distances += distance
    return distances, pairs

if __name__ == "__main__":
    data = load_data("input.txt")
    from pprint import pprint as pp
    galaxies = process_mapping(data)
    print(galaxies)
    print(load_data_two("input.txt"))
    # 