from pprint import pprint as pp
class Pattern():
    def __init__(self, pat):
        self.pat = pat

    def __repr__(self):
        return '<Pat: ' + str(len(self.pat)) + '>'

    def split_vert(self, axis):
        l_width = len(self.pat[0][0:axis])
        r_width = len(self.pat[0][axis:])

        extend = min(l_width, r_width)
        
        left = []
        right = []
        for row in self.pat:
            left.append(row[axis - extend:axis])
            right.append(row[axis:axis + extend])
        
        flipped_left = [x[::-1] for x in left]

        return flipped_left, right
    
    def find_matches_vert_axis(self):
        matches = []
        for axis in range(1, len(self.pat[0])):
            left, right = self.split_vert(axis)
            if left == right:
                matches.append(axis)
        return matches
    
    def split_hor(self, axis):
        up_height = len(self.pat[0:axis])
        down_hieght = len(self.pat[axis:])

        extend = min(up_height, down_hieght)

        top = self.pat[axis - extend:axis]
        bottom = self.pat[axis:axis + extend]
        flipped_top = top[::-1]

        return flipped_top, bottom
    
    def find_matches_hor_axis(self):
        matches = []
        for axis in range(1, len(self.pat)):
            top, bot = self.split_hor(axis)
            if top == bot:
                matches.append(axis)
        return matches

    def score(self):
        total = 0
        vert_matches = self.find_matches_vert_axis()
        hor_matches = self.find_matches_hor_axis()
        if vert_matches:
            added = sum(vert_matches)
            total += added
        if hor_matches:
            added = sum(hor_matches) * 100
            total += added
        return total


        
        


def load_data(input):
    with open(input) as file:
        patterns = []
        curr = []
        while line := file.readline():
            # print(curr)
            if len(line.strip()) > 0:
                curr.append(line.strip())
            else:
                newPat = Pattern(curr)
                patterns.append(newPat)
                curr = []
        newPat = Pattern(curr)
        patterns.append(newPat)
        return patterns
    
if __name__ == "__main__":
    patterns = load_data("input.txt")
    grand_score = 0
    for ind, pattern in enumerate(patterns):
        if pattern.score() == 0:
            print("no reflection found for ", ind)
        grand_score += pattern.score()
    print(grand_score)
    # sing_pat = patterns[0]
    # print(sing_pat.find_matches_vert_axis())
    # print(sing_pat.find_matches_hor_axis())
    # print(sing_pat.split_hor(8))