from utils import startOpts, moveOpts

class Maz():
    def __init__(self, maze):
        self.maze=maze
        self.start, self.pos1, self.pos2 = self.find_starts()
        self.visited = [self.start]
        

    def __repr__(self):
        return str(self.maze)

    def find_starts(self):
        startx, starty = -1,-1
        for ind, val in enumerate(self.maze):
            for ind2, val2 in enumerate(val):
                if val2 == 'S':
                    self.start = (ind, ind2)
                    startx, starty = (ind, ind2)
        
        startops = self.find_start_opts(self.start)
        [pos1, pos2] = self.start_move(self.start,startops)

        return (startx, starty), pos1, pos2


    def find_start_opts(self, pos):
        (x,y) = pos
        options = []

        if x+1 <len(self.maze):
            if (npos := self.maze[x+1][y]) != '.':
                if npos in startOpts['N']:
                    options.append(startOpts['N'][npos])
        if x - 1 >= 0:
            if (npos := self.maze[x-1][y]) != '.':
                if npos in startOpts['S']:
                    options.append(startOpts['S'][npos])
        if y + 1 < len(self.maze[0]):
            if (npos := self.maze[x][y+1]) != '.':
                if npos in startOpts['E']:
                    options.append(startOpts['E'][npos])
        if y - 1 >= 0:
            if (npos := self.maze[x][y-1]) != '.':
                if npos in startOpts['W']:
                    options.append(startOpts['W'][npos])
        
        return options
    
    def move_single(self, pos):
        (x,y) = pos
        deltas = moveOpts[self.maze[x][y]]
        next_locs = []
        for (deltaX, deltaY) in deltas:
            next_locs.append((x+deltaX, y+deltaY))
        [next_loc] = [x for x in next_locs if x not in self.visited]
        self.visited.append(pos)

        return next_loc
    
    def move_both(self):
        self.pos1 = self.move_single(self.pos1)
        self.pos2 = self.move_single(self.pos2)

    def start_move(self, pos, options):
        final = []
        (x,y) = pos
        for option in options:
            (dX, dY) = option
            final.append((x+dX, y+dY))
        return final
        
    
    def meeting(self):
        return self.pos1 == self.pos2

def load_data(path):
    maze = []
    with open(path) as file:
        while line := file.readline():
            maze.append(line.strip())
    newMaz = Maz(maze)
    return newMaz

if __name__ == "__main__":
    data = load_data('input.txt')
    stepcount = 1
    while not data.meeting():
        print(data.pos1, data.pos2)
        stepcount += 1
        data.move_both()
    print(stepcount)
    