from pprint import pprint as pp
import time
class Lazer():
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir
    def __repr__(self):
        return "< " + str(self.pos) + " | " + str(self.dir) + " >"
    
    def move(self, width, height):
        (x,y) = self.pos
        if self.dir == "N":
            if x - 1 >= 0:
                self.pos = (x - 1, y)
            else:
                self.pos = (-1, -1)

        elif self.dir == "S":
            if x + 1 <= height - 1:
                self.pos = (x + 1, y)
            else:
                self.pos = (-1, -1)

        elif self.dir == "E":
            if y + 1 <= width - 1:
                self.pos = (x, y + 1)
            else: self.pos = (-1, -1)

        elif self.dir == "W":
            if y - 1 >= 0:
                self.pos = (x, y-1)
            else:
                self.pos = (-1, -1)
            
    def set_heading(self, new_heading):
        self.dir = new_heading

class MirSplit():
    def __init__(self, type):
        self.type = type

    def __repr__(self):
        return "<MirSplit " + self.type + " >"
    
    def impact(self, dir):
        '''
        defining how a lazer heading impacting
        a mirror or splitter should behave
        '''
        match self.type:
            case ".":
                return [dir]
            case "/":
                if dir == "S":
                    return ["W"]
                elif dir == "E":
                    return ["N"]
                elif dir == "N":
                    return ["E"]
                elif dir == "W":
                    return ["S"]
            case "\\":
                if dir == "S":
                    return ["E"]
                elif dir == "E":
                    return ["S"]
                elif dir == "N":
                    return ["W"]
                elif dir == "W":
                    return "N"
            case "|":
                if dir == "S":
                    return ["S"]
                elif dir == "E":
                    return ["S", "N"]
                elif dir == "N":
                    return  ["N"]
                elif dir == "W":
                    return ["S", "N"]
            case "-":
                if dir == "S":
                    return ["E", "W"]
                elif dir == "E":
                    return "E"
                elif dir == "N":
                    return  ["E", "W"]
                elif dir == "W":
                    return ["W"]
        
class Cave():
    def __init__(self, layout):
        self.layout = layout
        self.lazers = [Lazer((0,0), "E")]
        self.visited = {}

    def __repr__(self):
        return "<Cave w %s lazers>" % len(self.lazers)

    def print_lazers(self):
        print("+++++++++++++++++")
        for lazer in self.lazers:
            if lazer.pos != (-1, -1):
                print(lazer)
        print("+++++++++++++++++")
    # def 
    def step(self):
        newlazers = []
        #for each lazer
        for lazer in self.lazers:
            if lazer.pos == (-1, -1):
                continue
            #add it to the visited
            self.visited[str(lazer.pos)] = True
            # figure out which type of mirsplit each lazer is in
            (x, y) = lazer.pos
            spot = self.layout[x][y]
            # figure out what headings need to happen
            impact = spot.impact(lazer.dir)
            # for each heading
            for heading in impact:
                replaceLazer = Lazer((x,y), heading)
                newlazers.append(replaceLazer)
        movedlazers = []
        for newlazer in newlazers:
            # print("moving lazer: ", newlazer)
            newlazer.move(len(self.layout[0]), len(self.layout))
            # print(newlazer)
            movedlazers.append(newlazer)
        self.lazers = movedlazers

    def cycle(self):
        counter = 0
        while len(self.lazers) > 0:
            self.step()
            # self.print_lazers()
            counter += 1
            self.print_layout()
            # time.sleep(.5)
            # if counter > 40:
            #     break
    
    def print_layout(self):
        through_layout = []
        for row in self.layout:
            through_layout.append("".join([x.type for x in row]))
        # pp(through_layout)
        for key in self.visited.keys():
            tup = key[1:len(key) - 1]
            [x, y] = [int(z) for z in tup.split(",")]
            row = list(through_layout[x])
            row[y] = "#"
            through_layout[x] = "".join(row)
        # pp(through_layout)
        print("==================")
        print(len(self.visited.keys()))
        print()
        print()
        # print(len(self.visited.keys()))



def load_data(path="input.txt"):
    with open(path,mode="r") as file:
        board = []
        while line := file.readline():
            items = [MirSplit(item) for item in line.strip()]
            board.append(items)
        newCave = Cave(board)
        return newCave

if __name__ == "__main__":
    newCave = load_data()
    newCave.cycle()
    newCave.print_layout()