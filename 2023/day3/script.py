import pprint as pp
gameboard = []
with open("input.txt") as file:
    for item in file:
        gameboard.append(item.strip())
    pp.pprint(gameboard)

def get_line_island(line):
    #return list of tuples of start and end of islands in a list
    onnumber = False
    starts = []
    ends = []
    i = 0
    while i < len(line):
        if line[i].isdigit():
            starts.append(i)
            while line[i].isdigit():
                i+=1
                if i == len(line):
                    break
            ends.append(i-1)
        i += 1
    combos = []
    for (a,b) in zip(starts, ends):
        combos.append((a,b))
    return combos

def get_islands(gameboard):
    bomblist = []
    for i in range(len(gameboard)):
        combos = get_line_island(gameboard[i])
        for (x, y) in combos:
            realx = x + i*len(gameboard)
            realy = y + i*len(gameboard)
            bomblist.append((realx, realy))
    return bomblist

bomblist = get_islands(gameboard)



special_characters = "!@#$%^&*()-+?_=,<>/"

def bomb_detect(gameboard, bomb):
    flattened = ''.join(gameboard)
    #given a gameboard and a bomb, detect if
    #first get left and right bounds
    (left, right) = bomb
    gamewidth = len(gameboard[0])
    if left % gamewidth - 1 < 0:
        leftbound = left
    else:
        leftbound = left - 1
        
    if (right + 1) % gamewidth == 0:
        rightbound = right
    else:
        rightbound = right + 1
    #first check left and right bounds for bombs

    if flattened[leftbound] in special_characters:
        return flattened[left:right + 1]
    if flattened[rightbound] in special_characters:
        return flattened[left:right + 1]
    #next compile list of above
    if leftbound - gamewidth < 0:
        upperleft = leftbound
    else:
        upperleft = leftbound - gamewidth
        
    if rightbound - gamewidth < 0:
        upperright = rightbound
    else:
        upperright = rightbound - gamewidth
    #check if bomb is in above: 
    for i in flattened[upperleft:upperright + 1]:
        if i in special_characters:
            return flattened[left:right + 1]
    

    
    #next compile list of below
    if leftbound + gamewidth > len(flattened):
        lowerleft = leftbound
    else:
        lowerleft = leftbound + gamewidth
        
    if rightbound - gamewidth >len(flattened):
        lowerright = rightbound
    else:
        lowerright = rightbound + gamewidth 

    for i in flattened[lowerleft:lowerright + 1]:
        if i in special_characters:
            return flattened[left:right + 1]

    return False
    

found = [bomb_detect(gameboard, x) for x in bomblist]

for x in range(len(found)):
    if found[x] == False:
        found[x] = 0
    else:
        found[x] = int(found[x])

print(found)
print(sum(found))

            
    
